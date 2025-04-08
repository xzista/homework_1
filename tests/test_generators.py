import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(result_data_gen, expected_data_for_gen1):
    generator1 = filter_by_currency(transaction=result_data_gen, currency="RUB")
    assert next(generator1) == expected_data_for_gen1
    assert next(generator1) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }

    with pytest.raises(StopIteration):
        generator2 = filter_by_currency(result_data_gen, "")
        assert next(generator2) == expected_data_for_gen1
    with pytest.raises(Exception):
        generator3 = filter_by_currency([], "")
        assert next(generator3) == expected_data_for_gen1


def test_transaction_descriptions(result_data_gen):
    descriptions = transaction_descriptions(result_data_gen)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"

    with pytest.raises(Exception):
        generator3 = transaction_descriptions([])
        assert next(generator3)


@pytest.mark.parametrize(
    "value_min, value_max, result",
    [
        (9999_9999_9999_9999, 9999_9999_9999_9999, "9999 9999 9999 9999"),
        (1, 2, "0000 0000 0000 0001"),
        (2, 3, "0000 0000 0000 0002"),
    ],
)
def test_card_number_generator(value_min, value_max, result):
    assert next(card_number_generator(value_min, value_max)) == result

    generator = card_number_generator(2, 3)
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
    with pytest.raises(StopIteration):
        next(generator)