import pytest
from users.models import User


@pytest.fixture
def user():
    user = User.objects.create_user(
        username="harry_potter",
        email="nu2@gmail.com",
        password="user2"
    )

    return user
