from server.utils.number_utils import is_positive

class AccountBalance:
    #constructor
    def __init__(self, account_balance):
        self._account_balance = is_positive(account_balance)

    #accessors
    def get_account_balance(self):
        return self._account_balance