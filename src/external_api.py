import os

import requests
from dotenv import load_dotenv


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
    return round(response_json["result"], 2)
