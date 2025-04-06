import json


def convert_json_to_list_of_dict(path_json: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    result = []
    try:
        with open(path_json, "r", encoding='utf-8') as f:
            result = json.load(f)
    except FileNotFoundError:
        print('Ошибка: файл не найден!')
    return result