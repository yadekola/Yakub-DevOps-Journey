# Capstone troubleshooting notes

Fill this in as you build. These notes turn "I did a project" into "I can talk about this
project for twenty minutes".

## Template per entry

**Symptom:**
**What I first assumed:**
**How I checked:**
**Actual cause:**
**Fix:**
**How I would catch it faster next time:**

---

## Likely candidates (you will probably hit at least three)

- Argo CD shows `OutOfSync` but will not sync — RBAC on the target namespace
- `ImagePullBackOff` from ECR — the node IAM role lacks `ecr:GetAuthorizationToken`
- GitHub Actions cannot push to ECR — OIDC trust policy has the wrong `sub` condition
- EKS nodes never join the cluster — subnet tagging or the aws-auth ConfigMap
- PVC stuck `Pending` — no EBS CSI driver installed on the cluster
- Ingress created but no address — no ingress controller, or no load balancer controller
- API pod `CrashLoopBackOff` — DATABASE_URL points at a service that is not ready yet
- Readiness probe failing — you pointed it at `/healthz` instead of `/readyz`, or vice versa
- Prometheus target DOWN — the Service has no port named for the scrape annotation
