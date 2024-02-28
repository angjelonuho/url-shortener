from fastapi.testclient import TestClient
from main import app
from .conftest import setup_database

client = TestClient(app)

def test_redirect_endpoint(setup_database):
    response = client.get("/test_shortcode", allow_redirects=False)
    assert response.status_code == 302
    assert response.headers["Location"] == "http://example.com"