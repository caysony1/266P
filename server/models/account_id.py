from server.utils.number_utils import is_positive

class AccountId:
    #constructor
    def __init__(self, account_id):
        # perform validations
        if is_positive(account_id) is False:
            raise ValueError('Invalid Account Id detected')
        
        # perform assignments
        self._account_id = account_id

    #accessors
    def get_id(self):
        return self._account_id