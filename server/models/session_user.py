from models.user_id import UserId
from models.user import User
from models.final import Final

class SessionUser(User):
    def __init__(self, id: int, user_name: str, first_name: str, last_name: str, email: str):
        super().__init__(id, user_name, first_name, last_name, email)

    # mandatory accessors for Flask to work
    def get_id(self) -> int:
        return self.id.user_id

    def is_active() -> bool:
        return True
    
    def is_authenticated() -> bool:
        return True
    
    def is_anonymous() -> bool:
        return False