# Architecture and source guide

## Request flow

1. Vite builds React into static assets. The browser loads index.html and generated CSS/JavaScript  at localhost:5173.
2. Browser JavaScript uses relative fetch URLs, such as `/api/products`.
3. fronend requests `/api/` requests to the `api` service on port 3000.
4. Express validates input and calls the product repository.
5. The repository executes parameterized SQL through a PostgreSQL connection pool.
6. Express returns JSON, and the frontend updates the page.


## Source responsibilities

| File | Responsibility |
|---|---|
| backend/src/server.js | Start HTTP server, handle shutdown signals |
| backend/src/app.js | Routes, headers, logging and consistent errors |
| backend/src/config.js | Read and validate environment settings |
| backend/src/db.js | PostgreSQL connection pool |
| backend/src/repository.js | SQL queries and database operations |
| backend/src/validation.js | Validate products, IDs and query parameters |
| backend/src/migrate.js | Apply new SQL migration files once |
| backend/src/seed.js | Insert optional sample products |
| backend/migrations/001_products.sql | Products table and constraints |
| frontend/src/main.jsx | Form events, fetch calls, list rendering and pagination |
| frontend/src/styles.css | Responsive visual layout |
| frontend/nginx.conf | Static files and API reverse proxy |

Express 5 forwards rejected promises from async route handlers to error middleware. Input validation and database constraints work together. React renders product data as text, without using raw HTML injection. Server logs record method, path, status, duration and generated request ID without logging request bodies or database passwords.

## Database schema

The `products` table stores one row per product. `sku` has a unique constraint. Quantity and price have nonnegative integer constraints. Category has an index for exact filtering. IDs use a sequence and may contain gaps.

The `schema_migrations` table records successfully applied migration filenames. The migration runner sorts SQL filenames, takes a PostgreSQL advisory lock, and executes each unapplied migration in a transaction. It records the filename only after the SQL succeeds. Existing migration files must not be edited after application: the runner tracks names, not content hashes.

`updated_at` is refreshed by repository update queries; there is no database trigger. A manual SQL UPDATE must set updated_at explicitly if that timestamp should change.

## Money and stock

Amounts use integer minor units. NGN 18,500.00 is stored as 1,850,000 kobo. The frontend parses decimal text and the API accepts integers only. This avoids storing price values in binary floating-point database columns.

Stock changes replace the recorded quantity. They do not record who made the change or a movement history. Concurrent edits use last-write-wins behavior. A future order/reservation system would need transactions, stock movement records and a concurrency policy.

## Startup sequence

The database must become healthy before migrations run. The API waits for successful migration completion, and Nginx waits for API readiness. The API readiness probe queries the products table, checking both connectivity and basic schema availability.

Compose startup conditions are not ongoing dependency supervision. If PostgreSQL later fails, requests can fail and readiness returns 503. Connection-pool recovery allows later requests to reconnect after PostgreSQL recovers. Docker does not restart a service just because a healthcheck is unhealthy; restart policies act on process exit.

## Security scope

The API and Nginx images run as non-root users. Database and API inputs stay server-side. SQL values are parameterized; dynamic update column names come from a fixed allowlist. JSON bodies are limited to 32 KB. Helmet applies API response headers, and Nginx applies a frontend Content Security Policy. Host-facing ports are bound to localhost.

There is no authentication, authorization, TLS termination, audit ledger or rate limiting. The example database login is an initialization superuser. Floating image tags allow updates but do not provide immutable deployment identity. These must be addressed for an internet-facing deployment.
