import pytest
from rest_framework.test import APIClient

from users.models import User

from blog.models import Page, Post

from django.urls import reverse

client = APIClient()
pytestmark = pytest.mark.django_db


def test_ban_user(user):
    client.force_authenticate(user)
    response = client.post(reverse("ban_user", kwargs={"id": 1}))
    assert response.status_code == 200
    assert User.objects.get(id=1).is_blocked == True
    response = client.post(reverse("ban_user", kwargs={"id": 1}), {"bantime": 10}, format='json')
    assert response.status_code == 200
    assert User.objects.get(id=1).is_blocked == True


def test_search(user):
    client.force_authenticate(user)
    name = user.username
    response = client.post(reverse("search"), {"username": "harry_potter"}, format='json')
    assert response.status_code == 200
    assert response.data["user"]["username"] == name


def test_show_liked(user, page, post, tag):
    client.force_authenticate(user)
    response = client.post(reverse('like_post', kwargs={"id": 1}))
    assert response.status_code == 200
    assert User.objects.get(likes__isnull=False) == user


def test_show_unliked(user, page, post, tag):
    client.force_authenticate(user)
    response = client.post(reverse('unlike_post', kwargs={"id": 1}))
    assert response.status_code == 200
    assert User.objects.get(likes__isnull=True) == user


def test_show_news(user, post):
    client.force_authenticate(user)
    response = client.get(reverse('show_news_post'))
    assert response.status_code == 200
    assert response.data[0]['content'] == post.content
