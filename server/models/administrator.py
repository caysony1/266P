from models.user import User

class Administrator (User):
    #constructor
    def __init__(self, user_id, user_name, first_name, last_name):
        User.__init__(self, user_id, user_name, first_name, last_name)

    # if there are additional methods, implement them here