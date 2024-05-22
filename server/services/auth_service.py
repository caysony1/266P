from flask_login import LoginManager
from models.register_user import RegisterUser
from database.db_controller import DBController
import logging
import datetime

'''
Changelog: 

    05/22/24 - added logging
    05/16/24 - account_type no longer required for register()
    05/15/24 - Base functionality for register() implemented.

'''


# preliminary material. subject to change
class AuthService:
    def __init__(self):
        pass

    def get_user(self, user_id: int):
        dbc = DBController()
        user = dbc.get_user_by_user_id(user_id)
        return user

    def get_user_by_name(self, user_name: str):
        dbc = DBController()
        user = dbc.get_user_by_username(user_name)
        return user

    def user_exists(self, user_name):
        dbc = DBController()
        existing_user = dbc.get_user_by_username(user_name)
        return existing_user is not None

    def is_valid_credentials(self, user_name, password) -> bool:
        dbc = DBController()
        existing_user = dbc.get_user_by_username(user_name)

        if existing_user is None:
            return False

        return existing_user.get('password') == password

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

        logger = logging.getLogger()
        logger.info("AuthService - Registering new user!")
        logger.info(
            "Username: " + new_user.get_user_name() + ", Password: " + new_user.get_password() + ", First name: " + new_user.get_first_name() + ", Last name: " + new_user.get_last_name() + ", Email: " + new_user.get_email())

        get_user_id = dbc.get_user_by_username(new_user.get_user_name()).get('id')

        logger.info("AuthService - Adding new account!")
        logger.info("User id: " + str(get_user_id) + " Starting balance: " + str(account_balance))

        dbc.insert_account(get_user_id, account_balance)
