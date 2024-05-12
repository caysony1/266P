from server.utils.number_utils import is_positive

class UserId:
    #constructor
    def __init__(self, user_id):
        # perform validations
        if is_positive(user_id) is False:
            raise ValueError('Invalid User Id detected')
        
        # perform assignments
        self._user_id = user_id

    #accessors
    def get_id(self):
        return self._user_id