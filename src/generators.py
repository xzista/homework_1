def filter_by_currency(transaction: list[dict], currency: str):
    result = (value for value in transaction if value['operationAmount']['currency']["code"] == currency)
    for val in result:
        yield val
