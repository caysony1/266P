from models.user_id import UserId
from models.user import User

class SessionUser(User):
    #constructor
    def __init__(self, id, user_name, first_name, last_name, email):
        super().__init__(id, user_name, first_name, last_name, email)

    #accessors
    def get_id(self) -> int:
        return self.id.get_id()

    def is_active() -> bool:
        return True
    
    def is_authenticated() -> bool:
        return True
    
    def is_anonymous() -> bool:
        return False