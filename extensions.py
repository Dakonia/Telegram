import requests
import json
from config import keys

class ConvertionException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):


        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}. Введите целое число.')

        try:
            amount = str(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}. Введите целое число.')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/6f3fb2412d2bf36d47f4a77b/pair/{quote_ticker}/{base_ticker}/{amount}')
        resp = json.loads(r.content)
        total_base = json.loads(r.content)['conversion_result']

        return total_base