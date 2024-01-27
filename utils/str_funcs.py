def split_by_4(value: str):
    """splits the incoming string into four-character separated strings"""
    output_list = list()
    while len(value) > 4:
        output_list.append(value[:4])
        value = value[4:]
    if value:
        output_list.append(value)
    return " ".join(output_list)


def get_masked_card_number(card_num: str):
    """masked card number in format XXXXXX******XXXX"""
    return f'{card_num[:6]}{"*" * len(card_num[6:-4])}{card_num[-4:]}'


def get_masked_account_number(account_num: str):
    """masked account number in format **XXXX"""
    return f"**{account_num[-4:]}"
