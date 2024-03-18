import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture
def user_data():
    return dict(
        first_name="first_name",
        email="root@mail.ru",
        password="nbuksddnvi43434",
        re_password="nbuksddnvi43434",
    )


@pytest.fixture
def admin_data():
    return dict(
        first_name="first_name",
        email="root@mail.ru",
        role="admin",
        password="nbuksddnvi43434",
        re_password="nbuksddnvi43434",
    )


@pytest.fixture
def fail_admin_data():
    return dict(
        first_name="first_name",
        email="root@mail.ru",
        role="admn",
        password="nbuksddnvi43434",
        re_password="nbuksddnvi43434",
    )
