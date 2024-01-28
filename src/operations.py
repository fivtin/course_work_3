from classes.transactions import ExecutedTransactionsList


def get_last_5_executed_operations():
    """Return last five executed operations sorted by datetime descending order"""
    last_5_transactions = ExecutedTransactionsList().transactions[:5]
    return [t.get_transaction_details() for t in last_5_transactions]


def print_last_5_executed_operations():
    """print last five executed operation sorted by datetime descending order"""
    print(*get_last_5_executed_operations(), sep="\n\n")


print_last_5_executed_operations()
