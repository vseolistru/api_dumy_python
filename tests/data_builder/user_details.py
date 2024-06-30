import json
# from enums import Currency, CardType
from faker import Faker

fake = Faker()
ADDRESS = fake.street_address()
CITY = fake.city()
STATE_NAME = fake.state()
POSTAL_CODE = fake.postalcode()
COORDS_LAT = fake.latitude()
COORDS_LNG = fake.longitude()
COUNTRY = fake.country()
CARD_EXPIRE = fake.credit_card_expire()
CARD_NUMBER = fake.credit_card_number()
CARD_PROVIDER = fake.credit_card_provider()
CARD_CURRENCY = fake.currency_code()


class UserDetails:
    def __init__(self):
        self._result = {
            "address": {
            },
            "bank": {
            }
        }

    def set_address(self, address=ADDRESS):
        self._result['address']['address'] = address
        return self

    def set_city(self, city=CITY):
        self._result['address']['city'] = city
        return self

    def set_state_name(self, state_name=STATE_NAME):
        self._result['address']['state'] = state_name
        return self

    def set_postalcode(self, postal_code=POSTAL_CODE):
        self._result['address']['postalCode'] = postal_code
        return self

    def set_coords(self, lat=COORDS_LAT, lng=COORDS_LNG):
        data = {
            "lat": float(lat),
            "lng": float(lng)
        }
        self._result['address']['coordinates'] = data
        return self

    def set_country(self, country=COUNTRY):
        self._result['address']['country'] = country
        return self

    def set_card_expire(self, card_expire=CARD_EXPIRE):
        self._result['bank']['cardExpire'] = card_expire
        return self

    def set_card_number(self, card_number=CARD_NUMBER):
        self._result['bank']['cardNumber'] = card_number
        return self

    def set_card_type(self, card_provider=CARD_PROVIDER):
        self._result['bank']['cardType'] = card_provider
        return self

    def set_currency(self, card_currency=CARD_CURRENCY):
        self._result['bank']['currency'] = card_currency
        return self

    def mount(self):
        self.set_address()
        self.set_city()
        self.set_state_name()
        self.set_postalcode()
        self.set_coords()
        self.set_country()
        self.set_card_expire()
        self.set_card_number()
        self.set_card_type()
        self.set_currency()
        return self

    def build(self):
        return self._result

#
# user_details = UserDetails().mount().build()
# print(user_details)

# with open('test_data.json', 'w') as f:
#     json.dump(user_details, f)



