from utils.str_funcs import get_masked_card_number, get_masked_account_number, split_by_4


class FundsStorage:
    """funds storage object and its methods"""
    is_card: bool = False
    is_account: bool = False
    name: str = ""
    number: str = ""

    def __init__(self, fund_str: str):
        """init object using incoming string"""
        if fund_str:
            self.name, _, self.number = fund_str.rpartition(" ")
            if self.name == "Счет":
                self.is_account = True
            else:
                self.is_card = True

    def get_name_and_masked_number(self):
        """return masked card/account details"""
        if self.is_card:
            return f"{self.name} {split_by_4(get_masked_card_number(self.number))}"
        elif self.is_account:
            return f"{self.name} {get_masked_account_number(self.number)}"
        else:
            return ""
