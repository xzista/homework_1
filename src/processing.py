import re
from collections import Counter


def filter_by_state(list_of_dict: list[dict], key_state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей,
    а возвращает новый, отфильтрованный по критерию список словарей"""
    filter_list = []
    for dictionary in list_of_dict:
        if dictionary.get("state") == key_state:
            filter_list.append(dictionary)
    if not filter_list:
        raise KeyError("В списке словарей ключей с именем state не обнаружено")
    return filter_list


def sort_by_date(list_for_sort: list[dict], reverse_sort: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки, а возвращает отсортированный по дате список"""
    sorted_list = sorted(list_for_sort, reverse=reverse_sort, key=lambda i: i["date"])
    return sorted_list


def filter_by_description(list_of_dict: list, search: str) -> list:
    """Функция, которая принимает список словарей и строку поиска,
    а возвращает список словарей, с искомой строкой поиска в описании"""
    result =[]
    for dictionary in list_of_dict:
        if re.search(f'{search}', dictionary.get("description")):
            result.append(dictionary)
    return result


def count_operations_by_category(list_of_dict: list, list_of_categories: list):# -> dict:
    """Функция, которая принимает список словарей и строку поиска,
    а возвращает словарь, где ключ — это категория, а количество операций его значение."""
    result_dict = {}
    categories_by_list = [dictionary.get("description") for dictionary in list_of_dict]
    category_count = Counter(categories_by_list)
    for category in list_of_categories:
        result_dict[category] = category_count[category]
    return result_dict
