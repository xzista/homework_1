def filter_by_state(list_of_dict: list[dict], key_state: str='EXECUTED') -> list[dict]:
    """ Функция, которая принимает список словарей,
    а возвращает новый, отфильтрованный по критерию список словарей"""
    filter_list = []
    for dictionary in list_of_dict:
        if dictionary['state'] == key_state:
            filter_list.append(dictionary)
    return filter_list
