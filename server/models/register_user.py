from server.utils.number_utils import is_positive
from server.utils.string_utils import is_not_null_or_empty

class RegisterUser:
    #constructor
    def __init__(self, user_name, password, first_name, last_name, account_balance):
        self._user_name = is_not_null_or_empty(user_name)
        self._password = is_not_null_or_empty(password) # be sure to hash this!
        self._first_name = is_not_null_or_empty(first_name)
        self._last_name = is_not_null_or_empty(last_name)
        self._account_balance = is_positive(account_balance)

    #accessors
    def get_user_name(self):
        return self._user_name
    
    def get_password(self):
        return self._password

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def get_account_balance(self):
        return self._account_balance