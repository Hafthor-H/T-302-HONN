from injector import inject

from core.domain.entities.user import User
from core.application.interfaces.i_user_repository import IUserRepository

class UserService:
    @inject
    def __init__(self, repository: IUserRepository):
        self.__repository = repository

    def get_all(self) -> list[User]:
        return self.__repository.get_all()

    def create_user(self, user: User):
        self.__repository.create_user(user)
