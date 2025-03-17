from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах,
    и возвращает строку с замаскированным номером"""
    numbers = ""
    name = ""
    for char in card:
        if char.isdigit():
            numbers += char
        else:
            name += char
    if len(numbers) == 16:
        return name + get_mask_card_number(str(numbers))
    elif len(numbers) == 20:
        return name + get_mask_account(str(numbers))
    else:
        raise Exception("Номер не относится ни к счету, ни к номеру карты")


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в неправильном формате,
    а возвращает дату в нужном формате"""
    if len(date) < 10 or date[4] != '-' or date[7] != '-':
        raise Exception('Некорректный формат данных')
    date_list = date[:10].split("-")
    date_list.reverse()
    return ".".join(date_list)
