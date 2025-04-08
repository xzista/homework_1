from unittest.mock import patch

from src.external_api import transaction_amount


@patch('requests.request')
def test_transaction_amount(mock_request):
    mock_request.return_value.json.return_value = {"result": 3724.305775}
    assert transaction_amount(mock_request) == 3724.31
    assert transaction_amount({"operationAmount": {"amount": "3.22", "currency": {"code": "RUB"}}}) == 3.22

