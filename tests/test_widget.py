import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize('value, result', [('Visa Platinum 7000792289606361', 'Visa Platinum 7000 79** **** 6361'),
                                           ('Счет 73654108430135874305', 'Счет **4305'),
                                           ('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                           ('Счет 64686473678894779589', 'Счет **9589'),
                                           ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                           ('Счет 35383033474447895560', 'Счет **5560'),
                                           ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                           ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                           ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353')])
def test_mask_account_card(value, result):
    assert mask_account_card(value) == result

    with pytest.raises(Exception):
        mask_account_card('Visa Platinum 700079228960636')
    with pytest.raises(Exception):
        mask_account_card('')
    with pytest.raises(Exception):
        mask_account_card('счет 1232122')

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == '11.03.2024'

    with pytest.raises(Exception):
        get_date('')
    with pytest.raises(Exception):
        get_date('123123123123')
