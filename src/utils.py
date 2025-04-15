import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def convert_json_to_list_of_dict(path_json: str) -> list:
    """Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях"""
    logger.info(f"Запуск функции: {convert_json_to_list_of_dict.__name__} с путем к файлу: {path_json}")
    try:
        with open(path_json, "r", encoding="utf-8") as f:
            result = json.load(f)
    except FileNotFoundError as e:
        logger.error(f"ОШИБКА: {e}")
        print("Ошибка: файл не найден!")
        raise e
    logger.info("Функция отработала успешно")
    return result
