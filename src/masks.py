import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.info(f"Запуск функции: {get_mask_card_number.__name__} с номером карты: {card_number}")
    if len(str(card_number)) != 16:
        logger.error(
            f"ОШИБКА: Количество цифр в номере карты не соответствует действительности:"
            f" {len(str(card_number))}, вместо 16"
        )
        raise Exception("Номер карты должен состоять из 16 цифр")
    list_of_number = []
    str_numbers = str(card_number)
    list_of_number.append(str_numbers[:4])
    list_of_number.append(str_numbers[4:6] + "**")
    list_of_number.append("****")
    list_of_number.append(str_numbers[-4:])
    logger.info("Функция отработала успешно")
    return " ".join(list_of_number)


def get_mask_account(account_number: int | str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    logger.info(f"Запуск функции: {get_mask_account.__name__} с номером счета: {account_number}")
    str_account_number = str(account_number)
    if len(str_account_number) != 20:
        logger.error(
            f"ОШИБКА: Количество цифр в номере счета не соответствует действительности:"
            f" {len(str_account_number)}, вместо 20"
        )
        raise Exception("Номер счета должен состоять из 20 цифр")
    logger.info("Функция отработала успешно")
    return "**" + str_account_number[-4:]
