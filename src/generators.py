def filter_by_currency(transaction: list[dict], currency: str):
    result = (value for value in transaction if value['operationAmount']['currency']["code"] == currency)
    for val in result:
        yield val


def transaction_descriptions(transaction: list[dict]):
    result = (value["description"] for value in transaction if value.get("description"))
    for res in result:
        yield res


def card_number_generator(min_number: int | str, max_number: int | str):
    i = min_number
    while i <= max_number:
        num16 = str(min_number).zfill(16)
        yield num16[:4] + ' ' + num16[4:8] + ' ' + num16[8:12] + ' ' + num16[-4:]
        min_number += 1
        i += 1
