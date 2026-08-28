# GitHub Actions

## Secrets

Repository Settings > Secrets and variables > Actions. Required for `ci.yml`:

| Secret | What it is |
|---|---|
| `DOCKERHUB_USERNAME` | Your Docker Hub username |
| `DOCKERHUB_TOKEN` | An access token from Docker Hub, **not** your password |

Secrets are masked in logs. Variables are not — use variables only for non-sensitive values.

## Why `if: github.ref == 'refs/heads/main'`

Without it, every feature branch publishes an image. That is how junior mistakes reach
production registries. The condition is the branch protection.

## Debugging

- Re-run with debug logging: set repo secret `ACTIONS_STEP_DEBUG` to `true`.
- `permission denied` on push usually means the default `GITHUB_TOKEN` needs
  `permissions: packages: write` declared at job level.
