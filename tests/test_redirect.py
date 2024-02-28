from fastapi.testclient import TestClient
from main import app
from .conftest import setup_database

client = TestClient(app)

def test_redirect_endpoint_with_valid_shortcode(setup_database):
    response = client.get("/test_shortcode", allow_redirects=False)
    assert response.status_code == 302
    assert response.headers["Location"] == "http://example.com"

def test_redirect_endpoint_with_missing_shortcode(setup_database):
    response = client.get("/invalid_shortcode", allow_redirects=False)
    assert response.status_code == 404
    assert response.json()["detail"] == "Shortcode not found"

def test_redirect_endpoint_with_invalid_shortcode_format(setup_database):
    response = client.get("/invalid_shortcode!@#$", allow_redirects=False)
    assert response.status_code == 404
    assert response.json()["detail"] == "Shortcode not found"

