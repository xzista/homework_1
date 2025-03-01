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
        return name + get_mask_card_number(int(numbers))
    else:
        return name + get_mask_account(int(numbers))


def get_date(date: str) -> str:
    """Функция, которая принимает на вход строку с датой в неправильном формате,
    а возвращает дату в нужном формате"""
    date_list = date[:10].split("-")
    date_list.reverse()
    return ".".join(date_list)
