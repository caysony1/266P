import sqlite3

def create_db():
    db_connection = sqlite3.connect('bank_app.db')
    cursor = db_connection.cursor()

    # create the necessary tables for the bank application
    cursor.execute('''
        CREATE TABLE User (
            id INTEGER PRIMARY KEY NOT NULL UNIQUE AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE AccountType (
            id INTEGER PRIMARY KEY NOT NULL UNIQUE AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE Account (
            id INTEGER PRIMARY KEY NOT NULL UNIQUE AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            account_type_id INTEGER NOT NULL,
            balance INTEGER NOT NULL,
            FOREIGN_KEY (account_type_id) REFERENCES AccountType(id),
            FOREIGN_KEY (user_id) REFERENCES User(id)
        )
    ''')

    # insert initial records into reference tables
    account_types = [
        ('Checking'),
        ('Savings')
    ]

    cursor.executemany('''
        INSERT INTO AccountType (name)
        VALUES (?)
    ''', account_types)