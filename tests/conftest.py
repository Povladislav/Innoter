import pytest
from users.models import User

from blog.models import Page, Post, Tag


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="harry_potter",
        email="nu2@gmail.com",
        password="user2",
        role=User.Roles.ADMIN
    )

    return user


@pytest.fixture
def tag():
    tag = Tag.objects.create(name="TestTag")
    return tag


@pytest.fixture
def page(user, tag):
    page = Page(
        id=1,
        name="TestPage",
        description="TestDescription",
        owner=user
    )
    page.save()
    page.tags.add(tag)
    return page


@pytest.fixture
def post(page):
    post = Post.objects.create(
        id=1,
        page=page,
        content="TestContet"
    )
    return post
