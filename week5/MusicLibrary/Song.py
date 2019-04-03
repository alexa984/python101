import datetime
import math
import time
class Song:
    def __init__(self, **kwargs):
        possible_kwargs = {"title", "artist", "album", "length"}
        if all([str(k) in possible_kwargs for k in kwargs.keys()]) and self.validate_data(kwargs):
            for k, v in kwargs.items():
                self.__dict__[k] = v
        else:
            raise AttributeError()

    def __repr__(self):
        return str(self.title) + ' ' + str(self.artist)

    def __str__(self):
        return "{0} - {1} from {2} - {3}".format(self.artist, self.title, self.album, self.length)

    def __eq__(self, other):
        if self.artist==other.artist and self.title == other.title and self.album == other.album and self.length == other.length:
            return True
        return False

    def __lt__(self, other):
        if self.name < other.name:
            return True

    def __iter__(self):
        self.n = 0
        self.curr = 1
        return self

    def __next__(self):
        if self.n < self.curr:
            self.n += 1
            self.curr = 1
            return self.n
        else:
            raise StopIteration

    def __setitem__(self, index, value):
        self.my_list[index] = value

    def __getitem__(self, index):
        return self.my_list[index]

    def __hash__(self):
        my_hash = math.fabs(hash(self.title)*hash(self.album) + hash(self.artist) + hash(self.length)//17)
        return int(my_hash)

    def len(self, seconds = False, minutes = False, hours = False):
        if any([seconds, minutes, hours]):
            try:
                my_time = time.strptime(self.length, '%M:%S')
                my_time_in_sec = my_time.tm_sec + my_time.tm_min*60
            except ValueError:
                #then the format is h:m:s
                my_time = time.strptime(self.length, '%H:%M:%S')
                my_time_in_sec = my_time.tm_sec + my_time.tm_min*60 + my_time.tm_hour*3600
            if seconds:
                return my_time_in_sec
            elif minutes:
                return my_time_in_sec//60
            else:
                return my_time_in_sec//3600

        return self.length

    @staticmethod
    def validate_data(data):
        if type(data['title'])!=str:
            return False
        if type(data['artist'])!=str:
            return False
        if type(data['album'])!=str:
            return False
        try:
            datetime.datetime.strptime(data['length'], '%H:%M:%S')
        except ValueError:
            try: 
                datetime.datetime.strptime(data['length'], '%M:%S')
            except:
                raise ValueError('Wrong length format for the song!')

        return True

