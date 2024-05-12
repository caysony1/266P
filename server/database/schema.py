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
            last_name TEXT NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS AccountType (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Account (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            account_type_id INTEGER NOT NULL,
            balance INTEGER NOT NULL,
            FOREIGN KEY (account_type_id) REFERENCES AccountType(id),
            FOREIGN KEY (user_id) REFERENCES User(id)
        );
    ''')

    # insert initial records into reference tables
    # have to end with a comma to ensure it is a tuple, not a string
    account_types_records = [
        ('Checking',), 
        ('Savings',)
    ]

    cursor.executemany('INSERT INTO AccountType (name) VALUES (?) ON CONFLICT DO NOTHING;', account_types_records)
    
    db_connection.commit()
    db_connection.close()

    print('Server side database created!')