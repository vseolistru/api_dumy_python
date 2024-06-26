json_user_info_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "number"
        },
        "firstName": {
            "type": "string"
        },
        "lastName": {
            "type": "string"
        },
        "maidenName": {
            "type": "string"
        },
        "age": {
            "type": "number"
        },
        "gender": {
            "type": "string"
        },
        "email": {
            "type": "string"
        },
        "phone": {
            "type": "string"
        },
        "username": {
            "type": "string"
        },
        "password": {
            "type": "string"
        },
        "birthDate": {
            "type": "string"
        },
        "image": {
            "type": "string"
        },
        "bloodGroup": {
            "type": "string"
        },
        "height": {
            "type": "number"
        },
        "weight": {
            "type": "number"
        },
        "eyeColor": {
            "type": "string"
        },
        "hair": {
            "type": "object",
            "properties": {
                "color": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                }
            },
            "required": [
                "color",
                "type"
            ],
            "additionalProperties": False
        },
        "ip": {
            "type": "string"
        },
        "address": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string"
                },
                "city": {
                    "type": "string"
                },
                "state": {
                    "type": "string"
                },
                "stateCode": {
                    "type": "string"
                },
                "postalCode": {
                    "type": "string"
                },
                "coordinates": {
                    "type": "object",
                    "properties": {
                        "lat": {
                            "type": "number"
                        },
                        "lng": {
                            "type": "number"
                        }
                    },
                    "required": [
                        "lat",
                        "lng"
                    ],
                    "additionalProperties": False
                },
                "country": {
                    "type": "string"
                }
            },
            "required": [
                "address",
                "city",
                "state",
                "stateCode",
                "postalCode",
                "coordinates",
                "country"
            ],
            "additionalProperties": False
        },
        "macAddress": {
            "type": "string"
        },
        "university": {
            "type": "string"
        },
        "bank": {
            "type": "object",
            "properties": {
                "cardExpire": {
                    "type": "string"
                },
                "cardNumber": {
                    "type": "string"
                },
                "cardType": {
                    "type": "string"
                },
                "currency": {
                    "type": "string"
                },
                "iban": {
                    "type": "string"
                }
            },
            "required": [
                "cardExpire",
                "cardNumber",
                "cardType",
                "currency",
                "iban"
            ],
            "additionalProperties": False
        },
        "company": {
            "type": "object",
            "properties": {
                "department": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "title": {
                    "type": "string"
                },
                "address": {
                    "type": "object",
                    "properties": {
                        "address": {
                            "type": "string"
                        },
                        "city": {
                            "type": "string"
                        },
                        "state": {
                            "type": "string"
                        },
                        "stateCode": {
                            "type": "string"
                        },
                        "postalCode": {
                            "type": "string"
                        },
                        "coordinates": {
                            "type": "object",
                            "properties": {
                                "lat": {
                                    "type": "number"
                                },
                                "lng": {
                                    "type": "number"
                                }
                            },
                            "required": [
                                "lat",
                                "lng"
                            ],
                            "additionalProperties": False
                        },
                        "country": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "address",
                        "city",
                        "state",
                        "stateCode",
                        "postalCode",
                        "coordinates",
                        "country"
                    ],
                    "additionalProperties": False
                }
            },
            "required": [
                "department",
                "name",
                "title",
                "address"
            ]
        },
        "ein": {
            "type": "string"
        },
        "ssn": {
            "type": "string"
        },
        "userAgent": {
            "type": "string"
        },
        "crypto": {
            "type": "object",
            "properties": {
                "coin": {
                    "type": "string"
                },
                "wallet": {
                    "type": "string"
                },
                "network": {
                    "type": "string"
                }
            },
            "required": [
                "coin",
                "wallet",
                "network"
            ],
            "additionalProperties": False
        },
        "role": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "firstName",
        "lastName",
        "maidenName",
        "age",
        "gender",
        "email",
        "phone",
        "username",
        "password",
        "birthDate",
        "image",
        "bloodGroup",
        "height",
        "weight",
        "eyeColor",
        "hair",
        "ip",
        "address",
        "macAddress",
        "university",
        "bank",
        "company",
        "ein",
        "ssn",
        "userAgent",
        "crypto",
        "role"
    ],
    "additionalProperties": False
}
