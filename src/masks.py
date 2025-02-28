def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    list_of_number = []
    str_numbers = str(card_number)
    list_of_number.append(str_numbers[:4])
    list_of_number.append(str_numbers[4:6] + "**")
    list_of_number.append("****")
    list_of_number.append(str_numbers[-4:])
    return " ".join(list_of_number)


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    return "**" + str_account_number[-4:]
