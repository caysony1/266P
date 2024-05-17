from models.login_user import LoginUser
from models.register_user import RegisterUser
from database.db_controller import DBController


'''
Changelog: 

    05/16/24 - account_type no longer required for register()
    05/15/24 - Base functionality for register() implemented.

'''

# preliminary material. subject to change
class AuthService:
    def __init__(self):
        pass

    def get_user(self, user_name, password):
        # get the user associated with the logged in session
        login_user = LoginUser(user_name, password)
        pass

    def register(self, user_name, password, first_name, last_name, account_balance):
        """
        Add new user and account to bank database.

        Args:
            user_name: Type[Str]
            password: Type[Str]
            first_name: Type[Str]
            last_name: Type[Str]
            account_balance: Type[Float]

        Returns:
            None
        """
        # perform action to put into the database - User and Accounts table

        new_user = RegisterUser(user_name, password, first_name, last_name, account_balance)

        dbc = DBController()

        dbc.insert_user(new_user.get_user_name(), new_user.get_password(), new_user.get_first_name(),
                        new_user.get_last_name())

        get_user_id = dbc.get_user_by_username(new_user.get_user_name()).get('id')

        dbc.insert_account(get_user_id, account_balance)

    def login(self, user_name, password):
        # perform authentication action and utilize the database
        pass
