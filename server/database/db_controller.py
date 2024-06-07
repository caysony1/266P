from os.path import join, dirname, abspath
import sqlite3
import logging

'''
Changelog: FIX PHASE 
    
    06/06/24 - Removed string concatenation. Re-implemented prepared statements for database communication.
             - Email no longer executes SQL statements.
             - Logger no longer reveals personal or sensitive information.
'''


class DBController:
    """
    Database controller class to act as a liaison between the database and other app components.

    NOTE:
     - DBController methods open a connection to the bank_app.db, perform operations, then close the connection when finished.

    """

    def __init__(self):
        """
        DBController should be able to find the bank_app.db in the project's directory.
        """
        self.db_path = None

        if self.db_path is None:
            self.db_path = join(dirname(dirname(abspath(__file__))), 'bank_app.db')

    def inspect_user_table(self):
        """

        Print out all the data stored in the User table in bank_app.db

        Returns:
            None

        """

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        logger = logging.getLogger()
        logger.info("Database - Inspecting User table")

        sql_query = """SELECT * FROM User;"""

        for user in cursor.execute(sql_query):
            print(user)

        db_connect.close()

    def inspect_account_table(self):
        """
        Print out all the data stored in the Account table in bank_app.db

        Returns:
            None

        """

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        logger = logging.getLogger()
        logger.info("Database - Inspecting Account table")

        sql_query = """SELECT * FROM Account;"""

        for account in cursor.execute(sql_query):
            print(account)

        db_connect.close()

    def execute_query(self, new_sql_query: str, can_commit: bool):
        """
        Execute a full SQL query on the database.

        NOTE:
            - Use TRIPLE quotation marks where you would input a string for new_sql_query (like a docstring)

        Args:
            new_sql_query: Type[Str]
            can_commit: Type[Bool]

        Returns:
            None

        """
        if not can_commit:
            db_connect = sqlite3.connect(self.db_path)

            cursor = db_connect.cursor()

            cursor.execute(new_sql_query)

            db_connect.close()

        if can_commit:
            db_connect = sqlite3.connect(self.db_path)

            cursor = db_connect.cursor()

            cursor.execute(new_sql_query)

            db_connect.commit()

            db_connect.close()

    def insert_user(self, user_name: str, password: str, first_name: str, last_name: str, email: str):
        """
        Add new user to User table in bank_app.db

        Args:
            user_name: Type[Str]
            password: Type[Str]
            first_name: Type[Str]
            last_name: Type[Str]
            email: Type[Str]

        Returns:
            None

        """
        sql_query_insert_user = "INSERT OR IGNORE INTO User (id, username, password, first_name, last_name, email) VALUES (NULL, ?, ?, ?, ?, ?);"

        logger = logging.getLogger()
        logger.info("Database - Inserting user: " + user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        parameters = (user_name, password, first_name, last_name, email)
        cursor.execute(sql_query_insert_user, parameters)

        db_connect.commit()

        db_connect.close()

    def get_user_by_username(self, user_name: str):
        """
        Retrieve user data from User table based on username.

        Returns a Dict with 'id', 'username', 'password', 'first_name', 'last_name'

        Example:

            To retrieve a specific value, you can do it like so:

            dbc = DBController()

            foo_password = dbc.get_user_by_username('foo').get('password')

        Args:
            user_name: Type[Str]

        Returns:
            Type[Dict] if user is found.

        """

        sql_query_get_user = "SELECT * FROM User WHERE username = ?;"

        logger = logging.getLogger()
        logger.info("Database - Attempting to get user by username: " + user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_user, (user_name,))

        data = cursor.fetchall()

        if data is None or data == []:
            return None

        user_data = {
            "id": data[0][0],
            "username": data[0][1],
            "password": data[0][2],
            "first_name": data[0][3],
            "last_name": data[0][4],
            "email": data[0][5]
        }

        db_connect.close()

        return user_data

    def get_user_by_user_id(self, user_id: int):
        """
        Retrieve user data from User table based on user ID.

        Returns a Dict with 'id', 'username', 'password', 'first_name', 'last_name'

        Example:

            To retrieve a specific value, you can do it like so:

            dbc = DBController()

            foo_password = dbc.get_user_by_id(1).get('password')

        Args:
            user_id: Type[Int]

        Returns:
            Type[Dict] if user is found.

        """

        sql_query_get_user = f"SELECT * FROM User WHERE id = ? ;"

        logger = logging.getLogger()
        logger.info(f"Database - Attempting to get user by user ID: {user_id}")

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_user, (user_id,))

        data = cursor.fetchall()

        if data is None:
            return None

        user_data = {
            "id": data[0][0],
            "username": data[0][1],
            "password": data[0][2],
            "first_name": data[0][3],
            "last_name": data[0][4],
            "email": data[0][5]
        }

        db_connect.close()

        return user_data

    def get_account_by_username(self, user_name: str):
        """
        Retrieve account data from Account table based on username.

        Returns a Dict with 'id', 'user_id', 'balance'

        Example:
            To retrieve a specific value, you can do it like so:

            dbc = DBController()

            foo_balance = dbc.get_account_by_username('foo').get('balance')

        Args:
            user_name: Type[Str]

        Returns:
            Type[Dict] if account is found.

        """

        sql_query_get_account = "SELECT * FROM Account WHERE id = ?;"

        logger = logging.getLogger()
        logger.info("Database - Attempting to get account by username: " + user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_account, (user_name,))

        data = cursor.fetchall()

        account_data = {
            "id": data[0][0],
            "user_id": data[0][1],
            "balance": data[0][2]
        }

        db_connect.close()

        return account_data

    def get_account_by_user_id(self, user_id: int):
        """
           Retrieve account data from Account table based on user ID.

           Returns a Dict with 'id', 'user_id', 'balance'

           Example:
               - To retrieve a specific value, you can do it like so:

               dbc = DBController()

               foo_balance = dbc.get_account_by_user_id(1).get('balance')


           Args:
               user_id: Type[Int]

           Returns:
               Type[Dict] if account is found.

        """
        sql_query_get_account = f"SELECT * FROM Account WHERE user_id = ?;"

        logger = logging.getLogger()
        logger.info(f"Database - Attempting to get account by user ID: {user_id}")

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_account, (user_id,))

        data = cursor.fetchall()

        account_data = {
            "id": data[0][0],
            "user_id": data[0][1],
            "balance": data[0][2]
        }

        db_connect.close()

        return account_data

    def insert_account(self, user_id: int, balance: float):
        """
        Add new account to Account table in bank_app.db

        Args:
            user_id: Type[Int]
            balance: Type[Float]

        Returns:
            None

        """

        sql_query_insert_account = "INSERT INTO Account (id, user_id, balance) VALUES (NULL, ?, ?)"

        logger = logging.getLogger()
        logger.info(f"Database - Inserting new account: user_id: {user_id}")

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_insert_account, (user_id, balance))

        db_connect.commit()

        db_connect.close()

    def update_balance(self, user_id: int, updated_balance: float):
        """
        Update the balance in a user's bank account.

        Args:
            user_id: Type[Int]
            updated_balance: Type[Float]

        Returns:
            None

        """

        sql_query_update_balance = "UPDATE Account SET balance = ? WHERE id = ?;"

        logger = logging.getLogger()
        logger.info(f"Database - Updating balance for: {user_id}")

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_balance, (user_id, updated_balance))

        db_connect.commit()

        db_connect.close()

    def update_password(self, user_name: str, new_password: str):
        """
        Update a user's password in the User table.

        Args:
            user_name: Type[Str]
            new_password: Type[Str]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        sql_query_update_password = f"UPDATE User SET password = ? WHERE id = ?;"

        logger = logging.getLogger()
        logger.info("Database - Updating password for: " + user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_password, (new_password, user_id))

        db_connect.commit()

        db_connect.close()

    def update_user_name(self, user_name: str, new_user_name: str):
        """
        Update the username.

        Args:
            user_name: Type[Str]
            new_user_name: Type[Str]

        Returns:
            None

        """

        user_id = self.get_user_by_username(user_name).get('id')

        sql_query_update_username = "UPDATE User SET username = ? WHERE id = ?;"

        logger = logging.getLogger()
        logger.info(
            "Database - Updating username: " + "Current username: " + user_name + " New username: " + new_user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_username, (new_user_name, user_id))

        db_connect.commit()

        db_connect.close()

    def update_first_name(self, user_name: str, new_first_name: str):
        """
        Update a user's first name in the User table.

        Args:
            user_name: Type[Str]
            new_first_name: Type[Str]

        Returns:
            None

        """

        user_id = self.get_user_by_username(user_name).get('id')

        sql_query_update_firstname = "UPDATE User SET first_name = ? WHERE id = ?;"

        logger = logging.getLogger()
        logger.info(
            "Database - Updating first name for: " + user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_firstname, (new_first_name, user_id))

        db_connect.commit()

        db_connect.close()

    def update_last_name(self, user_name: str, new_last_name: str):
        """
        Update a user's last name in the User table.

        Args:
            user_name: Type[Str]
            new_last_name: Type[Str]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        sql_query_update_name = "UPDATE User SET last_name = ? WHERE id = ?;"

        logger = logging.getLogger()
        logger.info(
            "Database - Updating last name for: " + "Username: " + user_name)

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_name, (new_last_name, user_id))

        db_connect.commit()

        db_connect.close()
