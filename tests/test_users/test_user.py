import jwt
import pytest

from rest_framework.test import APIClient

from django.urls import reverse

client = APIClient()
pytestmark = pytest.mark.django_db

import os

secret_key = os.environ.get("secret_key")


def test_register_user():
    payload = dict(
        first_name="Harry",
        second_name="Potter",
        username="harry_potter",
        email="nu2@gmail.com",
        password="user2"
    )

    response = client.post(reverse("register"), payload)

    data = response.data

    assert data["username"] == payload["username"]


def test_register_the_same_user(user):
    payload = dict(
        first_name="Harry",
        second_name="Potter",
        username="harry_potter",
        email="nu2@gmail.com",
        password="user2"
    )
    response = client.post(reverse("register"), payload)

    data = response.data

    assert data["username"] != payload["username"]


def test_login_user(user):
    payload = dict(
        email="nu2@gmail.com", password="user2"
    )

    response = client.post(reverse("login"), payload)
    token = response.data['access_token']
    payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    assert payload['user_id'] == user.pk
    assert response.status_code == 200


def test_login_user_fail():
    payload = dict(
        email="nu2@gmail.com", password="ssdb21"
    )

    response = client.post(reverse("login"), payload)
    assert response.status_code == 403


def test_get_users(user):
    client.force_authenticate(user)
    response = client.get(reverse("users"))
    assert response.status_code == 200


def test_logout(user):
    client.force_authenticate(user)
    response = client.post(reverse("logout"))
    assert response.status_code == 200
    assert response.data['message'] == "success"
