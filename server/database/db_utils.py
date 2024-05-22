import sqlite3
from services.auth_service import AuthService


def add_default_accounts():
    """
    Add default dummy accounts to the database

    Returns:
        None
    """

    auth = AuthService()

    auth.register("admin", 'password1234', 'the', 'administrator', 'admin@admin.io', 100000.00)
    auth.register("usertest", 'mynameisfoo', 'foo', 'bar', 'foo@bar.io', 55000.50)
    auth.register("moneyiscool", 'money123', 'beff', 'jezos', 'beff@jezos.io', 2073000001.25)
    auth.register("grandpajoe", 'goldentix', 'joseph', 'bucket', 'jbucket@wonka.io', 0.75)
    auth.register("bank_user_01", 'strongpassword', 'john', 'smith', 'john@smith.io', 75000.25)
    auth.register("bank_user_02", 'evenstrongerpassword', 'jane', 'doe', 'jane@doe.io', 120000.75)
