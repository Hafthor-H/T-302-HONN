from injector import inject

from movie.i_movie_repository import IMovieRepository
from movie.movie import Movie


class MovieService:
    @inject
    def __init__(self, repository: IMovieRepository):
        self.__repository = repository

    def get_all(self) -> list[Movie]:
        return self.__repository.get_all()

    def create_movie(self, movie: Movie) -> None:
        self.__repository.create_movie(movie)
