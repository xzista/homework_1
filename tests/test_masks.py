import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, result', [(7000792289606361, '7000 79** **** 6361'),
                                           ('7000792289606361', '7000 79** **** 6361'),
                                           (792063612896, '7920 63** **** 2896'),
                                           ('', ' ** **** ')])
def test_get_mask_card_number(value, result):
    assert get_mask_card_number(value) == result


@pytest.mark.parametrize('value, result', [(73654108430135874305, '**4305'),
                                           (430135875410, '**5410'),
                                           ('73654108430135875410', '**5410'),
                                           ('', '**')])
def test_get_mask_account(value, result):
    assert get_mask_account(value) == result