from server.models.account_balance import AccountBalance
from server.models.account_id import AccountId
from server.models.account_type import AccountType
from server.models.user_id import UserId

class Account:
    #constructor
    def __init__(self, account_id, user_id, account_type, account_balance):
        self._account_id = AccountId(account_id)
        self._user_id = UserId(user_id)
        self._account_type = any(account_type == item.value for item in AccountType)
        self._account_balance = AccountBalance(account_balance)

    def get_account_id (self):
        return self._account_id
    
    def get_user_id (self):
        return self._user_id    
    
    def get_account_type (self):
        return self._account_type    

    def get_account_balance (self):
        return self._account_balance    