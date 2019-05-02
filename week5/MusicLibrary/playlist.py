import json
import numpy as numpy
import matplotlib.pyplot as plt
from random import shuffle
from song import Song
class Playlist:
    def __init__(self, name, repeat=False, shuffle=False):
        #everything in song_list should be of class Song
        self.name = name
        self.song_list = []
        self.repeat = repeat
        self.Shuffle = shuffle
        self.number_songs = 0
        self.curr_playing_index = 0

    def __len__(self):
        return self.number_songs

    def __getitem__(self,index):
        return self.song_list[index]

    def __setitem__(self,index,value):
        self.song_list[index] = value

    def add_song(self, song):
        if type(song)!=Song:
            raise TypeError('Invalid type of song')
        if self.number_songs == 0:
            self.curr_playing_index = 0

        self.song_list.append(song)
        self.number_songs+=1

    def remove_song(self, song):
        self.song_list.remove(song)
        self.number_songs-=1

    def add_songs(self, songs):
        for song in songs:
            if isinstance(song, Song):
                self.song_list.append(song)
                self.number_songs+=1

    def total_length(self):
        total_len = 0
        for song in self.song_list:
            total_len+=song.len(seconds=True)

        hours = total_len//3600
        minutes = total_len//60%60
        seconds = total_len%60
        return "%02d:%02d:%02d" % (hours, minutes, seconds)

    def artists(self):
        #dictionary, containing artist and number of its songs in playlist
        all_artists = {}
        for song in self.song_list:
            if song.artist in all_artists:
                #increase number of findings
                all_artists[song.artist] += 1
            else:
                all_artists[song.artist] = 1

        width = 0.3
        #scale.limit_range_for_scale(0, len(all_artists.values()), 1)
        plt.bar(all_artists.keys(), all_artists.values(), width, color = (0.2, 0.4, 0.6, 0.6))
        plt.show()

    def next_song(self):
        if self.Shuffle:
            self.shuff()
        if self.repeat == False and self.curr_playing_index+1==self.number_songs:
            return IndexError('End of your playlist. No more songs to show.')
        elif self.repeat == True and self.curr_playing_index+1==self.number_songs:
            self.curr_playing_index = 0
        else:
            self.curr_playing_index+=1
        return self.song_list[self.curr_playing_index]

    def shuff(self):
        #the part that is still not played will be shuffled
        #because we want to play only songs which are still not played
        to_shuffle = self.song_list[self.curr_playing_index+1:]
        shuffle(to_shuffle)
        self.song_list = self.song_list[0:self.curr_playing_index+1] + to_shuffle


    def pprint_playlist(self):
        print("""|    Artist      |         Song         | Length |
| -------------- |----------------------|--------|""")
        for song in self.song_list:
            print('| {:^14} | {:^20} | {:^6} |'.format(song.artist, song.title, song.length))

    def save(self):
        name = self.name
        name.replace(' ', '-')
        name+='.json'
        print(name)
        playlist_info = { 'name': self.name, 
        "song_list": [song.__dict__ for song in self.song_list],
        "repeat": self.repeat,
        "shuffle": self.Shuffle, 
        "number_songs":self.number_songs }

        with open(name, 'w') as plst:
            json.dump(playlist_info, plst, indent=4)

    @staticmethod
    def load(path):
        with open(path, "r") as read_file:
            playlist_info = json.load(read_file)
            pl = Playlist(playlist_info['name'])
            pl.song_list=[]
            for song in playlist_info['song_list']:
                new_song = Song(title=song['title'], artist=song['artist'], album=song['album'], length=song['length'])
                pl.song_list.append(new_song)

            pl.repeat = playlist_info['repeat']
            pl.Shuffle = playlist_info['shuffle']
            pl.number_songs = playlist_info['number_songs']

        return pl

        