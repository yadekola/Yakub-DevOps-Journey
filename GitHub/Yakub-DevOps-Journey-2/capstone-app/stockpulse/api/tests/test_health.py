def test_liveness_does_not_touch_the_database(client):
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_readiness_reports_database(client):
    r = client.get("/readyz")
    assert r.status_code == 200
    assert r.json()["checks"]["database"] is True


def test_metrics_is_prometheus_text_not_json(client):
    client.get("/api/items")
    r = client.get("/metrics")
    assert r.status_code == 200
    assert "text/plain" in r.headers["content-type"]
    assert "stockpulse_items_total" in r.text
    assert "stockpulse_low_stock_items" in r.text
