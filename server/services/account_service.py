from database.db_controller import DBController

'''
Changelog: 
    05/19/24 - hooked up initial account service calls
'''

class AccountService:
    def __init__(self):
        pass

    def get_account (user_id):
        dbc = DBController()
        account_info = dbc.get_account_by_user_id(user_id)
        return account_info

    def view_balance (user_id):
        dbc = DBController()
        account_info = dbc.get_account_by_user_id(user_id)

        if account_info is None:
            raise ValueError('Account could not be found.')

        return account_info.get('balance')

    def deposit (user_id, amount):
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(user_id)

        if account_info is None:
            raise ValueError('Account could not be found.')

        dbc.update_balance(user_id, amount)

    def withdraw (user_id, amount):
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(user_id)

        if account_info is None:
            raise ValueError('Account could not be found.')

        current_balance = account_info.get('balance')

        if (amount > current_balance):
            raise ValueError('The amount exceeds current balance in account')

        dbc.update_balance(user_id, amount * -1)