from models.user_id import UserId
from utils.string_utils import is_not_null_or_empty

class User:
    #constructor
    def __init__(self, user_id, user_name, first_name, last_name):
        self._user_id = UserId(user_id)
        self._user_name = is_not_null_or_empty(user_name)
        self._first_name = is_not_null_or_empty(first_name)
        self._last_name = is_not_null_or_empty(last_name)

    #accessors
    def get_user_id(self):
        return self._user_id

    def get_user_name(self):
        return self._user_name
    
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name