def filter_by_state(list_of_dict: list[dict], key_state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список словарей,
    а возвращает новый, отфильтрованный по критерию список словарей"""
    filter_list = []
    for dictionary in list_of_dict:
        if dictionary["state"] == key_state:
            filter_list.append(dictionary)
    return filter_list


def sort_by_date(list_for_sort: list[dict], reverse_sort: bool = True) -> list[dict]:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки, а возвращает отсортированный по дате список"""
    sorted_list = sorted(list_for_sort, reverse=reverse_sort, key=lambda i: i["date"])
    return sorted_list
