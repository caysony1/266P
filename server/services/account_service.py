from database.db_controller import DBController
from models.user_id import UserId

'''
Changelog: 
    05/19/24 - hooked up initial account service calls
'''

class AccountService:
    def __init__(self, userId: int):
        self._userId = UserId(userId)
        pass

    def get_account (self):
        dbc = DBController()
        account_info = dbc.get_account_by_user_id(self._userId.get_id())
        return account_info

    def view_balance (self):
        dbc = DBController()
        account_info = dbc.get_account_by_user_id(self._userId.get_id())

        if account_info is None:
            raise ValueError('Account could not be found.')

        return account_info.get('balance')

    def deposit (self, amount):
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(self._userId.get_id())

        if account_info is None:
            raise ValueError('Account could not be found.')

        current_balance = float(account_info.get('balance'))
        new_balance = current_balance + float(amount)
        dbc.update_balance(self._userId.get_id(), new_balance)

    def withdraw (self, amount):
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(self._userId.get_id())

        if account_info is None:
            raise ValueError('Account could not be found.')

        current_balance = account_info.get('balance')

        if (amount > current_balance):
            raise ValueError('The amount exceeds current balance in account')

        new_balance = float(current_balance) - float(amount)
        dbc.update_balance(self._userId.get_id(), new_balance)