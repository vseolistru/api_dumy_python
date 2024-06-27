from enum import Enum


class Countries(Enum):
    US = "United States"
    JP = "Japan"
    GE = "Germany"
    AUS = "Australia"
    FR = "France"
    GB = "England"


class Currency(Enum):
    US = "USD"
    JP = "JPY"
    GE = "EUR"
    AUS = "AUD"
    FR = "EUR"
    GB = "GBP"


class CardType(Enum):
    UP = 'UnionPay'
    MSC = 'Maestro'
    MC = 'Mastercard'
    AE = 'American Express'
    Visa = 'Visa'
