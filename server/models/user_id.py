from utils.number_utils import is_positive

class UserId:
    #constructor
    def __init__(self, user_id):
        self._user_id = is_positive(user_id)

    #accessors
    def get_id(self):
        return self._user_id