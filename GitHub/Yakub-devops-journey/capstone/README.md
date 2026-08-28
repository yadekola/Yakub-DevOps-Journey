# Capstone — GitOps deployment of a multi-tier application to Kubernetes on AWS

**Built: 26–31 October 2026.** This is the project you will talk about in interviews.

## The one-sentence version

*"I push a commit to GitHub, and a few minutes later that change is running on a
Kubernetes cluster on AWS, with monitoring, without anyone running a deploy command."*

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
       ├── Build (Maven)                             │
       ├── Unit tests                                │
       ├── SonarQube analysis + quality gate         │
       ├── Build Docker image (multi-stage)          │
       ├── Push image to Amazon ECR                  │
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
     Ingress        vproapp              vprodb         vprocache
     (nginx)      (Deployment)         (PVC-backed)     vpromq
                                   |
                                   v
                       Prometheus  ->  Grafana  ->  Slack alerts
```

## What each week contributed

| Week | Skill | Where it appears in the capstone |
|---|---|---|
| 1 | AWS fundamentals, security groups | EKS node group networking |
| 2 | Maven, Jenkins CI, quality gates | The build and SonarQube stages |
| 3 | GitHub Actions, secrets management | The entire CI pipeline |
| 4 | Terraform, Python/Boto3 | EKS + VPC provisioning, the cost auditor |
| 5 | Ansible, Prometheus, Grafana | The monitoring stack and alerting |
| 6 | VPC design, private subnets | Worker nodes in private subnets |
| 7 | Docker, multi-stage builds | The application image pushed to ECR |
| 8 | Kubernetes, Helm | The chart Argo CD syncs |
| 9 | GitOps, Argo CD | The deployment mechanism itself |

## Build order (do not reorder — each step depends on the last)

1. **Terraform: VPC + EKS.** `capstone/terraform/`. Verify with `kubectl get nodes`.
2. **ECR repository + IAM role** for GitHub Actions (use OIDC, not long-lived access keys).
3. **Helm chart** for the app — start from `kubernetes/helm/vprofile` and extend it.
4. **GitHub Actions pipeline** — build, scan, push to ECR, bump the tag in the chart.
5. **Install Argo CD**, point it at the chart repo, enable auto-sync.
6. **Prometheus + Grafana** via Helm, with your Week 5 dashboard imported.
7. **The proof:** change one line of application code, push, and watch it reach the cluster
   without touching kubectl. Record this. It is the demo.

## Deliverables checklist

- [ ] `architecture/capstone.png` — a diagram you drew, not one you copied
- [ ] Application source in its own repository
- [ ] `capstone/terraform/` — VPC, EKS, ECR, IAM, all destroyable with one command
- [ ] `.github/workflows/cd.yml` — the full pipeline
- [ ] `capstone/helm/` — the chart Argo CD watches
- [ ] Argo CD application manifest
- [ ] Prometheus + Grafana deployed, dashboard JSON committed
- [ ] `README.md` with reproduction instructions a stranger could follow
- [ ] `capstone/docs/troubleshooting.md` — everything that went wrong and how you fixed it
- [ ] Screenshots: pipeline green, Argo CD synced, app in a browser, Grafana dashboard
- [ ] A recorded 10–15 minute walkthrough
- [ ] `terraform destroy` run and verified at the end

## Demonstration instructions

Write these so that someone with an AWS account and no context can reproduce your project.
If your instructions require you to be in the room, they are not finished.

```
1. Prerequisites: AWS account, Terraform >= 1.5, kubectl, helm, an ECR repo.
2. cd capstone/terraform && terraform init && terraform apply
3. aws eks update-kubeconfig --name <cluster> --region <region>
4. kubectl create secret generic app-secret --from-literal=db-pass="$DB_PASS"
5. Install Argo CD, apply capstone/argocd-app.yaml
6. Push a commit. Watch Argo CD sync.
7. Reach the app at the Ingress hostname.
8. terraform destroy
```

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
helm uninstall vprofile
kubectl delete pvc --all
terraform destroy -auto-approve
aws eks list-clusters                    # expect []
python3 ../scripts/aws_audit.py --all-regions
```
