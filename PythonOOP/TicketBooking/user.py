from tickets import Ticket


class Customer:

    def __init__(self, name: str, number: str, email: str) -> None:
        
        self.name = name
        self.email = email
        self.number = number
        self.__bookings = []

    @property
    def bookings(self):
        return self.__bookings
    

    def add_booking(self, booking: Ticket):
        self.__bookings.append(booking)

