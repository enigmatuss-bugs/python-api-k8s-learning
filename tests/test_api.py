import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200


def test_home(client):
    response = client.get("/")

    assert response.status_code == 200
    assert response.is_json


def test_protected_without_key(client):
    response = client.get("/protected")

    assert response.status_code in (401, 403)
