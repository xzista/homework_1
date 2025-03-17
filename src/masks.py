def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if len(str(card_number)) != 16:
        raise Exception('Номер карты должен состоять из 16 цифр')
    list_of_number = []
    str_numbers = str(card_number)
    list_of_number.append(str_numbers[:4])
    list_of_number.append(str_numbers[4:6] + "**")
    list_of_number.append("****")
    list_of_number.append(str_numbers[-4:])
    return " ".join(list_of_number)


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        raise Exception('Номер счета должен состоять из 20 цифр')
    return "**" + str_account_number[-4:]
