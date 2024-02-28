from fastapi.testclient import TestClient
from main import app
from .conftest import setup_database

client = TestClient(app)

def test_stats_endpoint(setup_database):
    response = client.get("/test_shortcode/stats")
    assert response.status_code == 200
    assert "created" in response.json()
    assert "lastRedirect" in response.json()
    assert "redirectCount" in response.json()

def test_get_shortcode_stats_not_found(setup_database):
    response = client.get("/non_existent_shortcode/stats")
    assert response.status_code == 404
    assert response.json()["detail"] == "Shortcode not found"