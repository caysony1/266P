from database.db_controller import DBController
from models.user_id import UserId
from utils.number_utils import round_currency

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

        return round_currency(account_info.get('balance'))

    def deposit (self, amount):
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(self._userId.get_id())

        if account_info is None:
            raise ValueError('Account could not be found.')

        current_balance = round_currency(float(account_info.get('balance')))
        currency_amount = round_currency(amount)
        
        new_balance = current_balance + currency_amount
        dbc.update_balance(self._userId.get_id(), new_balance)

    def withdraw (self, amount):
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(self._userId.get_id())

        if account_info is None:
            raise ValueError('Account could not be found.')

        current_balance = round_currency(float(account_info.get('balance')))
        currency_amount = round_currency(amount)

        if (currency_amount > current_balance):
            raise ValueError('The amount exceeds current balance in account')

        new_balance = current_balance - currency_amount
        dbc.update_balance(self._userId.get_id(), new_balance)