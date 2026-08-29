# Secrets in Kubernetes - read this before you commit anything

A Kubernetes Secret is **base64 encoded, not encrypted**. Anyone with the YAML has the
password. This is the most common mistake beginners make.

## Create secrets out of band, never in a committed file

```bash
kubectl create secret generic app-secret \
  --from-literal=db-pass="$DB_PASS" \
  --from-literal=rmq-pass="$RMQ_PASS"
```

**What this does:** stores the values in etcd inside the cluster.
**Why this way:** the values come from your shell environment, so they never touch a file
Git can see.
**Expected:** `kubectl get secret app-secret` shows key names and sizes, not values.

## Verify you have not leaked anything

```bash
grep -ri "password\|secret\|token" kubernetes/ --include="*.yaml"
```

Every hit should be a `secretKeyRef`, never a literal value.

## For the capstone

Use a sealed-secrets controller or an external secrets operator so the *encrypted* secret
can safely live in Git - that is what makes GitOps work without leaking credentials.
