import json
from apischema.json_schema import deserialization_schema
from dataclasses import dataclass, field
from apischema import deserialize, serialize


@dataclass
class UserInfo:
    id: int
    username: str
    email: str
    firstName: str
    lastName: str
    gender: str
    image: str
    token: str
    refreshToken: str


def resource(data):
    result = deserialize(UserInfo, data)
    return result


user_info_class = UserInfo
