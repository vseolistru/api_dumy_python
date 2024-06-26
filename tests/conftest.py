import pytest
from httpx import AsyncClient




@pytest.fixture(scope="session")
def f_hello():
    yield print('\nhello')