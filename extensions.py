import requests
import json
from Conf import keys

class Exep(Exception):
    pass

class Conv:
    @staticmethod
    def convert(queue: str, base: str, amount: str ):
        if queue == base:
            raise Exep(f"Нельзя перевести одинаковые валюты {queue}")

        try:
            queue_ticker = keys[queue]
        except KeyError:
            raise Exep(f"Неверная валюта {queue}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise Exep(f"Неверная валюта {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise Exep(f"неверное количество {amount}")
        r = requests.get(
            f'https://api.currencyapi.com/v3/latest?apikey=cur_live_ZDRuXU9hkIngjWKhu4rVFqBRaASr7hbe3kJEKWif&currencies={queue_ticker}&base_currency={base_ticker}')
        sum = json.loads(r.content)[keys[base]]*amount