from models.final import Final
from models.account_balance import AccountBalance
from utils.number_utils import is_positive
from utils.string_utils import is_not_null_or_empty

class RegisterUser:
    user_name: str = Final()
    password: str = Final()
    first_name: str = Final()
    last_name: str = Final()
    email: str = Final()
    account_balance: AccountBalance = Final()

    def __init__(self, user_name: str, password: str, first_name: str, last_name: str, email: str, account_balance: float):
        self.user_name = is_not_null_or_empty(user_name)
        self.password = is_not_null_or_empty(password) # be sure to hash this!
        self.first_name = is_not_null_or_empty(first_name)
        self.last_name = is_not_null_or_empty(last_name)
        self.email = is_not_null_or_empty(email)
        self.account_balance = AccountBalance(account_balance)