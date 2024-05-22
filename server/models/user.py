from flask_login import UserMixin
from models.user_id import UserId
from utils.string_utils import is_not_null_or_empty

class User (UserMixin):
    #constructor
    def __init__(self, id, user_name, first_name, last_name, email):
        self._id = UserId(id)
        self._user_name = is_not_null_or_empty(user_name)
        self._first_name = is_not_null_or_empty(first_name)
        self._last_name = is_not_null_or_empty(last_name)
        self._email = is_not_null_or_empty(email)

    #accessors
    def get_id(self):
        return self.id

    def get_user_name(self):
        return self._user_name
    
    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name
    
    def get_email(self):
        return self._email