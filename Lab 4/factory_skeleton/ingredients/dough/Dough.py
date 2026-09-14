from abc import ABC, abstractmethod

class Dough(ABC):
    @abstractmethod
    def __str__(self):
        pass
