def filter_by_currency(transaction: list[dict], currency: str):
    result = (value for value in transaction if value['operationAmount']['currency']["code"] == currency)
    for val in result:
        yield val


def transaction_descriptions(transaction: list[dict]):
    result = (value["description"] for value in transaction if value.get("description"))
    for res in result:
        yield res
