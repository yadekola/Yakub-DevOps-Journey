# Multi-stage build for the StockPulse API.
# Stage 1 compiles the dependency wheels (needs a compiler for psycopg2).
# Stage 2 is the runtime and contains no compiler and no build tooling.
# Compare the two with `docker images` - that gap is the point of multi-stage.

# ---------- Stage 1: build ----------
FROM python:3.12-slim AS build
WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# ---------- Stage 2: runtime ----------
FROM python:3.12-slim
WORKDIR /app

# Run as a non-root user. A container running as root is a container where a code
# execution bug becomes a host problem.
RUN groupadd -r app && useradd -r -g app app \
    && apt-get update && apt-get install -y --no-install-recommends libpq5 curl \
    && rm -rf /var/lib/apt/lists/*

COPY --from=build /wheels /wheels
COPY requirements.txt .
RUN pip install --no-cache-dir --no-index --find-links=/wheels -r requirements.txt \
    && rm -rf /wheels

COPY app ./app
USER app

ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
EXPOSE 8000

# Uses the LIVENESS endpoint, which does not touch the database - see routes/health.py
HEALTHCHECK --interval=15s --timeout=3s --start-period=10s --retries=3 \
  CMD curl -fsS http://localhost:8000/healthz || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
