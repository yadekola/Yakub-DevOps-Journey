# StockPulse

A small inventory tracker for a shop: items, stock movements, and low-stock alerts.

This is the **capstone application** for Yacoub's 60-day DevOps programme. It exists to be
deployed, broken, monitored and explained — not to be admired as software.

## Why this app and not the course app

The course uses vProfile (Java/Tomcat/MySQL/Memcached/RabbitMQ). Thousands of people have
completed that course and their repos all contain the same application, the same
Jenkinsfile and the same architecture. An interviewer who has seen two of them recognises
the third instantly.

StockPulse is a different stack — Python/FastAPI, PostgreSQL, Redis, static frontend — but
the same DevOps *shape*: a web tier, an API tier, a database, a cache. Every technique from
the course transfers directly, and nothing is copy-pasteable.

Use vProfile for Labs 1–8. Use StockPulse for the capstone.

## Architecture

```
Browser
   |
   v
Nginx (web)  ──── serves the static UI, reverse-proxies /api ────┐
                                                                 v
                                                        FastAPI (api)
                                                          |        |
                                                          v        v
                                                   PostgreSQL    Redis
                                                    (state)     (cache,
                                                                optional)
```

**Two design decisions worth defending in an interview:**

1. **The cache is optional.** If Redis dies, `/api/summary` gets slower but keeps working.
   Kill the Redis container and the app stays up — that's a degraded system, not a broken
   one. Most junior projects make the cache a hard dependency and turn a cache outage into
   a total outage.

2. **Liveness and readiness are different endpoints.** `/healthz` never touches the
   database; `/readyz` does. If liveness checked the database, one brief DB blip would make
   Kubernetes restart every healthy pod and turn a small problem into an outage.

## Run it

### Locally, no Docker (fastest for development)

```bash
cd api
pip install -r requirements-dev.txt
python -m app.seed          # loads 12 sample items
uvicorn app.main:app --reload --port 8000
```

Open http://localhost:8000/docs — FastAPI generates interactive API docs for free.
Uses SQLite, so no database server is needed.

### Full stack with Docker

```bash
cp .env.example .env        # then change the password
docker compose up -d --build
docker compose ps           # wait for "healthy", not just "Up"
```

Open **http://localhost:8080**.

```bash
make down     # stop; data survives
make clean    # stop and DELETE the database volume
```

### Tests

```bash
make test     # 18 tests, no running services required
```

The tests need no Postgres and no Redis — they run against SQLite with caching disabled.
**This is deliberate.** A test suite that requires infrastructure is a test suite that
gets skipped in CI. Yours will run in a GitHub Actions job in about four seconds.

## The API

| Method | Path | Purpose |
|---|---|---|
| GET | `/healthz` | Liveness. Never touches the database. |
| GET | `/readyz` | Readiness. 503 when the database is unreachable. |
| GET | `/metrics` | Prometheus exposition (plain text, not JSON) |
| GET | `/api/items` | List; supports `?search=` and `?category=` |
| POST | `/api/items` | Create. 409 on duplicate SKU. |
| GET | `/api/items/low-stock` | Items at or below reorder level |
| PATCH | `/api/items/{id}` | Update metadata (not quantity — see below) |
| DELETE | `/api/items/{id}` | Delete item and its movements |
| POST | `/api/movements` | Record stock in/out/adjust |
| GET | `/api/movements` | Audit trail, `?sku=` filter |
| GET | `/api/summary` | Dashboard totals (Redis-cached) |

Full docs at `/docs` when running.

### The one business rule that matters

`item.quantity` can **only** change through a movement, never through a direct update. So
every change has an audit row explaining it.

And stock cannot go negative. An `out` movement larger than the quantity on hand is
rejected with **409**, and *nothing* is written — not the movement, not the quantity
change. Both happen in one transaction or neither does.

```bash
curl -X POST localhost:8080/api/movements -H 'Content-Type: application/json' \
  -d '{"sku":"BEV-002","kind":"out","quantity":999}'
# {"detail":"insufficient stock for 'BEV-002': have 12, tried to remove 999"}
```

There is a test for exactly this (`test_rejected_movement_writes_nothing`). When an
interviewer asks "how do you handle partial failures?", this is your answer.

## Metrics for Grafana

`/metrics` exposes:

| Metric | Type | Use it for |
|---|---|---|
| `stockpulse_http_requests_total{method,path,status}` | counter | Request rate, error rate by status |
| `stockpulse_items_total` | gauge | Business metric on the dashboard |
| `stockpulse_units_total` | gauge | Total stock held |
| `stockpulse_low_stock_items` | gauge | **Alert on this** — a business alert, not a CPU alert |
| `stockpulse_cache_up` | gauge | Goes to 0 when Redis dies, app stays up |

An alert on `stockpulse_low_stock_items > 5` is far more interesting in an interview than
another CPU alert, because it shows you understand that monitoring exists to serve the
business, not the server.

## Secrets

Nothing secret is in this repository. The database password comes from `.env` locally
(gitignored), from GitHub Secrets in CI, and from a Kubernetes Secret created out of band
in the cluster. See `../../kubernetes/SECRETS.md`.

## Next

- `docs/EXERCISES.md` — 12 staged extensions, easy to hard. **Do these.** Deploying
  someone else's code teaches you deployment; extending it teaches you the codebase.
- `docs/CAPSTONE_TASKS.md` — how this app plugs into the Week 9 GitOps pipeline.
