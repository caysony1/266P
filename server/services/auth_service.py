from flask_login import LoginManager
from models.register_user import RegisterUser
from database.db_controller import DBController
import logging
from models.user import User
from models.user_id import UserId

'''
Changelog: (FIX PHASE)
    06/09/24 - Updated service to use better data integrity models
    06/06/24 - Logger no longer reveals personal or sensitive info.

'''

class AuthService:
    def __init__(self):
        pass

    def get_user(self, user_id: int) -> User:
        dbc = DBController()
        user_info = dbc.get_user_by_user_id(user_id)
        return User(
            user_info.get('id'),
            user_info.get('username'),
            user_info.get('first_name'),
            user_info.get('last_name'),
            user_info.get('email')
        )

    def get_user_by_name(self, user_name: str) -> User:
        dbc = DBController()
        user_info = dbc.get_user_by_username(user_name)
        return User(
            user_info.get('id'),
            user_info.get('username'),
            user_info.get('first_name'),
            user_info.get('last_name'),
            user_info.get('email')
        )

    def user_exists(self, user_name)-> bool:
        dbc = DBController()
        existing_user = dbc.get_user_by_username(user_name)
        return existing_user is not None

    def is_valid_credentials(self, user_name, password) -> bool:
        dbc = DBController()
        existing_user = dbc.get_user_by_username(user_name)

        if existing_user is None:
            return False

        return existing_user.get('password') == password

    def register(self, user_name, password, first_name, last_name, email, account_balance) -> None:
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

        logger = logging.getLogger()
        logger.info(f"AuthService - Registering new user: {new_user.user_name} - Adding to database...")

        dbc.insert_user(
            new_user.user_name, 
            new_user.password, 
            new_user.first_name,
            new_user.last_name, 
            new_user.email
        )

        user_id = dbc.get_user_by_username(new_user.user_name).get('id')

        logger.info(f"AuthService - Adding new account for {new_user.user_name} - Adding to database...")

        dbc.insert_account(user_id, account_balance)
