from models.Buyer import Buyer
from Validation import Validation

class BuyerHasAgreedToTermsValidation(Validation):

    def __init__(self, buyer: Buyer):
        self.__buyer = buyer

    def validate(self) -> bool:
        return self.__buyer.has_agreed_to_terms
