from models.final import Final
from utils.number_utils import is_positive

class AccountId:
    account_id: int = Final()

    def __init__(self, account_id: int):
        self.account_id = is_positive(account_id)