from classes.transactions import Transaction


def test_empty():
    assert not Transaction({})


def test_not_executed():
    assert not Transaction({"state": "CANCELED"}).is_executed


def test_details():
    assert Transaction({"test": "test"}).details == {"test": "test"}


def test_get_transaction_details():
    details = {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    }
    assert Transaction(details).get_transaction_details() == \
           "23.03.2018 Открытие вклада\n -> Счет **2431\n48223.05 руб."
