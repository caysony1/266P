from utils.number_utils import is_positive
from models.final import Final

class UserId:
    user_id: int = Final()
    
    def __init__(self, user_id: int):
        self.user_id = is_positive(user_id)

    # necessary to have Flask identify a session user
    def get_id(self) -> int:
        return self.user_id