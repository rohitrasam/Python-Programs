class Song:
    """
    Class to represent a song
    
    Attributes:
    title (str): The title of the song
    artist (Artist): An artist object representing the songs creator.
    duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method
        
        Args:
            title (str): Initialises the 'title' attribute
            artist (Artist): At Artist object representing the song's creator.
            duration (Optional[int]): Initial value for the 'duration' attribute.
                Will default to zero if not specified
        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an Album, using it's track list
    
    Attributes:
        name (str): The name of the album
        year (int): The year an album was released
        artist: (Artist): The artist responsible for the album.
            If no specified, the artist will default to an artist with the name
            "Various Artists".
        tracks (List[Song]): A list of the songs on the album"""

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        self.artist = Artist("Various Artists") if artist == None else artist

        self.tracks = []

    def add_song(self, song, position=None):
        if position == None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:

    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def add_album(self, album):
        self.albums.append(album)



def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open('albums/albums.txt', 'r') as albums:
        for line in albums:
            # row consists of artist, album, year, song
            artist_field, album_field, year_field, song_field = line.strip('\n').split('\t')
            year_field = int(year_field)
            print("|| {} || {} || {} || {}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We've just read details for new artist
                # store the current album in the current artists collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None
            
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # Just read a new album for the current artist
                # store current album in the artist's collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)
            
            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

        # After reading the last line of the text file, we will have an artist and album that haven't been stored - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)

    return artist_list  

def create_checkfile(artists_list):
    with open('albums/checkfile.txt', 'w') as check:
        for new_artist in artists_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=check)                    

if __name__ == '__main__':
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)