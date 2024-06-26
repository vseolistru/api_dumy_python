

json_user_login_schema = {
  "type": "object",
  "properties": {
    "id": {
      "type": "number"
    },
    "username": {
      "type": "string"
    },
    "email": {
      "type": "string"
    },
    "firstName": {
      "type": "string"
    },
    "lastName": {
      "type": "string"
    },
    "gender": {
      "type": "string"
    },
    "image": {
      "type": "string"
    },
    "token": {
      "type": "string"
    },
    "refreshToken": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "username",
    "email",
    "firstName",
    "lastName",
    "gender",
    "image",
    "token",
    "refreshToken"
  ],
    "additionalProperties": False,
}