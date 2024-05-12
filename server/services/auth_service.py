from models.login_user import LoginUser
from models.register_user import RegisterUser

#preliminary material. subject to change
class AuthService:
    def __init__(self):
        pass

    def get_user (user_name, password):
        # get the user associated with the logged in session
        login_user = LoginUser(user_name, password)
        pass

    def register (user_name, password, first_name, last_name, account_balance):
        new_user = RegisterUser(user_name, password, first_name, last_name, account_balance)
        # perform action to put into the database - User and Accounts table
        pass

    def login (user_name, password):
        # perform authentication action and utilize the database
        pass
