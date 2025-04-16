import csv
import logging

import pandas as pd

logger = logging.getLogger("csv_and_xlsx_converters")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/csv_and_xlsx_converters.log", mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def convert_csv_to_list_of_dict(path_csv: str) -> list:
    """Функция, которая принимает на вход путь до CSV-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    logger.info(f"Запуск функции: {convert_csv_to_list_of_dict.__name__} с путем к файлу: {path_csv}")
    result = []
    try:
        with open(path_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                row_dict = {
                    "id": row["id"],
                    "state": row["state"],
                    "date": row["date"],
                    "operationAmount": {
                        "amount": row["amount"],
                        "currency": {"name": row["currency_name"], "code": row["currency_code"]},
                    },
                    "description": row["description"],
                    "from": row["from"],
                    "to": row["to"],
                }
                result.append(row_dict)
    except FileNotFoundError as e:
        logger.error(f"ОШИБКА: {e}")
        print("Ошибка: файл не найден!")
        raise e
    logger.info("Функция отработала успешно")
    return result


def convert_xlsx_to_list_of_dict(path_xlsx: str) -> list:
    """Функция, которая принимает на вход путь до xlsx-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    logger.info(f"Запуск функции: {convert_xlsx_to_list_of_dict.__name__} с путем к файлу: {path_xlsx}")
    try:
        data_excel = pd.read_excel(path_xlsx)
        list_excel = data_excel.to_dict(orient="records")
    except FileNotFoundError as e:
        logger.error(f"ОШИБКА: {e}")
        print("Ошибка: файл не найден!")
        raise e
    logger.info("Функция отработала успешно")
    return list_excel
