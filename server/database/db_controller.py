from os.path import join, dirname, abspath
import sqlite3

'''
Changelog: 
    
    05/16/24 - Added and implemented update_user_name
    05/15/24 - Added and implemented the following methods: 
             - update_balance, update_password, update_first_name, update_last_name, get_account_by_username, get_account_by_user_id, get_user_by_user_id
    05/14/24 - Added and implemented table inspection methods. 
             - Added and implemented insert_user, get_user_by_username, and insert_account methods.
             - Added WIP execute_query_method. Updated docstring format
    05/13/24 - Class created. Blocked out methods.
    
    
'''


class DBController:
    """
    Database controller class to act as a liaison between the database and other app components.

    NOTE:
    DBController methods open a connection to the bank_app.db, perform operations, then close the connection when finished.

    TODO (kj-art-dev):  -   Continue method introduction and implementation for whatever is needed next.
                        -   Duplicate one or more methods, convert them to use concatentation as a vulnerability, then test them out.

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

        sql_query = """SELECT * FROM User"""

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

        sql_query = """SELECT * FROM Account"""

        for account in cursor.execute(sql_query):
            print(account)

        db_connect.close()

    def inspect_account_type_table(self):
        """

        Print out all the data stored in the AccountType table in bank_app.db

        Returns:
            None

        """
        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        sql_query = """SELECT * FROM AccountType"""

        for account_type in cursor.execute(sql_query):
            print(account_type)

        db_connect.close()

    def execute_query(self, new_sql_query, can_commit):
        """

        Execute a full SQL query on the database.

        Args:
            new_sql_query: Type[Str] with TRIPLE quotation marks (like a docstring)
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

    def insert_user(self, user_name, password, first_name, last_name):
        """
        Add new user to User table in bank_app.db

        Args:
            user_name: Type[Str]
            password: Type[Str]
            first_name: Type[Str]
            last_name: Type[Str]

        Returns:
            None

        """

        new_user_values = (user_name, password, first_name, last_name)

        sql_query_insert_user = """INSERT INTO User (id, username, password, first_name, last_name) VALUES (NULL, ?, ?, ?, ?)"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_insert_user, new_user_values)

        db_connect.commit()

        db_connect.close()

    def get_user_by_username(self, user_name):
        """
        Retrieve user data from User table based on username.

        Returns a Dict with 'id', 'username', 'password', 'first_name', 'last_name'

        To retrieve a specific value, you can do it like so:

        Example:

            dbc = DBController()

            foo_password = dbc.get_user_by_username('foo').get('password')

        Args:
            user_name: Type[Str]

        Returns:
            Type[Dict] if user is found.

        """

        sql_query_get_user = """SELECT * FROM User WHERE username = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_user, (user_name,))

        data = cursor.fetchall()

        user_data = {

            "id": data[0][0],
            "username": data[0][1],
            "password": data[0][2],
            "first_name": data[0][3],
            "last_name": data[0][4]
        }

        db_connect.close()

        return user_data

    def get_user_by_user_id(self, user_id):
        """
        Retrieve user data from User table based on user ID.

        Returns a Dict with 'id', 'username', 'password', 'first_name', 'last_name'

        To retrieve a specific value, you can do it like so:

        Example:

            dbc = DBController()

            foo_password = dbc.get_user_by_id(1).get('password')

        Args:
            user_id: Type[Int]

        Returns:
            Type[Dict] if user is found.

        """

        sql_query_get_user = """SELECT * FROM User WHERE id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_user, (user_id,))

        data = cursor.fetchall()

        user_data = {

            "id": data[0][0],
            "username": data[0][1],
            "password": data[0][2],
            "first_name": data[0][3],
            "last_name": data[0][4]
        }

        db_connect.close()

        return user_data

    def get_account_by_username(self, user_name):
        """
        Retrieve account data from Account table based on username.

        Returns a Dict with 'id', 'user_id', 'account_type_id', 'balance'

        To retrieve a specific value, you can do it like so:

        Example:

            dbc = DBController()

            foo_balance = dbc.get_account_by_username('foo').get('balance')


        Args:
            user_name: Type[Str]

        Returns:
            Type[Dict] if account is found.

        """

        sql_query_get_account = """SELECT * FROM Account WHERE id = ?"""

        user_id = self.get_user_by_username(user_name).get('id')

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_account, (user_id,))

        data = cursor.fetchall()

        account_data = {

            "id": data[0][0],
            "user_id": data[0][1],
            "account_type_id": data[0][2],
            "balance": data[0][3]

        }

        db_connect.close()

        return account_data

    def get_account_by_user_id(self, user_id):
        """
           Retrieve account data from Account table based on user ID.

           Returns a Dict with 'id', 'user_id', 'account_type_id', 'balance'

           To retrieve a specific value, you can do it like so:

           Example:

               dbc = DBController()

               foo_balance = dbc.get_account_by_user_id(1).get('balance')


           Args:
               user_id: Type[Int]

           Returns:
               Type[Dict] if account is found.

        """

        sql_query_get_account = """SELECT * FROM Account WHERE user_id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_get_account, (user_id,))

        data = cursor.fetchall()

        account_data = {

            "id": data[0][0],
            "user_id": data[0][1],
            "account_type_id": data[0][2],
            "balance": data[0][3]

        }

        db_connect.close()

        return account_data

    def insert_account(self, user_id, account_type, balance):
        """
        Add new account to Account table in bank_app.db

        Args:
            user_id: Type[Int]
            account_type: Type[Int]
            balance: Type[Float]

        Returns:
            None

        """
        new_account_values = (user_id, account_type, balance)

        sql_query_insert_account = """INSERT INTO Account (id, user_id, account_type_id, balance) VALUES (NULL, ?, ?, ?)"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_insert_account, new_account_values)

        db_connect.commit()

        db_connect.close()

    def update_balance(self, user_name, updated_balance):
        """
        Update the balance in a user's bank account.

        NOTE: Does not currently have safeguards implemented.

        Args:
            user_name: Type[Str]
            updated_balance: Type[Float]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        update_balance_values = (updated_balance, user_id)

        sql_query_update_balance = """UPDATE Account SET balance = ? WHERE id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_balance, update_balance_values)

        db_connect.commit()

        db_connect.close()

    def update_password(self, user_name, new_password):
        """
        Update a user's password in the User table.

        NOTE: Does not currently have safeguards.

        Args:
            user_name: Type[Str]
            new_password: Type[Str]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        update_password_values = (new_password, user_id)

        sql_query_update_password = """UPDATE User SET password = ? WHERE id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_password, update_password_values)

        db_connect.commit()

        db_connect.close()

    def update_user_name(self, user_name, new_user_name):
        """
        Update the username.

        Args:
            user_name: Type[Str]
            new_user_name: Type[Str]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        update_username_values = (new_user_name, user_id)

        sql_query_update_username = """UPDATE User SET username = ? WHERE id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_username, update_username_values)

        db_connect.commit()

        db_connect.close()

    def update_first_name(self, user_name, new_first_name):
        """
        Update a user's first name in the User table.

        Args:
            user_name: Type[Str]
            new_first_name: Type[Str]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        update_name_values = (new_first_name, user_id)

        sql_query_update_firstname = """UPDATE User SET first_name = ? WHERE id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_firstname, update_name_values)

        db_connect.commit()

        db_connect.close()

    def update_last_name(self, user_name, new_last_name):
        """
        Update a user's last name in the User table.

        Args:
            user_name: Type[Str]
            new_last_name: Type[Str]

        Returns:
            None

        """
        user_id = self.get_user_by_username(user_name).get('id')

        update_name_values = (new_last_name, user_id)

        sql_query_update_name = """UPDATE User SET last_name = ? WHERE id = ?"""

        db_connect = sqlite3.connect(self.db_path)

        cursor = db_connect.cursor()

        cursor.execute(sql_query_update_name, update_name_values)

        db_connect.commit()

        db_connect.close()
