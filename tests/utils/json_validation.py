import json
from enums.enams import GlobalErrors


async def playground_validate(json_dict):
    obj = json_dict
    key = 'answer'
    assert obj[key], GlobalErrors.WRONG_JSON_KEY.value

