from database.db_controller import DBController
from models.user_id import UserId
from models.account import Account
from models.transaction_deposit import TransactionDeposit
from models.transaction_withdraw import TransactionWithdraw
from models.account_balance import AccountBalance
from utils.number_utils import round_currency

'''
Changelog:
    06/11/24 - added transaction and account balance models for input validation
    06/09/24 - performed fix phase on account services
    05/19/24 - hooked up initial account service calls
'''

class AccountService:
    def __init__(self, userId: int):
        self._userId = UserId(userId)
        pass

    def get_account (self) -> Account:
        dbc = DBController()
        account_info = dbc.get_account_by_user_id(self._userId.get_id())
        return Account(
            account_info.get('id'), 
            account_info.get('user_id'), 
            account_info.get('balance')
        )

    def view_balance (self) -> float:
        dbc = DBController()
        account_info = dbc.get_account_by_user_id(self._userId.get_id())
        account = Account(account_info.get('id'), account_info.get('user_id'), account_info.get('balance'))
        
        return round_currency(account.account_balance.balance)

    def deposit (self, amount) -> None:
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(self._userId.get_id())
        account = Account(account_info.get('id'), account_info.get('user_id'), account_info.get('balance'))

        current_balance = AccountBalance(round_currency(account.account_balance.balance)).balance
        transaction = TransactionDeposit(account, round_currency(amount))
        currency_amount = transaction.amount
        
        new_balance = current_balance + currency_amount
        dbc.update_balance(self._userId.get_id(), new_balance)

    def withdraw (self, amount) -> None:
        dbc = DBController()

        account_info = dbc.get_account_by_user_id(self._userId.get_id())
        account = Account(account_info.get('id'), account_info.get('user_id'), account_info.get('balance'))

        current_balance = AccountBalance(round_currency(account.account_balance.balance)).balance
        transaction = TransactionWithdraw(account, round_currency(amount))
        currency_amount = transaction.amount

        if (currency_amount > current_balance):
            raise ValueError('The amount exceeds current balance in account')

        new_balance = current_balance - currency_amount
        dbc.update_balance(self._userId.get_id(), new_balance)