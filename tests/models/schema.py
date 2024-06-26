


json_carts_dummy_schema = {
  "type": "object",
  "properties": {
    "carts": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "number"
          },
          "products": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "id": {
                  "type": "number"
                },
                "title": {
                  "type": "string"
                },
                "price": {
                  "type": "number"
                },
                "quantity": {
                  "type": "number"
                },
                "total": {
                  "type": "number"
                },
                "discountPercentage": {
                  "type": "number"
                },
                "discountedTotal": {
                  "type": "number"
                },
                "thumbnail": {
                  "type": "string"
                }
              },
              "required": [
                "id",
                "title",
                "price",
                "quantity",
                "total",
                "discountPercentage",
                "discountedTotal",
                "thumbnail"
              ],
              "additionalProperties": False
            }
          },
          "total": {
            "type": "number"
          },
          "discountedTotal": {
            "type": "number"
          },
          "userId": {
            "type": "number"
          },
          "totalProducts": {
            "type": "number"
          },
          "totalQuantity": {
            "type": "number"
          }
        },
        "required": [
          "id",
          "products",
          "total",
          "discountedTotal",
          "userId",
          "totalProducts",
          "totalQuantity"
        ],
        "additionalProperties": False
      }
    },
    "total": {
      "type": "number"
    },
    "skip": {
      "type": "number"
    },
    "limit": {
      "type": "number"
    }
  },
  "required": [
    "carts",
    "total",
    "skip",
    "limit"
  ],
  "additionalProperties": False
}