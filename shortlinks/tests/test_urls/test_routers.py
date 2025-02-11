from unittest.mock import patch

from fastapi.testclient import TestClient

from shortlinks.database import SessionLocal
from shortlinks.main import app
from shortlinks.models import URL

client = TestClient(app)
db = SessionLocal()


def test_create_url():
    with patch("shortlinks.urls.services.create_random_key") as random_key:
        random_key.return_value = "AgH695a"
        response = client.put(
            url="/url/", json={"target_url": "https://fastapi.tiangolo.com/"}
        )
    assert response.status_code == 201

    urls_count = (
        db.query(URL).filter(URL.target_url == "https://fastapi.tiangolo.com/").count()
    )
    assert urls_count == 1


def test_get_existing_url():
    with patch("shortlinks.urls.services.create_random_key") as random_key:
        random_key.return_value = "AgH695a"
        response = client.put(
            "/url/", json={"target_url": "https://fastapi.tiangolo.com/"}
        )
    assert response.status_code == 200

    urls_count = (
        db.query(URL).filter(URL.target_url == "https://fastapi.tiangolo.com/").count()
    )
    assert urls_count == 1


def test_create_with_invalid_url():
    response = client.put("/url/", json={"target_url": "fastapi.tiangolo.com/"})
    assert response.status_code == 400


def test_forward():
    response = client.get("/url/AgH695a")
    assert response.status_code == 200


def test_forward_with_unexisting_key():
    response = client.get("/url/123ert")
    assert response.status_code == 404
    print(response.json())
    assert response.json() == {"detail": "Provided URL is invalid"}
