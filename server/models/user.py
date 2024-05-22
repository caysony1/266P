from models.user_id import UserId
from utils.string_utils import is_not_null_or_empty

class User:
    #constructor
    def __init__(self, id, user_name, first_name, last_name, email):
        self.id = UserId(id)
        self.user_name = is_not_null_or_empty(user_name)
        self.first_name = is_not_null_or_empty(first_name)
        self.last_name = is_not_null_or_empty(last_name)
        self.email = is_not_null_or_empty(email)

    #accessors
    def get_id(self):
        return self.id

    def get_user_name(self):
        return self.user_name
    
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name
    
    def get_email(self):
        return self.email