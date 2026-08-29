# Capstone — GitOps deployment of a multi-tier application to Kubernetes on AWS

**Built: 26–31 October 2026.** This is the project you will talk about in interviews.

> **The application is `../capstone-app/stockpulse/`** — a Python/FastAPI + PostgreSQL +
> Redis inventory tracker, deliberately a different stack from the course's vProfile app so
> this project is not recognisable as a tutorial. Read that README and its
> `docs/CAPSTONE_TASKS.md` before starting.

## The one-sentence version

*"I push a commit to GitHub, and a few minutes later that change is running on a Kubernetes
cluster on AWS, with monitoring, without anyone running a deploy command."*

## Why this project

Every earlier week produced one capability. This project is the only one that requires all
of them at once, which is exactly why it is worth building. If any single piece is shaky,
the pipeline stops — so it cannot be faked.

## Architecture

```
   Developer
       |  git push
       v
   GitHub  ──────────────────────────────────────────┐
       |  triggers                                   │ (Helm chart repo — Git is the
       v                                             │  single source of truth)
   GitHub Actions                                    │
       ├── pytest (18 tests, no services needed)     │
       ├── ruff lint                                 │
       ├── Trivy scan (fails on HIGH/CRITICAL)       │
       ├── Build Docker images (multi-stage)         │
       ├── Push images to Amazon ECR                 │
       └── Update image tag in the Helm chart ───────┘
                                                     |
                                                     v
                                                 Argo CD
                                            (detects drift, syncs)
                                                     |
                                                     v
                          Amazon EKS  (provisioned by Terraform)
                                   |
        ┌──────────────┬───────────┴────────┬──────────────┐
     Ingress      stockpulse-api       postgres          redis
     (nginx)       (2 replicas)      (PVC-backed)      (optional)
                                   |
                                   v
                       Prometheus  ->  Grafana  ->  Slack alerts
```

## What each week contributed

| Week | Skill | Where it appears in the capstone |
|---|---|---|
| 1 | AWS fundamentals, security groups | EKS node group networking |
| 2 | Maven, Jenkins CI, quality gates | The build and analysis stages |
| 3 | GitHub Actions, secrets management | The entire CI pipeline |
| 4 | Terraform, Python/Boto3 | EKS + VPC provisioning, the cost auditor |
| 5 | Ansible, Prometheus, Grafana | The monitoring stack and alerting |
| 6 | VPC design, private subnets | Worker nodes in private subnets |
| 7 | Docker, multi-stage builds | The application images pushed to ECR |
| 8 | Kubernetes, Helm | The chart Argo CD syncs |
| 9 | GitOps, Argo CD | The deployment mechanism itself |

## Build order (do not reorder — each step depends on the last)

Detailed version with a checklist: `../capstone-app/stockpulse/docs/CAPSTONE_TASKS.md`

1. **Terraform: VPC + EKS + ECR + IAM.** Verify with `kubectl get nodes`.
2. **Helm chart** for StockPulse (api, web, postgres + PVC, redis, Ingress).
3. **Secrets created out of band** — `kubectl create secret`, never in Git.
4. **GitHub Actions pipeline** — test, lint, scan, build, push to ECR.
5. **Actions bumps the chart tag** and commits back to Git.
6. **Install Argo CD**, point it at the chart, enable auto-sync.
7. **Prometheus + Grafana**, scraping the app's own `/metrics`.
8. **The proof:** change one line, push, watch it reach the cluster untouched.

## Deliverables checklist

- [ ] `architecture/capstone.png` — a diagram you drew, not one you copied
- [ ] Application code extended with at least four exercises from `docs/EXERCISES.md`
- [ ] `capstone/terraform/` — VPC, EKS, ECR, IAM, destroyable with one command
- [ ] `.github/workflows/cd.yml` — the full pipeline
- [ ] `capstone/helm/` — the chart Argo CD watches
- [ ] Argo CD application manifest
- [ ] Prometheus + Grafana deployed, dashboard JSON committed
- [ ] `README.md` with reproduction instructions a stranger could follow
- [ ] `capstone/docs/troubleshooting.md` — everything that went wrong and how you fixed it
- [ ] Screenshots: pipeline green, Argo CD synced, app in a browser, Grafana dashboard
- [ ] A recorded 10–15 minute walkthrough
- [ ] `terraform destroy` run and verified

## The four demo moments

1. **The loop.** Change a line, commit, push, narrate the pipeline, refresh the browser.
2. **Kill the cache.** Delete the Redis pod. App keeps serving; `stockpulse_cache_up` drops
   to 0. *"A cache outage should be a slowdown, not an outage."*
3. **Trigger a business alert.** Sell stock down until `stockpulse_low_stock_items` crosses
   the threshold and Slack fires.
4. **Break it and fix it live.** Push something that fails the scan. Show the pipeline
   refusing to deploy.

## Interview questions to answer in writing

1. Walk me through what happens between your `git push` and the change being live.
2. What is GitOps and how is it different from a normal CD pipeline?
3. Where do your secrets live and why is that safe?
4. Why Terraform for the cluster instead of `eksctl` or the console?
5. What breaks if Argo CD goes down? What breaks if GitHub goes down?
6. How would you do a rollback? How would you do a zero-downtime deploy?
7. What does this architecture cost per month, and what would you cut first?
8. What would you change before running this in production?

## Cost warning

**EKS bills per cluster-hour, plus worker nodes, plus a NAT gateway, plus EBS volumes for
PVCs.** This is the most expensive thing in the whole plan. Build it in a focused session,
capture your screenshots, then destroy it. Rebuilding from your own Terraform is a feature,
not a chore — it proves the code works.

```bash
helm uninstall stockpulse
kubectl delete pvc --all
terraform destroy -auto-approve
aws eks list-clusters                    # expect []
python3 ../scripts/aws_audit.py --all-regions
```
