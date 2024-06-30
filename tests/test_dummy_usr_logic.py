import pytest
from utils.utils import request_get_async_client, request_post_client, export_json_data, resource, get_token
from playground_project.tests.enums.enums import GlobalErrors
from models.dummy_user_models.login.api_login_dummy_user_schema import user_info_class
from models.dummy_user_models.user_info.api_user_info_schema import user_info_response_class
from models.dummy_user_models.login.json_schema import json_user_login_schema
from models.dummy_user_models.user_info.json_user_info_schema import json_user_info_schema
from apischema import serialize
from jsonschema import validate

# python3 -m pytest -s -v test_dummy_usr_logic.py



DUMMY_LOGIN = 'https://dummyjson.com/user/login'
DUMMY_USER = 'https://dummyjson.com/auth/me'
OK = 200
USERNAME = "jacksone"
PASS = "jacksonepass"


# @pytest.mark.skip('')
@pytest.mark.asyncio
async def test_login_fake_user_endpoint():
    """ARRANGE"""
    data = {
        "username": USERNAME,
        "password": PASS
    }
    """ACT"""
    res = await request_post_client(DUMMY_LOGIN, data, '')
    """ASSERT"""
    assert res.status_code == OK, GlobalErrors.WRONG_STATUS_CODE.value
    assert serialize(user_info_class, resource(user_info_class, res.json())) == res.json()
    validate(json_user_login_schema, res.json())
    export_json_data('token', {"authorization": f"Bearer {res.json()['token']}"})
    # print(res.json()['firstName'])
    pass


@pytest.mark.asyncio
async def test_get_current_user():
    """ARRANGE"""
    token = get_token()
    """ACT"""
    res = await request_get_async_client(DUMMY_USER, '', token)
    """ASSERT"""
    assert res.status_code == OK, GlobalErrors.WRONG_STATUS_CODE.value
    assert serialize(user_info_response_class, resource(user_info_response_class, res.json())) == res.json()
    validate(json_user_info_schema, res.json())
