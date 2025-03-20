from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_greeting():
    response = client.get("/greeting")
    assert response.status_code == 200
    assert "Hello" in response.text

def test_redirect_root():
    response = client.get("/", allow_redirects=False)
    assert response.status_code in (302, 307)
