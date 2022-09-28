import pytest
from rest_framework.test import APIClient

from users.models import User

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


def test_follow_page(user, page2):
    client.force_authenticate(user)
    response = client.get(reverse('follow_page', kwargs={"id": 2}))
    assert response.status_code == 200
    assert page2.followers.first().username == user.username
    assert response.data.get('subscription') == 'done'


def test_accept_all_private_users(user, page):
    client.force_authenticate(user)
    response = client.put(reverse('accept_all_followers', kwargs={"pk": 1}))
    assert response.status_code == 200
    assert page.followers.first().username == user.username
    assert response.data.get('accepted') == 'users were successfully accepted'


def test_accept_not_private_all_users(user, page2):
    client.force_authenticate(user)
    response = client.put(reverse('accept_all_followers', kwargs={"pk": 2}))
    assert response.status_code == 200
    assert response.data.get('accepted') == 'page is not private!'


def test_accept_follower_for_private_page(user, page):
    client.force_authenticate(user)
    response = client.put(reverse('accept_particular_follower', kwargs={"pk": 1, "id": 1}))
    assert response.status_code == 200
    assert page.followers.first().username == user.username
    assert response.data.get('accepted') == 'user was successfully accepted'
