from httpx import AsyncClient
import json
from apischema import deserialize


async def request_get_async_client(*args):
    """
    url, json, headers
    :param args:
    :return: response
    """
    async with AsyncClient() as client:
        result = await client.get(url=args[0], params=args[1], headers=args[2], follow_redirects=True)
    return result


async def request_post_client(*args):
    """
    url, json, headers
    :param args:
    :return: response
    """
    async with AsyncClient() as client:
        result = await client.post(url=args[0], json=args[1], headers=args[2])
        assert result.status_code == 200
    return result


def export_json_data(file_name, data):
    with open(f'./test_data/{file_name}_data.json', 'w') as f:
        json.dump(data, f)


def resource(class_schema, data):
    result = deserialize(class_schema, data)
    return result


def get_token() -> dict:
    with open('./test_data/token_data.json') as f:
        token = json.load(f)
    return token
