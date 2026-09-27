from abc import ABC, abstractmethod

from user.user import User


class IUserRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def create_user(self, user: User) -> None:
        pass