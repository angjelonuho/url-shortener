from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_shorten_endpoint_successful():
    response = client.post("/shorten", json={"url": "http://example.com",  "shortcode": ""})
    assert response.status_code == 201
    assert "shortcode" in response.json()

def test_shorten_endpoint_with_invalid_shortcode_format(setup_database):
    response = client.post("/shorten", json={"url": "http://example.com", "shortcode": "invalid_shortcode!@#$"})
    assert response.status_code == 412
    assert response.json()["detail"] == "The provided shortcode is invalid"


def test_shorten_endpoint_with_existing_shortcode(setup_database):
    response = client.post("/shorten", json={"url": "http://example.com", "shortcode": "test_shortcode"})
    assert response.status_code == 412
    assert response.json()["detail"] == "Shortcode already in use"

def test_shorten_endpoint_with_empty_url():
    response = client.post("/shorten", json={"url": "", "shortcode": "test"})
    assert response.status_code == 400
    assert response.json()["detail"] == "Url not present"

def test_shorten_endpoint_with_missing_url():
    response = client.post("/shorten", json={"shortcode": "test"})
    assert response.status_code == 422