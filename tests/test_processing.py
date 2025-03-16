import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import data_for_module_processing


def test_filter_by_state(data_for_module_processing, expected_data_1, expected_data_2):
    assert filter_by_state(data_for_module_processing) == expected_data_1
    assert filter_by_state(data_for_module_processing, 'CANCELED') == expected_data_2

    with pytest.raises(KeyError):
        filter_by_state([{'id': 939719570, 'staaate': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}])
    with pytest.raises(KeyError):
        filter_by_state([])


def test_sort_by_date(data_for_module_processing, result_data, result_data_rev):
    assert sort_by_date(data_for_module_processing) == result_data
    assert sort_by_date(data_for_module_processing, False) == result_data_rev
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                         {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                         ])
    assert sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '201907-03T18:35:29.512364'},
                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
                        ])