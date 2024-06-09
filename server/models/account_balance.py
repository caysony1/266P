from utils.number_utils import is_positive
from models.final import Final

class AccountBalance:
    balance: float = Final()

    def __init__(self, account_balance: float):
        self.balance = is_positive(account_balance)