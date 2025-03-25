# Виджет банковских операций клиента

## Описание:

Разработка виджета банковских операций клиента (*будет дополнено по мере разработки*).

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/xzista/homework_1.git
```
2. Установите зависимости:
```
poetry install
```
## Использование:

(*В разработке*)

## Тестирование:

1. Для выполнения тестирования пропишите команду:
```
pytest
```
2. Для получения информации о тестировании пропишите команду:
```
pytest --cov
```

## Модуль Generators

Модуль `generators` предоставляет функции для работы с массивами транзакций. Он включает в себя следующие функции:

- `filter_by_currency(transactions, currency)`: фильтрует транзакции по заданной валюте и возвращает итератор.
- `transaction_descriptions(transactions)`: генератор, возвращающий описания транзакций.
- `card_number_generator(start, stop)`: генератор, который выводит номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ.

### Примеры использования:

```python
# Пример использования filter_by_currency
usd_transactions = filter_by_currency(transactions, 'USD')
for transaction in usd_transactions:
    print(transaction)

# Пример использования transaction_descriptions
for description in transaction_descriptions(transactions):
    print(description)

# Пример использования card_number_generator
for card in card_number_generator(4000123456789010, 4000123456789015):
    print(card)
```

## Документация:

Для получения дополнительной информации обратитесь к [документации](README.md).

## Лицензия:

Этот проект лицензирован по лицензии MIT.