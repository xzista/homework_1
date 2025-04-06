import os

import requests
from dotenv import load_dotenv

from src.generators import filter_by_currency
from src.utils import convert_json_to_list_of_dict


def transaction_amount(transaction: dict) -> float:
    """Функция, которая принимает на вход транзакцию и
    возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    load_dotenv()
    api_token = os.getenv('API_KEY')
    headers = {"apikey": api_token}
    url = (f'https://api.apilayer.com/exchangerates_data/convert?to=RUB'
           f'&from={transaction["operationAmount"]["currency"]["code"]}'
           f'&amount={transaction["operationAmount"]["amount"]}')
    response = requests.request('GET', url=url, headers=headers)
    response_json = response.json()
    # print(response_json)
    # print(response.status_code)
    # print(response.text)
    return round(response_json["result"], 2)


if __name__ == '__main__':
    gen1 = filter_by_currency(convert_json_to_list_of_dict('../data/operations.json'), 'USD')
    print(transaction_amount(next(gen1)))
    # print(transaction_amount(next(gen1)))