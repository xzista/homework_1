def filter_by_currency(transaction: list[dict], currency: str):
    if not transaction:
        raise Exception("Передан пустой список")
    result = (value for value in transaction if value["operationAmount"]["currency"]["code"] == currency)
    for val in result:
        yield val


def transaction_descriptions(transaction: list[dict]):
    if not transaction:
        raise Exception("Передан пустой список")
    result = (value["description"] for value in transaction if value.get("description"))
    for res in result:
        yield res


def card_number_generator(start: int | str, stop: int | str):
    i = start
    while i <= stop:
        num16 = str(start).zfill(16)
        yield num16[:4] + " " + num16[4:8] + " " + num16[8:12] + " " + num16[-4:]
        start += 1
        i += 1
