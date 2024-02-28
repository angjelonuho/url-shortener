from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_shorten_endpoint():
    response = client.post("/shorten", json={"url": "http://example.com",  "shortcode": ""})
    assert response.status_code == 201
    assert "shortcode" in response.json()