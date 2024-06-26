import json
from apischema.json_schema import deserialization_schema
from dataclasses import dataclass, field
from apischema import deserialize, serialize


@dataclass
class Crypto:
    coin: str
    wallet: str
    network: str


@dataclass
class Coordinates:
    lat: float
    lng: float


@dataclass
class Address:
    address: str
    city: str
    state: str
    stateCode: str
    postalCode: str
    country: str
    coordinates: Coordinates


@dataclass
class Company:
    department: str
    name: str
    title: str
    address: Address


@dataclass
class Bank:
    cardExpire: str
    cardNumber: str
    cardType: str
    currency: str
    iban: str


@dataclass
class Hair:
    color: str
    type: str


@dataclass
class UserInfo:
    id: int
    firstName: str
    lastName: str
    maidenName: str
    age: int
    gender: str
    email: str
    phone: str
    username: str
    password: str
    birthDate: str
    image: str
    bloodGroup: str
    height: float
    weight: float
    eyeColor: str
    ip: str
    macAddress: str
    university: str
    ein: str
    ssn: str
    userAgent: str
    role: str
    crypto: Crypto
    company: Company
    bank: Bank
    address: Address
    hair: Hair


user_info_response_class = UserInfo