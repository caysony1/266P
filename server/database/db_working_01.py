from os.path import join, dirname, abspath
import sqlite3
from db_controller import DBController

# This will construct the path of the database in the project directory.
# db_path = join(dirname(dirname(abspath(__file__))), 'bank_app.db')
#
# db_connect = sqlite3.connect(db_path)
#
# cursor = db_connect.cursor()
#
# sql_query_test_01 = """SELECT name FROM sqlite_master
#   WHERE type='table';"""
#
# cursor.execute(sql_query_test_01)
#
# print(cursor.fetchall())
#
# db_connect.close()

dbc = DBController()


# dbc.insert_user("admin", "admin", "admin", "admin")

dbc.inspect_user_table()
