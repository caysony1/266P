import sqlite3
from db_controller import DBController
from services.auth_service import AuthService

'''
THIS IS A TEST FILE

This is just to test database communication and methods etc.

'''
dbc = DBController()

auth = AuthService()

auth.register("admin", 'password1234', 'the', 'administrator', 'admin@admin.io', 100000.00)

auth.register("usertest", 'password5678', 'foo', 'bar', 'foo@bar.io', 55000.50)

print("User table: ")
dbc.inspect_user_table()
print("Account table: ")
dbc.inspect_account_table()
print("Test:")
fetch_balance = dbc.get_account_by_username('admin').get('balance')

print("Admin balance: " + str(fetch_balance))

