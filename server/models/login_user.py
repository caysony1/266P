from utils.number_utils import is_positive
from utils.string_utils import is_not_null_or_empty

class LoginUser:
    #constructor
    def __init__(self, user_name, password):
        self._user_name = is_not_null_or_empty(user_name)
        self._password = is_not_null_or_empty(password) # be sure to hash this!

    #accessors
    def get_user_name(self):
        return self._user_name
    
    def get_password(self):
        return self._password