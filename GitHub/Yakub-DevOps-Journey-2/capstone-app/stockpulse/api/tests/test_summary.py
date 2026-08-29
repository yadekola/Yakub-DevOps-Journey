def test_summary_totals(client):
    client.post("/api/items", json={"sku": "S-1", "name": "One", "category": "a",
                                    "quantity": 10, "reorder_level": 2})
    client.post("/api/items", json={"sku": "S-2", "name": "Two", "category": "b",
                                    "quantity": 1, "reorder_level": 5})
    s = client.get("/api/summary").json()
    assert s["total_items"] == 2
    assert s["total_units"] == 11
    assert s["low_stock_count"] == 1
    assert s["categories"] == {"a": 1, "b": 1}


def test_summary_works_without_redis(client):
    """No Redis configured in tests. The app must still answer, just uncached."""
    s = client.get("/api/summary").json()
    assert s["cached"] is False
