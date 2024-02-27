from fastapi.testclient import TestClient
from ..app.shorten import router

client = TestClient(router)

def test_shorten_url():
    response = client.post("/shorten", json={"url": "https://www.example.com"})
    assert response.status_code == 201
    assert "shortcode" in response.json()