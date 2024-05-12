from server.utils.number_utils import is_positive

class AccountBalance:
    #constructor
    def __init__(self, account_balance):
        if is_positive(account_balance) is False:
            raise ValueError('Invalid Account Balance detected')
        
        self._account_balance = account_balance

    #accessors
    def get_account_balance(self):
        return self._account_balance