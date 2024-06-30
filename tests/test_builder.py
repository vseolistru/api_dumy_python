import pytest
from data_builder.enums import Currency, CardType

# python3 -m pytest -s -v test_builder.py
@pytest.mark.skip('')
@pytest.mark.parametrize("currency", [
    Currency.US.value,
    Currency.GB.value,
    Currency.JP.value,
    Currency.GE.value,
])
@pytest.mark.parametrize("card_type", [
    CardType.Visa.value,
    CardType.MC.value,
    CardType.MSC.value,
    CardType.UP.value
])
def test_currency_data_builder(currency, card_type, get_data):
    print(get_data.mount().set_card_type(card_type).set_currency(currency).build())


@pytest.mark.parametrize("del_key", [
    "address",
    "city",
    "state",
    "postalCode"
])
def test_delete_key_data_builder(del_key, get_data):
    user_del_obj = get_data.mount().build()
    del user_del_obj['address'][del_key]
    print(user_del_obj)