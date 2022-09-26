import pytest

from rest_framework.test import APIClient

client = APIClient()
pytestmark = pytest.mark.django_db


def test_register_user():
    payload = dict(
        first_name="Harry",
        second_name="Potter",
        username="harry_potter",
        email="nu2@gmail.com",
        password="user2"
    )

    response = client.post("/accounts/register/", payload)

    data = response.data

    assert data["username"] == payload["username"]


def test_login_user(user):
    response = client.post("/accounts/login/", dict(email="nu2@gmail.com", password="user2"))
    assert response.status_code == 200


def test_login_user_fail():
    response = client.post("/accounts/login/", dict(email="nu2@gmail.com", password="ssdb21"))
    assert response.status_code == 403


def test_get_users(user):
    client.force_authenticate(user)
    response = client.get("/accounts/users/")
    assert response.status_code == 200


def test_logout(user):
    client.force_authenticate(user)
    response = client.post("/accounts/logout/")
    assert response.status_code == 200
    assert response.data['message'] == "success"
