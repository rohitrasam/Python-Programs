from random import randint
from theatre import Theatre

class Ticket:

    def __init__(self, customer_name: str, movie_name: str, theatre: Theatre) -> None:
        self.customer_name = customer_name
        self.movie = movie_name
        self.theatre = theatre

        self.__booking_id = str(randint() + "".join([ord(ch) for ch in self.customer_name]))

    @property
    def get_booking_id(self):
        return self.__booking_id 