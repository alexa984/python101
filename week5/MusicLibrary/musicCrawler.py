#creates playlists and songs objects from mp3-s
import mutagen
import json
from os import listdir, path

class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        #craws all the files and returns a new playlist full of songs.
        dir_list = listdir(self.path)
        songs_dict = {}
        songs_dict['name'] = path.basename(self.path)
        songs_dict['shuffle'] = False
        songs_dict['repeat'] = False
        songs_dict['song_list'] = []
        #add to json so it is easier to be loaded later
        for file in dir_list:
            file_info = mutagen.File(file)
            song = Song(file_info['title'], file_info['artist'], file_info['album'], length)


