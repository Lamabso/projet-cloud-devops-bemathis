import pytest


@pytest.mark.parametrize("path", ["/api/events", "/api/news", "/api/faq"])
def test_api_endpoints_return_items_list(client, path):
    resp = client.get(path)
    assert resp.status_code == 200
    assert resp.is_json

    payload = resp.get_json()
    assert isinstance(payload, dict)
    assert "items" in payload
    assert isinstance(payload["items"], list)


def test_events_items_have_expected_fields_when_present(client):
    resp = client.get("/api/events")
    payload = resp.get_json()

    # Bonus: if there are items, ensure the first has expected fields
    if payload["items"]:
        first = payload["items"][0]
        assert "title" in first
        assert "date" in first
