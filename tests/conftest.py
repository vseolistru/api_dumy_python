import pytest
from httpx import AsyncClient
from data_builder.user_details import UserDetails


@pytest.fixture(scope="session")
def f_hello():
    yield print('\nhello')


@pytest.fixture(scope="session")
def get_data():
    yield UserDetails()
