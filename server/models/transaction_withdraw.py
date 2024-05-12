from models.account import Account
from utils.number_utils import is_positive

class TransactionWithdraw:
    #constructor
    def __init__(self, account, amount):
        # be very cautious here to do validation with Account class
        self._account = Account(account.account_id, account.user_id, account.account_type, account.account_balance)
        self._amount = is_positive(amount)

    def get_account_id(self):
        return self._account.get_account_id()
    
    def get_user_id(self):
        return self._account.get_user_id()

    def get_account_type(self):
        return self._account.get_account_type()

    def get_withdraw_amount(self):
        return self._amount   