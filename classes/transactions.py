from classes.funds_storages import FundsStorage
from utils.date_funcs import get_formatted_isodatetime
from utils.file_funcs import load_from_file


class Transaction:
    """Transaction object and its methods"""
    details = dict()

    def __init__(self, details):
        """init transaction with details"""
        if isinstance(details, dict):
            self.details = details
            self._from = FundsStorage(details.get("from", ""))
            self._to = FundsStorage(details.get("to", ""))

    def __bool__(self):
        """return False if details are empty"""
        return bool(self.details)

    @property
    def is_executed(self):
        """return True if transaction state is executed"""
        return self.details.get("state") == "EXECUTED"

    def get_transaction_details(self):
        """return a string representation in the specified format"""
        first_line = f"{get_formatted_isodatetime(self.details['date'])} {self.details['description']}"
        second_line = f"{self._from.get_name_and_masked_number()} -> {self._to.get_name_and_masked_number()}"
        third_line = \
            f"{self.details['operationAmount']['amount']} {self.details['operationAmount']['currency']['name']}"
        return f"{first_line}\n{second_line}\n{third_line}"


class ExecutedTransactionsList:
    """"""

    def __init__(self):
        """"""
        self._transactions = list()
        for operation in load_from_file():
            transaction = Transaction(operation)
            if transaction and transaction.is_executed:
                self._transactions.append(transaction)

        self._transactions.sort(key=lambda x: x.details['date'], reverse=True)

    @property
    def transactions(self):
        return self._transactions
