from utils.number_utils import is_positive

class AccountId:
    #constructor
    def __init__(self, account_id):
        self._account_id = is_positive(account_id)

    #accessors
    def get_id(self):
        return self._account_id