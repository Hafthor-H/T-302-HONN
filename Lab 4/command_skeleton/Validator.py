from Validation import Validation

class Validator(Validation):

    def __init__(self):
        self.__validations: list[Validation] = []

    def validate(self) -> bool:
        return all(validation.validate() for validation in self.__validations)

    def add_validation(self, validation: Validation) -> None:
        self.__validations.append(validation)
