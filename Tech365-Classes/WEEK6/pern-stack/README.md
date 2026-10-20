# Tech365 Inventory: React + Node.js/Express + PostgreSQL

A runnable inventory application using **Node.js, Express, PostgreSQL, and a React frontend . The React frontend uses Vite to build static assets. The Node.js/Express backend provides the REST API. This repository contains application source code and technical documentation

## Features

- Create, view, edit and delete products.
- Track SKU, name, category, price and available quantity.
- Search by name or SKU, filter by category, and paginate results.
- Validate input and reject duplicate SKUs.
- Store records in a persistent PostgreSQL database.
- Separate liveness and database/schema readiness endpoints.
- Versioned SQL migrations and optional repeatable sample data.
- OpenAPI 3.0 specification and automated API tests.

You can access the frontend from **http://localhost:5173**. The backend API is **http://localhost:3000/api**. 


## Components and ports

| Service | Technology | Container port | Host address | Internal address |
|---|---|---|---|---|
| web | React, Vite build  | 5173 | http://localhost:5173 | web:5173 |
| api | Node.js and Express | 3000 | http://localhost:3000 | api:3000 |
| db | PostgreSQL | 5432 | Not published by default | db:5432 |
| migrate | Node.js SQL migration runner | None | None | Connects to db:5432 |

The browser requests `/api/products` from the same origin as the page. Frontend forwards that request to `api:3000`. The API queries `db:5432`. 

## Version reference

| Component | Declared version/tag | Location |
|---|---|---|
| Application | 1.0.0 | backend/package.json |
| Node.js | 24 |  |
| Express | 5.1.0 | backend/package.json |
| PostgreSQL driver, pg | 8.16.3 | backend/package.json |
| Helmet | 8.1.0 | backend/package.json |
| pg-mem, tests only | 3.0.5 | backend/package.json |
| PostgreSQL | 17 |  |
| React / React DOM | 19.2.0 | frontend/package.json |
| Vite | 6.4.1 | frontend/package.json |

These are selected versions, not a claim that every dependency is the latest available. Each package-lock.json records its resolved dependency tree. The backend image uses `npm ci --omit=dev`; the frontend build stage uses `npm ci` so Vite is available. Image tags can receive patch updates; they are not immutable digests. See docs/OPERATIONS.md for actual runtime version commands. Review dependency and image updates before any deployment.

## Repository structure

```text
tech365-react-express/
  .env.example
  backend/
    package.json
    package-lock.json
    openapi.json
    migrations/001_products.sql
    src/
      app.js
      config.js
      db.js
      repository.js
      validation.js
      server.js
      migrate.js
      seed.js
    scripts/smoke.js
    test/api.test.js
  frontend/
    index.html
    src/styles.css
    src/main.jsx
    src/api.js
    package.json
    package-lock.json
    vite.config.js
  docs/
    API.md
    CONFIGURATION.md
    ARCHITECTURE.md
    VALIDATION.md
```

## Documentation

- [API reference](docs/API.md): every endpoint, field, status code and request example.
- [Configuration](docs/CONFIGURATION.md): environment variables and local Node.js startup.
- [Operations](docs/OPERATIONS.md): logs, development mode, migrations, backups and troubleshooting.
- [Architecture](docs/ARCHITECTURE.md): request flow, source file responsibilities and design choices.
- [Validation](docs/VALIDATION.md): completed checks and remaining runtime checks.
- [OpenAPI specification](backend/openapi.json): import into Postman or an OpenAPI-compatible client. It is also served at http://localhost:8081/api/openapi.json. The file is the specification, not an embedded Swagger UI.


## Application scope

Prices are in Nigerian naira (NGN). API amounts use integer kobo: `1850000` means NGN 18,500.00. The UI converts naira input to kobo. Quantity is a nonnegative integer. This is a product catalogue with editable stock counts, not an accounting, purchasing or order fulfilment system. Edits use last-write-wins behavior; there is no stock movement ledger or concurrent edit conflict detection.

Before exposing it publicly, add authentication, authorization, HTTPS, appropriate rate limits, a least-privilege database role, managed secrets, monitoring and tested backups. The default PostgreSQL initialization user is a superuser. These omitted features are documented boundaries, not claims of production readiness.
