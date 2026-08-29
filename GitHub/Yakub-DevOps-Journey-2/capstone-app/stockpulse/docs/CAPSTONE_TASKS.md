# Wiring StockPulse into the Week 9 capstone

The app is the payload. The capstone is the *pipeline that delivers it*. This is the build
order for 26–31 October.

## Target architecture

```
   git push
      |
      v
GitHub Actions
   ├── pytest (18 tests, ~4s, no services needed)
   ├── ruff lint
   ├── Trivy scan (fails on HIGH/CRITICAL)
   ├── docker build (multi-stage) x2 images: api, web
   ├── push to Amazon ECR, tagged with the commit SHA
   └── bump the image tag in the Helm chart values.yaml, commit back to Git
                                  |
                                  v
                              Argo CD  (watches the chart, syncs automatically)
                                  |
                                  v
                    Amazon EKS (Terraform-provisioned)
        ┌──────────────┬──────────┴───────┬──────────────┐
     Ingress       api Deployment    postgres (PVC)    redis
     (nginx)       (2 replicas)      StatefulSet     Deployment
                        |
                        v
              Prometheus scrapes /metrics -> Grafana -> Slack alerts
```

## Build order

| # | Task | Done when |
|---|---|---|
| 1 | Terraform: VPC + EKS + ECR + IAM (OIDC for Actions) | `kubectl get nodes` works |
| 2 | Helm chart: api Deployment/Service, web Deployment/Service, Ingress, Postgres StatefulSet + PVC, Redis | `helm install` brings it all up |
| 3 | Secrets created out of band (`kubectl create secret`) | `grep -ri password helm/` returns nothing |
| 4 | GitHub Actions: test → lint → scan → build → push to ECR | Green run on a push to main |
| 5 | Actions bumps the chart tag and commits back | The chart's `values.yaml` shows the new SHA |
| 6 | Argo CD installed and pointed at the chart path | App shows Synced/Healthy |
| 7 | Prometheus + Grafana via Helm, scraping `/metrics` | `stockpulse_low_stock_items` visible in Grafana |
| 8 | Alert on `stockpulse_low_stock_items > 5` → Slack | Message arrives when you sell stock down |
| 9 | Seed job runs as a Kubernetes Job | 12 items visible in the browser |
| 10 | **The proof run** | Change one line, push, watch it reach the cluster untouched |

## Probes — use the right endpoint

```yaml
livenessProbe:
  httpGet: { path: /healthz, port: 8000 }    # never touches the DB
  initialDelaySeconds: 10
  periodSeconds: 20
readinessProbe:
  httpGet: { path: /readyz, port: 8000 }     # 503 while the DB is unreachable
  initialDelaySeconds: 5
  periodSeconds: 10
```

Getting these the wrong way round is one of the most common Kubernetes mistakes. Being able
to explain why is a strong signal.

## The four demo moments

Rehearse these. They are what people remember.

1. **The loop.** Change a line, commit, push. Narrate the pipeline as it runs. Refresh the
   browser — the change is live and you never ran a deploy command.

2. **Kill the cache.** `kubectl delete pod -l app=redis`. The app keeps serving; the badge
   in the UI flips permanently to "cache miss"; `stockpulse_cache_up` drops to 0 in Grafana.
   Say the line: *"a cache outage should be a slowdown, not an outage."*

3. **Trigger a business alert.** Sell stock down until `stockpulse_low_stock_items` crosses
   the threshold. The Slack message arrives. *"I alert on things the business cares about,
   not just CPU."*

4. **Break it and fix it live.** Push a change that fails the quality gate or the security
   scan. Show the pipeline refusing to deploy. This one demonstrates that the pipeline has
   teeth — a CI pipeline that can never fail is theatre.

## Cost control

EKS + NAT gateway + EBS volumes is the expensive part of the whole programme. Build in a
focused session, capture screenshots and the recording, then:

```bash
helm uninstall stockpulse
kubectl delete pvc --all          # PVCs survive uninstall and keep billing
terraform destroy -auto-approve
python3 ../../scripts/aws_audit.py --all-regions
```

If you need the demo again later, rebuild from your own Terraform. That rebuild *is* the
proof the code works — recruiters ask "could you rebuild it?" and you'll have done it.
