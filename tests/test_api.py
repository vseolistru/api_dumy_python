import pytest
from utils.utils import request_get_async_client, request_post_client
from utils.json_validation import playground_validate
from playground_project.tests.enums.enums import GlobalErrors
from models.api_shema_class import resource, carts
from models.schema import json_carts_dummy_schema
from apischema import serialize
from jsonschema import validate

pytest_plugins = ('pytest_asyncio',)

URL = 'https://playground.learnqa.ru/api/'
DUMMY = 'http://dummyjson.com/users'
DUMMY_LOGIN = 'https://dummyjson.com/user/login'
SINGLE_USER = 'http://dummyjson.com/users/1'
FAKE_STORE = 'https://dummyjson.com/products'
DUMMY_CARTS = 'https://dummyjson.com/carts'
OK = 200



@pytest.mark.skip('')
@pytest.mark.asyncio
async def test_first_endpoint():
    data = {
        "name":"michaelw"
    }
    res = await request_get_async_client(URL+'hello', data, '')
    # res = requests.get(DUMMY)
    assert res.status_code == 200, GlobalErrors.WRONG_STATUS_CODE.value
    # export_json_data('products', res.json())
    print(res.json())
    await playground_validate(res.json())

@pytest.mark.skip('')
@pytest.mark.asyncio
async def test_get_fake_users_endpoint():
    res = await request_get_async_client(DUMMY, '', '')
    # res = requests.get(DUMMY)
    assert res.status_code == 200, GlobalErrors.WRONG_STATUS_CODE.value
    # export_json_data('products', res.json())
    print(res.history[0].url)
    print(res.url)


@pytest.mark.skip('')
@pytest.mark.asyncio
async def test_check_type_playground_endpoint():
    data = {
        "params":"value1"
    }
    res = await request_get_async_client(URL+'check_type', data, '')
    assert res.status_code == 200, GlobalErrors.WRONG_STATUS_CODE.value
    print(res.text)


@pytest.mark.skip('')
@pytest.mark.asyncio
async def test_login_fake_user_endpoint():
    data = {
        "username": "michaelw",
        "password": "michaelwpass"
    }
    res = await request_post_client(DUMMY_LOGIN, data, '')
    assert res.status_code == OK, GlobalErrors.WRONG_STATUS_CODE.value
    print(res.json())


@pytest.mark.asyncio
async def test_get_dummy_carts_endpoint():
    """ACT"""
    res = await request_get_async_client(DUMMY_CARTS, '', '')
    """ASSERT"""
    assert res.status_code == 200, GlobalErrors.WRONG_STATUS_CODE.value
    assert serialize(carts, resource(res.json())) == res.json()
    validate(res.json(), json_carts_dummy_schema)