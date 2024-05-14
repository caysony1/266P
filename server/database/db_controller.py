import sqlite3
import account

'''
Changelist: 
    
    05/13/24 - Class created. Blocked out methods.

'''

class DBController:
    """
    Database controller class to act as a liaison between the database and other app components.

    TODO @kj-art-dev: Start actual implementation of database communication and methods.
    """

    def __init__(self, database):
        """
        Initialize DBController with the database it controls.
        Args:
            database: db object
        """
        self.database = database

    def inspect_user_table(self):
        """
        (WIP) Get all user data from tables. Should be used

        Returns: All user data currently in table.

        """
        pass

    def inspect_account_table(self):
        """
        (WIP) Get all account data from table.
        """
        pass

    def add_user_to_table(self, user):
        """
        (WIP) Add user object to the user table.

        Args:
            user: User-type object with a user ID.

        Returns: None

        """
        pass

    def add_account_to_table(self, account):
        """
        (WIP) Add a new account object to the account table
        Args:
            account: Account-type object with an account ID.

        Returns: None

        """
        pass

    def update_balance(self, user, account, updated_balance):
        """
        (WIP) Update the account balance for a user. Can be
        Args:
            user: User-type object
            account: Account-type object
            updated_balance: number as float

        Returns: None

        """
        pass

    def update_user_first_name(self, user, first_name):
        """
        (WIP) Update a user's first name in User table in database.

        Args:
            user: User-type object with a user ID
            first_name: New first name as string

        Returns: None

        """
        pass

    def update_user_last_name(self, user, last_name):
        """
        (WIP) Update user's last name in Users table in database

            user: User-type object.
            last_name: New last name as string.

        Returns: None

        """
        pass
