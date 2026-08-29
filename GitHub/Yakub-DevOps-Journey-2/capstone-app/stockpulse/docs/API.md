# API reference

Interactive docs are generated automatically at `/docs` when the app is running. This file
covers the parts the generated docs cannot explain: the reasoning.

## Status codes and what they mean here

| Code | When | Why not something else |
|---|---|---|
| 201 | Item or movement created | Not 200 — a resource was created and this is what tells the client so |
| 204 | Item deleted | No body to return |
| 404 | Unknown item id or SKU | |
| **409** | Duplicate SKU, or stock would go negative | **Not 500.** The server is fine; the request conflicts with current state. Returning 500 here would page an on-call engineer for a user typo. |
| 422 | Validation failure (negative quantity, missing field) | FastAPI/Pydantic returns this automatically |
| 503 | `/readyz` when the database is unreachable | Tells Kubernetes to stop sending traffic without restarting the pod |

**The 409 vs 500 distinction is worth rehearsing.** It's a small decision that shows you
think about the operator, not just the happy path.

## Movement kinds

| Kind | Effect | Use |
|---|---|---|
| `in` | `quantity += n` | Delivery received |
| `out` | `quantity -= n`, rejected if it would go negative | Sale or usage |
| `adjust` | `quantity = n` (absolute) | Physical stock take correction |

## Caching behaviour

Only `GET /api/summary` is cached, TTL 30 seconds, invalidated on every write to items or
movements.

The response includes `"cached": true|false` on purpose so the behaviour is *visible* —
the frontend badge flips between "cache hit" and "cache miss" every few seconds. When you
kill Redis in the demo it stays on "cache miss" and the app keeps working.

## Example session

```bash
BASE=http://localhost:8080

curl -s $BASE/api/summary

curl -s -X POST $BASE/api/items -H 'Content-Type: application/json' \
  -d '{"sku":"BEV-004","name":"Ginger Drink","category":"beverages","quantity":24,"reorder_level":6}'

# Sell six
curl -s -X POST $BASE/api/movements -H 'Content-Type: application/json' \
  -d '{"sku":"BEV-004","kind":"out","quantity":6,"note":"counter sale"}'

# Try to oversell -> 409, and nothing is written
curl -s -X POST $BASE/api/movements -H 'Content-Type: application/json' \
  -d '{"sku":"BEV-004","kind":"out","quantity":999}'

curl -s $BASE/api/items/low-stock
curl -s $BASE/api/movements?sku=BEV-004
curl -s $BASE/metrics | grep stockpulse_
```
