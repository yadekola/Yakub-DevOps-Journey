# Lab 8: Kubernetes deployment with Helm - CAPSTONE PHASE 1

**Week 8 — Saturday 24 October 2026**

## Objective

This lab is the first phase of your capstone. Provision an EKS cluster with Terraform (or run on Minikube if you want to avoid EKS cost), package the application as a Helm chart, and deploy it with secrets, persistent volumes, services and an Ingress.

## Why this lab exists

This is capstone phase 1. Everything you build today, you will wire into a GitOps pipeline next week — so build it as if someone else has to maintain it.

## Architecture

```
Terraform -> EKS cluster (or Minikube locally)
Helm chart -> Deployment, Service, Ingress, ConfigMap, Secret, PVC
  app pods -> mysql (PVC) | memcached | rabbitmq
Ingress controller -> browser
```

Draw your own version of this diagram before you start building. Save it to
`../../architecture/lab-08.png`. If you cannot draw it, you do not understand it yet.

## Prerequisites

- Lab 7 images published
- kubectl and helm installed
- Lectures 324-346 completed
- **Cost warning:** an EKS control plane bills hourly. Use Minikube if in doubt.

## Acceptance criteria

- [ ] Terraform-managed cluster, not a console-created one
- [ ] One Helm chart with a values.yaml that switches between dev and prod settings
- [ ] Secrets NOT committed - use kubectl create secret or an external secret reference
- [ ] A working Ingress you can reach in a browser

## Steps

1. **Get a cluster.** Minikube for zero cost, or Terraform-provisioned EKS if you accept
   the hourly charge and will destroy it the same day.

2. **Create the secrets out-of-band:**
   ```bash
   kubectl create secret generic app-secret \
     --from-literal=db-pass="$DB_PASS" --from-literal=rmq-pass="$RMQ_PASS"
   ```
   *Why not in YAML:* a Kubernetes Secret manifest is base64, not encryption. Committing it
   is committing the password.
   *Expected:* `kubectl get secret app-secret` shows the keys but not the values.

3. **Write the PVC for MySQL**, then the MySQL Deployment and Service.

4. **Write Deployments and Services** for memcached, rabbitmq and the app.

5. **Add an Ingress** and an ingress controller, and reach the app in a browser.

6. **Package it all as a Helm chart** with a `values.yaml` that can switch image tag,
   replica count and resource limits between dev and prod.

7. **Roll out a change and roll it back:** `helm upgrade`, then `helm rollback`.

## Verification

- [ ] `kubectl get pods` — all Running, no restarts
- [ ] `helm install` from a clean cluster brings everything up
- [ ] The app is reachable through the Ingress
- [ ] `kubectl rollout undo` restores the previous version
- [ ] `grep -ri password kubernetes/` returns nothing

## Troubleshooting challenges

Work these out yourself before looking anything up. Hints only — no answers.

1. **Pods stuck in Pending - describe the pod and read the events.**
   *Hint: Read the actual error, not the summary. Then ask: what changed?*
2. **CrashLoopBackOff on the app pod with a database connection refused error.**
   *Hint: Check the layer below the one you think is broken.*
3. **The PVC stays Pending forever on your cluster.**
   *Hint: Compare a working case with the broken one and list every difference.*

## Cleanup

```bash
helm uninstall vprofile
kubectl delete pvc --all       # PVCs survive helm uninstall and keep billing
terraform destroy -auto-approve   # if you used EKS
aws eks list-clusters          # expect an empty list
```
**Do not skip the PVC deletion.** Orphaned EBS volumes from deleted PVCs are the most
common surprise bill for people learning Kubernetes.

## Interview questions

Answer these in writing in `answers.md` before you consider the lab finished.

1. What is the difference between a Pod, a ReplicaSet and a Deployment?
2. How does a Service find its Pods?
3. Your pod is in CrashLoopBackOff. Walk me through your diagnosis.
4. What is the difference between a ConfigMap and a Secret? Is a Secret encrypted?
5. Why is a PVC needed for MySQL but not for the app tier?
6. What does Helm give you that raw `kubectl apply` does not?
