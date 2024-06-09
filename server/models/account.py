from models.account_balance import AccountBalance
from models.account_id import AccountId
from models.user_id import UserId
from models.final import Final

class Account:
    account_id: AccountId = Final()
    user_id: UserId = Final()
    account_balance: AccountBalance = Final()

    def __init__(self, account_id: int, user_id: int, account_balance: float):
        self.account_id = AccountId(account_id)
        self.user_id = UserId(user_id)
        self.account_balance = AccountBalance(account_balance)