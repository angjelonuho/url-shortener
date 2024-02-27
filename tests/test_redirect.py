from fastapi.testclient import TestClient
from ..app.redirect import router

client = TestClient(router)

def test_redirect_to_url():
    response = client.get("/abc123")
    assert response.status_code == 302