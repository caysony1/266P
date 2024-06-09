from models.user_id import UserId
from models.final import Final
from utils.string_utils import is_not_null_or_empty

class User:
    id: UserId = Final()
    user_name: str = Final()
    first_name: str = Final()
    last_name: str = Final()
    email: str = Final()

    def __init__(self, id: int, user_name: str, first_name: str, last_name: str, email: str):
        self.id = UserId(id)
        self.user_name = is_not_null_or_empty(user_name)
        self.first_name = is_not_null_or_empty(first_name)
        self.last_name = is_not_null_or_empty(last_name)
        self.email = is_not_null_or_empty(email)