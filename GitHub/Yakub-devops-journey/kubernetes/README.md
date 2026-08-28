# Kubernetes

## Debugging order (learn this sequence, you will use it constantly)

```bash
kubectl get pods                  # 1. what state is it in?
kubectl describe pod <name>       # 2. read the EVENTS at the bottom - the answer is usually there
kubectl logs <name>               # 3. what did the application itself say?
kubectl logs <name> --previous    # 4. for CrashLoopBackOff: the logs of the run that died
kubectl exec -it <name> -- sh     # 5. get inside and look around
```

## What the states mean

| State | Usually means |
|---|---|
| `Pending` | No node can schedule it: not enough CPU/memory, or a PVC that will not bind |
| `ImagePullBackOff` | Wrong image name/tag, or a private registry with no pull secret |
| `CrashLoopBackOff` | The container starts and exits. Read `logs --previous` |
| `Running` but not `Ready` | The readiness probe is failing - check the path and the port |
| `OOMKilled` | It exceeded its memory limit |

## Helm

```bash
helm lint ./helm/vprofile
helm install vprofile ./helm/vprofile --dry-run --debug   # render without applying
helm install vprofile ./helm/vprofile
helm upgrade vprofile ./helm/vprofile --set image.tag=v2
helm rollback vprofile 1
helm uninstall vprofile
kubectl delete pvc --all    # PVCs SURVIVE helm uninstall and keep costing money
```
