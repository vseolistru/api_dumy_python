import json
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

    def set_address(self):
        self._result['address']['address'] = ADDRESS
        return self

    def set_city(self):
        self._result['address']['city'] = CITY
        return self

    def set_state_name(self):
        self._result['address']['state'] = STATE_NAME
        return self

    def set_postalcode(self):
        self._result['address']['postalCode'] = POSTAL_CODE
        return self

    def set_coords(self):
        data = {
            "lat": float(COORDS_LAT),
            "lng": float(COORDS_LNG)
        }
        self._result['address']['coordinates'] = data
        return self

    def set_country(self):
        self._result['address']['country'] = COUNTRY
        return self

    def set_card_expire(self):
        self._result['bank']['cardExpire'] = CARD_EXPIRE
        return self

    def set_card_number(self):
        self._result['bank']['cardNumber'] = CARD_NUMBER
        return self

    def set_card_type(self):
        self._result['bank']['cardType'] = CARD_PROVIDER
        return self

    def set_currency(self):
        self._result['bank']['currency'] = CARD_CURRENCY
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


user_details = UserDetails().mount().build()

print(user_details)

# with open('test_data.json', 'w') as f:
#     json.dump(user_details, f)



