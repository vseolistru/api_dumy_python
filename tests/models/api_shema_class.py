from apischema.json_schema import deserialization_schema
from dataclasses import dataclass, field
from apischema import deserialize


@dataclass
class Products:
    id: int
    title: str
    price: float
    quantity: int
    total: float
    discountPercentage: float
    discountedTotal: float
    thumbnail: str


@dataclass
class Cart:
    id: int
    total: float
    discountedTotal: float
    userId: int
    totalProducts: int
    totalQuantity: int
    products: list[Products] = field(default_factory=set)

@dataclass
class Carts:
    carts: list[Cart]
    total: int
    skip: int
    limit: int

def resource(data):
    result = deserialize(Carts, data)
    return result

carts = Carts

# print(deserialization_schema(Carts))