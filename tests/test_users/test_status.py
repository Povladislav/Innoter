import pytest
from rest_framework.test import APIClient

from users.models import User

from django.urls import reverse

client = APIClient()
pytestmark = pytest.mark.django_db


def test_ban_user(user):
    user2 = User.objects.create_user(pk=1, username="testUser", email="tu@gmail.com", password="test",
                                     role=User.Roles.ADMIN)
    client.force_authenticate(user2)
    response = client.post(reverse("ban_user", kwargs={"id": 1}))
    assert response.status_code == 200
    assert User.objects.get(pk=1).is_blocked == True
    response = client.post(reverse("ban_user", kwargs={"id": 1}), {"bantime": 10}, format='json')
    assert response.status_code == 200
    assert User.objects.get(pk=1).is_blocked == True
