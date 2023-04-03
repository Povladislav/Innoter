import json

import pytest
from rest_framework.test import APIClient

from django.urls import reverse

client = APIClient()
pytestmark = pytest.mark.django_db


def test_list_of_tag(user, tag):
    client.force_authenticate(user)
    response = client.get(reverse("tag"))
    assert response.data[0]["name"] == tag.name
    assert response.status_code == 200


def test_update_tag(user, tag):
    client.force_authenticate(user)
    response = client.put(reverse("tag_id", kwargs={"id": 1}), data={"name": "2132"})
    assert response.status_code == 200
    assert response.data['name'] == "2132"


def test_post_tag(user):
    client.force_authenticate(user)
    response = client.post(reverse("tag_id", kwargs={"id": 2}), data={"name": "tesf"})
    assert response.status_code == 201
    assert response.data['name'] == "tesf"


def test_delete_tag(user, tag):
    client.force_authenticate(user)
    response = client.delete(reverse("tag_id", kwargs={"id": 1}))
    assert response.status_code == 204


def test_retrieve_tag(user, tag):
    client.force_authenticate(user)
    response = client.get(reverse("tag_id", kwargs={"id": 1}))
    assert response.status_code == 200
    assert response.data["name"] == tag.name
