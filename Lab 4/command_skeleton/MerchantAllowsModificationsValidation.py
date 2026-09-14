from models.Merchant import Merchant
from Validation import Validation

class MerchantAllowsModificationsValidation(Validation):

    def __init__(self, merchant: Merchant):
        self.__merchant = merchant

    def validate(self) -> bool:
        return self.__merchant.allow_modifications
