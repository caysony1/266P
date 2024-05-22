import sqlite3

def create_db():
    db_connection = sqlite3.connect('bank_app.db')
    cursor = db_connection.cursor()

    # create the necessary tables for the bank application
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS User (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            balance INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES User(id)
        );
    ''')

    db_connection.commit()
    db_connection.close()

    print('Server side database created!')