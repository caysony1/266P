from os.path import join, dirname, abspath
import sqlite3

'''
Changelist: 
    
    05/14/14 - Added and implemented table inspection methods. 
             - Added and implemented insert_user, get_user_by_username, and insert_account methods.
             - Added WIP execute_query_method. Updated docstring format
    05/13/24 - Class created. Blocked out methods.
    
    
'''

class DBController:
    """
    Database controller class to act as a liaison between the database and other app components.

    NOTE:
    DBController methods will open a connection to the bank_app.db, perform operations, then close the connection when finished.

    TODO (kj-art-dev): Continue method introduction and implementation for whatever is needed next.

    """

    def __init__(self):
        """
        Initialize DBController with a path to the local database.

        This path is used to connect to the database using the sqlite3.connect() method.
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
        (WIP)
        Execute a full SQL query on bank_app.db

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
            user_name: Type[String]
            password: Type[String]
            first_name: Type[String]
            last_name: Type[String]

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

        To retrieve a specific value, you can do it in one line like so:

        Examples:

            foo_password = get_user_by_username('admin').get('password')

        Args:
            user_name: Type[String]

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

    def update_balance(self, user, account, updated_balance):
        """
        (WIP) Update the account balance for a user. Can be
        Args:
            user: User-type object
            account: Account-type object
            updated_balance: number as float

        Returns:
            None

        """
        pass

    def update_user_first_name(self, user, first_name):
        """
        (WIP) Update a user's first name in User table in database.

        Args:
            user: User-type object with a user ID
            first_name: New first name as string

        Returns:
            None

        """
        pass

    def update_user_last_name(self, user, last_name):
        """
        (WIP) Update user's last name in Users table in database

            user: User-type object.
            last_name: New last name as string.

        Returns:
            None

        """
        pass
