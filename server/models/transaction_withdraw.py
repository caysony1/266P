from models.account import Account
from models.final import Final
from utils.number_utils import is_positive

class TransactionWithdraw:
    account: Account = Final()
    amount: float = Final()

    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = is_positive(amount)