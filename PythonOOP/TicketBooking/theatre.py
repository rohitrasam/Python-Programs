from datetime import datetime
from movie import Movie


class Theatre:

    def __init__(self, name: str, address: str, screens: int) -> None:
        self.name = name
        self.address = address
        self.screens = screens

        self.__movies: list[Movie] = []

    
    def add_movie(self, movie: Movie):
        self.__movies.append(movie)

    
    def schedule(self):
        print(self)
        for movie in self.__movies:
            print(f"{movie}")
        print("="*20)

    def __str__(self) -> str:
        return f'{self.name} - {self.address}'

    

