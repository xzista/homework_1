from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
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
