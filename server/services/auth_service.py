from flask_login import LoginManager
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

    def get_user(self, user_id):
        dbc = DBController()
        user = dbc.get_user_by_user_id(user_id)
        return user
    
    def user_exists(self, user_name):
        dbc = DBController()
        existing_user = dbc.get_user_by_username(user_name)
        return existing_user is not None

    def register(self, user_name, password, first_name, last_name, email, account_balance):
        """
        Add new user and account to bank database.

        Args:
            user_name: Type[Str]
            password: Type[Str]
            first_name: Type[Str]
            last_name: Type[Str]
            email: Type[Str]
            account_balance: Type[Float]

        Returns:
            None
        """
        # perform action to put into the database - User and Accounts table

        new_user = RegisterUser(user_name, password, first_name, last_name, email, account_balance)

        dbc = DBController()

        dbc.insert_user(new_user.get_user_name(), new_user.get_password(), new_user.get_first_name(),
                        new_user.get_last_name(), new_user.get_email())

        get_user_id = dbc.get_user_by_username(new_user.get_user_name()).get('id')

        dbc.insert_account(get_user_id, account_balance)
