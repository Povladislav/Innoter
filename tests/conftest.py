import pytest
from users.models import User

from blog.models import Page, Post, Tag


@pytest.fixture
def user():
    user = User.objects.create_user(
        id=1,
        username="harry_potter",
        email="nu2@gmail.com",
        password="user2",
        role=User.Roles.ADMIN
    )

    return user


@pytest.fixture
def tag():
    tag = Tag.objects.create(pk=1, name="TestTag")
    return tag


@pytest.fixture
def page(user, tag):
    page = Page(
        id=1,
        name="TestPage",
        description="TestDescription",
        owner=user,
        is_private=True
    )
    page.save()
    page.tags.add(tag)
    page.follow_requests.add(user)
    return page


@pytest.fixture
def page2(user, tag):
    page2 = Page(
        id=2,
        name="TestPage",
        description="TestDescription",
        owner=user,
    )
    page2.save()
    page2.tags.add(tag)
    return page2


@pytest.fixture
def post(page):
    post = Post.objects.create(
        id=1,
        page=page,
        content="TestContet"
    )
    return post
