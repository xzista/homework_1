import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, result', [(7000792289606361, '7000 79** **** 6361'),
                                           ('7000792289602222', '7000 79** **** 2222')])
def test_get_mask_card_number(value, result):
    assert get_mask_card_number(value) == result

    with pytest.raises(Exception):
        get_mask_card_number(7920_6361_289)
    with pytest.raises(Exception):
        get_mask_card_number('')


@pytest.mark.parametrize('value, result', [(73654108430135874305, '**4305'),
                                           ('84301358758743051111', '**1111')])
def test_get_mask_account(value, result):
    assert get_mask_account(value) == result

    with pytest.raises(Exception):
        get_mask_account('')
    with pytest.raises(Exception):
        get_mask_account(12323)
