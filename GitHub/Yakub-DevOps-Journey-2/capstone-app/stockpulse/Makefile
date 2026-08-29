.PHONY: help dev test lint up down logs seed clean

help:
	@echo "make dev    - run the API locally on :8000 with SQLite (no Docker needed)"
	@echo "make test   - run the test suite (no services required)"
	@echo "make up     - build and start the full stack on http://localhost:8080"
	@echo "make down   - stop the stack (data survives)"
	@echo "make clean  - stop the stack AND delete the database volume"
	@echo "make seed   - load sample inventory data"
	@echo "make logs   - follow the API logs"

dev:
	cd api && uvicorn app.main:app --reload --port 8000

test:
	cd api && python -m pytest tests -v

lint:
	cd api && ruff check app tests

up:
	docker compose up -d --build
	@echo "StockPulse is starting. Open http://localhost:8080"

down:
	docker compose down

clean:
	docker compose down -v

seed:
	docker compose run --rm seed

logs:
	docker compose logs -f api
