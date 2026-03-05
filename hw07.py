"""
DSC 20 Spring 2025 Homework 07
Name: Karina Lopez
PID: A18356687
Source: ChatGPT with raise ValueError()
"""

# Question 1
def type_with_number(message):
    """
    takes in a string and returns the sequence of digits
    you need to press on your phone, as a string
    --
    Parameters:
    message: string
    --
    Returns:
    sequence of digits you need to press on your phone,
    as a string

    >>> type_with_number('Welcome to Beijing!')
    '9352663086023454641'
    >>> type_with_number('I miss my laptop.')
    '40647706905278671'
    >>> type_with_number('!!??..  ,,')
    '1111110011'

    # Add at least 3 doctests below here, DO NOT delete this line #
    >>> type_with_number('')
    ''

    >>> type_with_number('abcdefghijklmnopqrstuvwxyz')
    '22233344455566677778889999'

    >>> type_with_number('Karina is the best lol')
    '5274620470843023780565'
    """
    dict_chars = {
    ',': 1, '.': 1, '?': 1, '!': 1,
    'a': 2, 'b': 2, 'c': 2,
    'd': 3, 'e': 3, 'f': 3,
    'g': 4, 'h': 4, 'i': 4, 
    'j': 5, 'k': 5, 'l': 5, 
    'm': 6, 'n': 6, 'o': 6, 
    'p': 7, 'q': 7, 'r': 7, 's': 7,
    't': 8, 'u': 8, 'v': 8, 
    'w': 9, 'x': 9, 'y': 9, 'z': 9,
    ' ': 0
    }
    if len(message) == 0:
        return ''
    else:
        return str(dict_chars[message[0].lower()])\
         + type_with_number(message[1:])

# Question 2
def make_palindrome(start, stop):
    """
    creates palindrome
    --
    Parameters:
    start: positive int to start with
    stop: positive int at the middle of palindrome
    --
    Returns:
    palindrome as a string

    >>> make_palindrome(1, 1)
    '1'
    >>> make_palindrome(3, 5)
    '34543'
    >>> make_palindrome(5, 2)
    '5432345'

    # Add at least 3 doctests below here, DO NOT delete this line #

    >>> make_palindrome(10, 0)
    '10987654321012345678910'

    >>> make_palindrome(0, 0)
    '0'

    >>> make_palindrome(5, 6)
    '565'
    """
    if start == stop:
        return str(stop)
    elif start < stop:
        return str(start) + make_palindrome(start + 1, stop) + str(start)
    else:
        return str(start) + make_palindrome(start - 1, stop) + str(start)


# Question 3
def doctests_q3():
    """
    >>> my_phone = Phone('Apple', 4000, 64000)
    >>> my_phone.brand
    'Apple'
    >>> my_phone.charge
    2000
    >>> my_phone.num_apps
    0
    >>> my_phone.use(10)
    >>> my_phone.charge
    1900
    >>> my_phone.recharge(10)
    >>> my_phone.charge
    2100
    >>> my_phone.install(1000, 'Spotify')
    'App installed'
    >>> my_phone.apps
    {'Spotify'}
    >>> my_phone.storage
    63000
    >>> my_phone.use(210)
    'Out of charge'
    >>> my_phone.recharge(400)
    >>> my_phone.charge
    4000
    >>> my_phone.install(1000, 'Spotify')
    'App already installed'

    # Add your own doctests below, DO NOT delete this line #

    >>> third_phone = Phone('Nokia', 2000, 32000)
    >>> third_phone.drain_rate
    15
    >>> third_phone.use(133)
    'Out of charge'
    >>> third_phone.recharge(1)
    >>> third_phone.charge
    20
    >>> third_phone.install(500, 'Snake')
    'App installed'
    >>> third_phone.apps
    {'Snake'}

    >>> selfie_phone = Phone('Apple', 5000, 32000)
    >>> selfie_phone.install(5000, 'KarinaCam')
    'App installed'
    >>> selfie_phone.apps
    {'KarinaCam'}

    >>> full_storage_phone = Phone('Apple', 4000, 1000)
    >>> full_storage_phone.install(500, 'Game1')
    'App installed'
    >>> full_storage_phone.install(500, 'Game2')
    'App installed'
    >>> full_storage_phone.install(1, 'Game3')
    'Not enough storage'
    """
    return

class Phone:
    """
    Implementation of Phone
    """
    def __init__(self, brand, max_battery, storage):
        self.brand = brand
        self.max_battery = max_battery
        self.storage = storage
        self.charge = max_battery // 2

        if brand == 'Apple':
            self.drain_rate = 10
        elif brand == 'OnePlus':
            self.drain_rate = 12
        elif brand == 'Samsung':
            self.drain_rate = 8
        else:
            self.drain_rate = 15

        self.charge_rate = 20
        self.num_apps = 0
        self.apps = set()

    def use(self, minutes):
        total_drain = self.drain_rate * minutes
        if total_drain >= self.charge:
            self.charge = 0
            return 'Out of charge'
        else:
            self.charge -= total_drain

    def recharge(self, minutes):
        total_charge = self.charge_rate * minutes
        self.charge = min(self.max_battery, self.charge + total_charge)

    def install(self, app_size, app_name):
        if self.charge == 0:
            return 'Out of charge'
        if app_size > self.storage:
            return 'Not enough storage'
        if app_name in self.apps:
            return 'App already installed'
        else:
            self.storage -= app_size
            self.num_apps += 1
            self.apps.add(app_name)
            return 'App installed'
    pass


################ CLASS PART ##################

# Question 4

def doctests_go_here():
    """
    >>> track1 = Song('More Life', 3.11, 'Just Until...', 'Cordae', 1220980)
    >>> print(track1)
    'More Life' by Cordae on 'Just Until...' is 3.11 minutes\
 long with 1220980 streams
    >>> track1.get_artist()
    'Cordae'
    >>> Song.platform
    'Spotify'
    >>> track1.platform
    'Spotify'
    >>> play1 = Playlist('Rap Caviar', 'James')
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 0 songs
    >>> play1.add_song(track1)
    True
    >>> play1.get_total_streams()
    1220980
    >>> print(play1)
    Playlist 'Rap Caviar' by James has 1 songs
    >>> play1.add_song(track1)
    False
    >>> play1.remove_song(track1)
    True
    
    >>> track2 = Song('Good Days', 4.65, 'Good Days', 'SZA', 276568815)
    >>> track3 = Song('Heat Waves', 3.999, 'Dreamland', 'Glass Animals', 5000)
    >>> play1.add_song(track2)
    True
    >>> play1.add_song(track1)
    True
    >>> play1.add_song(track3)
    True
    >>> track2.add_to_playlist(play1)
    False
    >>> play1.sort_songs('length')
    >>> [x.get_name() for x in play1.get_songs()]
    ['More Life', 'Heat Waves', 'Good Days']
    >>> play1.sort_songs('name')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Good Days', 'Heat Waves', 'More Life']
    >>> play1.sort_songs('streams')
    >>> [x.get_name() for x in play1.get_songs()]
    ['Heat Waves', 'More Life', 'Good Days']
    >>> play1.get_most_played_song()
    'Good Days'
    >>> play1.get_total_streams()
    277794795
    >>> play1.get_total_length()
    11.759
    >>> print(play1.play())
    Listening to 'Heat Waves' by Glass Animals
    Listening to 'More Life' by Cordae
    Listening to 'Good Days' by SZA
    >>> print(track1.listen())
    Listening to 'More Life' by Cordae
    >>> play1.get_total_streams()
    277794799
    >>> play2 = Playlist('Anti Pop', 'Spotify')
    >>> play1.combine_playlists(play2)
    True
    >>> play2.combine_playlists(play1)
    True
    >>> print(play2)
    Playlist 'Anti Pop' by Spotify has 3 songs
    >>> play2.combine_playlists(play1)
    3
    >>> play2.remove_song(track2)
    True
    >>> play2.get_most_played_song()
    'More Life'
    >>> track2.add_to_playlist(play2)
    True
    >>> play2.get_most_played_song()
    'Good Days'
    >>> play3 = Playlist('test', 'ab')
    >>> play3.get_most_played_song()
    ''
    >>> play3.get_total_streams()
    0
    >>> play3.get_total_length()
    0
    >>> play3.sort_songs('length')
    >>> play3.songs
    []
    >>> play2.combine_playlists(play3)
    True

    >>> TS = Song('Shake it Off', 1.23, '1989', 'Taylor Swift', 12345)
    >>> BC = Song('Halo', 2.34, 'I Am... Sasha Fierce', 'Beyoncé', 23456)
    >>> JB = Song('Baby', 3.45, 'Okay', 'Justin Bieber', 34567)
    >>> LG = Song('Bad Romance', 4.53, 'Talk You Back', 'Lady Gaga', 45678)
    >>> AG = Song('Side to Side', 1.01, 'Dangerous Woman',\
 'Ariana Grande', 56432)
    >>> SG = Song('BiggieBig', 3.22, 'The Album', 'Selena Gomez', 987)
    >>> WG = Song('God is Fair', 32.43, 'GOD IS AROUND US',\
 'Windaco God', 99999999)
    >>> BM = Song('Talking to the Moon', 3.38,\
 'Doo-Wops & Hooligans', 'Bruno Mars', 2814901)
    >>> NB = Song('Long Song', 99999.99, 'Billy Boy',\
 'Nobody Billy', 7654321)
    >>> Playlist1 = Playlist('God Spoken!', 'Yes sir')
    >>> Playlist2 = Playlist('Do you still love me if I am DJ', 'Xiaozi')
    >>> Playlist3 = Playlist('Best Song', 'Ye')
    >>> lst = [TS,BC,JB,LG,AG,SG,WG,BM,NB]

    # Add your own doctests below, DO NOT delete this line #

    >>> rauw_song = Song('2:12', 2.12, 'Vice Versa', 'Rauw Alejandro', 300)
    >>> chill_vibes = Playlist('Chill Vibes', 'karina_loves_music')
    >>> chill_vibes.add_song(rauw_song)
    True
    >>> rauw_song.listen()
    "Listening to '2:12' by Rauw Alejandro"
    >>> chill_vibes.get_total_streams()
    301
    >>> chill_vibes.get_total_length()
    2.12
    >>> chill_vibes.play()
    "Listening to '2:12' by Rauw Alejandro"


    >>> ivan_song = Song('Corre', 3.5, 'Dañado', 'Iván Cornejo', 1200000)
    >>> sad_hours = Playlist('Sad Hours', 'karina_crying')
    >>> sad_hours.add_song(ivan_song)
    True
    >>> ivan_song.listen()
    "Listening to 'Corre' by Iván Cornejo"
    >>> sad_hours.get_total_streams()
    1200001
    >>> sad_hours.get_total_length()
    3.5
    >>> print(sad_hours)
    Playlist 'Sad Hours' by karina_crying has 1 songs


    >>> saturno = Song('Saturno', 3.08, 'Viceversa', 'Rauw Alejandro', 9500000)
    >>> karina_playlist = Playlist('Chill Vibes', 'karina')
    >>> karina_playlist.add_song(saturno)
    True
    >>> saturno.get_artist()
    'Rauw Alejandro'
    >>> karina_playlist.get_total_streams()
    9500000
    >>> karina_playlist.play()
    "Listening to 'Saturno' by Rauw Alejandro"
    >>> karina_playlist.remove_song(saturno)
    True
    """
    return


class Song:
    """
    Implementation of a song
    """
    platform = 'Spotify'

    def __init__(self, name, length, album, artist, streams):
        """
        Constructor of Song
        Parameters:
        name (str): name of the song
        length (float): song duration in minutes
        album (str): name of album the song is in
        artist (str): name of artist
        streams (int): number of times the song has been streamed
        """
        if not name:
            raise ValueError('Song name cannot be an empty string')
        if length <= 0:
            raise ValueError('Length must be positive')
        if not album:
            raise ValueError('Album cannot be an empty string')
        if not artist:
            raise ValueError('Artist cannot be an empty string')
        if streams < 0:
            raise ValueError('Streams must be positive')

        self.name = name
        self.length = length
        self.album = album
        self.artist = artist
        self.streams  = streams
        pass


    def get_name(self):
        """ Getter for name attribute """
        return self.name
        pass


    def get_length(self):
        """ Getter for length attribute """
        return self.length
        pass 


    def get_album(self):
        """ Getter for album attribute """
        return self.album
        pass 


    def get_artist(self):
        """ Getter for artist attribute """
        return self.artist
        pass 


    def get_streams(self):
        """ Getter for streams attribute """
        return self.streams
        pass


    def __str__(self):
        """
        String representation of Song
        """
        return f"'{self.get_name()}' by {self.get_artist()}\
 on '{self.get_album()}' is {self.get_length()}\
 minutes long with {self.get_streams()} streams"
        pass


    def listen(self):
        """
        Listens to the song, increasing the stream counter.
        Returns a string with the song name and artist
        """
        self.streams += 1
        return f"Listening to '{self.get_name()}'\
 by {self.get_artist()}"
        pass


    def add_to_playlist(self, playlist):
        """
        Takes a Playlist object and adds the current Song instance into it.
        return True if successful
        return False if song is already included in playlist
        """
        return playlist.add_song(self)
        pass

# Question 5

class Playlist:
    """
    Implementation of a playlist
    """

    def __init__(self, title, user):
        """
        Constructor of Playlist
        Parameters:
        title (str): title of the playlist
        user (str): username of user who created playlist
        Attributes:
        songs (list): list used to store songs in playlist
        """
        assert isinstance(title, str) and title != ''
        assert isinstance(user, str) and user != ''
        self.title = title
        self.user = user
        self.songs = []
        pass


    def get_title(self):
        """ Getter for title attribute """
        return self.title
        pass 


    def get_user(self):
        """ Getter for user attribute """
        return self.user
        pass 
    

    def get_songs(self):
        """ Getter for songs attribute """
        return self.songs
        pass 


    def __str__(self):
        """
        String representation of Playlist
        """
        return f"Playlist '{self.get_title()}'\
 by {self.get_user()} has {len(self.get_songs())} songs"
        pass 


    def add_song(self, song):
        """
        Adds song to list
        return True if successful
        return False if song is already included in playlist
        """
        assert isinstance(song, Song)

        if song in self.songs:
            return False
        else: 
            self.songs.append(song)
            return True
        pass


    def remove_song(self, song):
        """
        Removes a song from the list
        return True if successful
        return False if song is not in the playlist
        """
        assert isinstance(song, Song)

        if song in self.songs:
            self.songs = [s for s in self.songs if s != song]
            return True
        else:
            return False
        pass


    def sort_songs(self, sort_by):
        """
        Sorts the songs by the sort_by attribute in ascending order
        """
        assert isinstance(sort_by, str)
        self.songs.sort(key=lambda song: getattr(song, sort_by))
        pass


    def get_total_streams(self):
        """
        Returns the total amount of streams of the songs in the playlist
        """
        return sum([song.get_streams() for song in self.songs])
        pass


    def get_total_length(self):
        """
        Returns the total length of the playlist
        """
        return sum([song.get_length() for song in self.songs])
        pass


    def play(self):
        """
        Plays every song in the playlist.
        Returns a string that records all the songs played.
        If the playlist is empty, return "Empty"
        """
        if not self.songs:
            return "Empty"
        return '\n'.join([song.listen() for song in self.songs])
        pass
    

    def combine_playlists(self, other_playlist):
        """
        Add all songs from other_playlist to current playlist.
        If all songs were added successfully, return True. 
        If not, return the number of songs that weren't added.
        """
        assert isinstance(other_playlist, Playlist)
        not_added = sum(not self.add_song(song)\
         for song in other_playlist.get_songs())
        return not_added or True
        pass
    

    def get_most_played_song(self):
        """
        Return the name of the most played song
        """
        if not self.songs:
            return ""
        else:
            return max(self.songs, key=lambda song:\
             song.get_streams()).get_name()
        pass