from src.csv_and_xlsx_converters import convert_csv_to_list_of_dict, convert_xlsx_to_list_of_dict
from src.generators import filter_by_currency
from src.processing import sort_by_date, filter_by_state, filter_by_description
from src.utils import convert_json_to_list_of_dict
from src.widget import get_date, mask_account_card


def main():
    user_input_greeting = int(input(f"Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
                           f"Выберите необходимый пункт меню:\n"
                           f"1. Получить информацию о транзакциях из JSON-файла\n"
                           f"2. Получить информацию о транзакциях из CSV-файла\n"
                           f"3. Получить информацию о транзакциях из XLSX-файла\n").strip())

    print(f'Для обработки выбран '
          f'{"JSON-файл" if user_input_greeting == 1 else "CSV-файл" if user_input_greeting == 2 else "XLSX-файл"}')

    if user_input_greeting == 1:
        data = convert_json_to_list_of_dict('../data/operations.json')
    elif user_input_greeting == 2:
        data = convert_csv_to_list_of_dict('../data/transactions.csv')
    else:
        data = convert_xlsx_to_list_of_dict('../data/transactions_excel.xlsx')

    while True:
        user_input_status = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                                  "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").strip().upper()
        if user_input_status in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Операции отфильтрованы по статусу "{user_input_status}"\n')
            data = filter_by_state(data, key_state=user_input_status)
            break
        print(f"\nОшибка: Статус операции {user_input_status} недоступен\n")

    while True:
        user_input_by_date = input("Отсортировать операции по дате? Да/Нет\n").strip().lower()
        if user_input_by_date == 'да':
            while True:
                user_input_by_sort = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
                if user_input_by_sort == 'по возрастанию':
                    data = sort_by_date(data, reverse_sort=False)
                    break
                elif user_input_by_sort == 'по убыванию':
                    data = sort_by_date(data)
                    break
                print('Введите "по возрастанию/по убыванию"')
        elif user_input_by_date == 'нет':
            break
        else:
            print('Введите "Да/Нет"')
            continue
        break

    while True:
        user_input_by_currency = input("Выводить только рублевые транзакции? Да/Нет\n").strip().lower()
        if user_input_by_currency == 'да':
            data = filter_by_currency(data, "RUB")
            break
        elif user_input_by_currency == 'нет':
            break
        print('Введите "Да/Нет"')

    while True:
        user_input_by_word = input("Отфильтровать список транзакций по определенному слову "
                                   "в описании? Да/Нет\n").strip().lower()
        if user_input_by_word == 'да':
            word_for_filter = input("Введите слово для фильтрации: ")
            data = filter_by_description(data, search=word_for_filter)
            break
        elif user_input_by_word == 'нет':
            break
        print('Введите "Да/Нет"')

    print(f"Всего банковских операций в выборке: {len(data)}\n")
    if data:
        for value in data:
            print(get_date(value['date']), value['description'])
            if value.get('from') and value.get('from').lower() != 'nan':
                print(mask_account_card(value['from']), '->', mask_account_card(value['to']))
            else:
                print(mask_account_card(value['to']))
            print(round(float(value["operationAmount"]["amount"])),
                  value["operationAmount"]["currency"]["name"], '\n')
    else:
        print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')
