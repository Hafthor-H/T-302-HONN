from abc import ABC, abstractmethod
from core.domain.entities.movie import Movie


class IMovieRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[Movie]:
        pass

    @abstractmethod
    def create_movie(self, movie: Movie) -> None:
        pass