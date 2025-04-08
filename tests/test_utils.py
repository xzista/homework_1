from unittest.mock import patch, mock_open

import pytest

from src.utils import convert_json_to_list_of_dict


@patch('builtins.open', new_callable=mock_open, read_data='[1, 2, 3]')
@patch('json.load')
def test_convert_json_to_list_of_dict(mock_json_load, mock_open):
    mock_json_load.return_value = [1, 2, 3]

    result = convert_json_to_list_of_dict('file.json')
    assert result == [1, 2, 3]

    mock_open.assert_called_once_with('file.json', 'r', encoding='utf-8')
    mock_json_load.assert_called_once()


def test_error_convert_json_to_list_of_dict():
    with pytest.raises(FileNotFoundError):
        convert_json_to_list_of_dict('')