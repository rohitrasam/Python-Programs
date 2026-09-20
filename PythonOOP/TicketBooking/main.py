import datetime as dt
from user import Customer
from tickets import Ticket
from theatre import Theatre
from movie import Movie




inox = Theatre("INOX", "Bund Garden", 3)
pvr = Theatre("PVR", "Magarpatta", 5)
cp = Theatre("City Pride", "Satara Road", 4)

animal = Movie("Animal", "3hrs 21min", "loeparoar")
avengers = Movie("Avengers: Endgame", "3hrs", "asdoasd")
inter = Movie("Interstellar", "2hrs 30min", "asdokawq")
# incep = Movie("Inception", "2hrs 40min", "auqoiwejaosd")
# spidey = Movie("Spiderman: No Way Home", "1hr 30min", "p[asdioia]")

inox.add_movie(animal)
inox.add_movie(avengers)
pvr.add_movie(animal)

def main():

    inox.schedule()
    pvr.schedule()


if __name__ == '__main__':
    main()