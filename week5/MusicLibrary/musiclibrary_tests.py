import io
import os
import sys
import unittest
from song import Song
from playlist import Playlist
class TestMusicLibrary(unittest.TestCase):
    def test_song_str(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        expected_result = 'Manowar - Odin from The Sons of Odin - 3:44'
        self.assertEqual(str(s), expected_result)

    def test_song_eq_if_not_equal(self):
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Kingdom Come", artist="Manowar", album="Kings of Metal", length="3:59")
        self.assertFalse(s1==s2)

    def test_song_eq_if_equal(self):
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertTrue(s1==s2)

    def test_length_of_song_in_seconds(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertEqual(s.len(seconds = True), 224)

    def test_length_of_song_in_minutes(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertEqual(s.len(minutes = True), 3)

    def test_length_of_song_in_hours(self):
        s1 = Song(title="very long song", artist="some artist", album="some album", length="1:30:44")
        s2 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertEqual(s1.len(hours = True), 1)
        self.assertEqual(s2.len(hours = True), 0)

    def test_length_of_song_string_representation(self):
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.assertEqual(s.len(), '3:44')

    def test_playlist_add_single_song(self):
        pl = Playlist('test')
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        pl.add_song(s)
        self.assertTrue(s in pl.song_list)

    def test_playlist_add_song_with_no_song_instance(self):
        pl = Playlist('test')
        s = "I'm not a song"
        with self.assertRaises(TypeError) as context:
            pl.add_song(s)
        self.assertTrue('Invalid type of song' in str(context.exception))

    def test_playlist_add_four_songs(self):
        pl = Playlist('test')
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Ohne Dich", artist="Rammstein", album="Reise, Reise", length="1:3:44")
        s3 = Song(title="Ich Will", artist="Rammstein", album="Mutter", length="4:05")
        s4 = Song(title="Ich Tu Dir Weh", artist="Rammstein", album="Liebe ist für alle da", length="3:58")
        list_of_songs = [s1, s2, s3, s4]
        pl.add_songs(list_of_songs)
        self.assertTrue(all([s in pl.song_list for s in list_of_songs]))

    def test_playlist_remove_song(self):
        pl = Playlist('test')
        s = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        pl.add_song(s)
        pl.remove_song(s)
        self.assertFalse(pl.song_list) #the list with songs is empty

    def test_playlist_print(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        pl = Playlist('test')
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Ich Will", artist="Rammstein", album="Mutter", length="4:05")
        s3 = Song(title="Ich Tu Dir Weh", artist="Rammstein", album="Liebe ist für alle da", length="3:58")
        s4 = Song(title="Apologize", artist="One Republic", album="Dreaming Out Loud", length="3:11")
        pl.add_songs([s1, s2, s3, s4])
        expected_output = """|    Artist      |         Song         | Length |
| -------------- |----------------------|--------|
|    Manowar     |         Odin         |  3:44  |
|   Rammstein    |       Ich Will       |  4:05  |
|   Rammstein    |    Ich Tu Dir Weh    |  3:58  |
|  One Republic  |      Apologize       |  3:11  |
"""
        pl.pprint_playlist()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

    def test_playlist_total_length(self):
        pl = Playlist('test')
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Ich Will", artist="Rammstein", album="Mutter", length="4:05")
        s3 = Song(title="Ich Tu Dir Weh", artist="Rammstein", album="Liebe ist für alle da", length="3:58")
        s4 = Song(title="Apologize", artist="One Republic", album="Dreaming Out Loud", length="3:11")
        pl.add_songs([s1, s2, s3, s4])
        self.assertEqual(pl.total_length(), '00:14:58')

    def test_playlist_next_song(self):
        pl = Playlist('test')
        s1 = Song(title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        s2 = Song(title="Ich Will", artist="Rammstein", album="Mutter", length="4:05")
        s3 = Song(title="Ich Tu Dir Weh", artist="Rammstein", album="Liebe ist für alle da", length="3:58")
        pl.add_songs([s1, s2, s3])
        self.assertEqual(pl.next_song(), s2)


if __name__ =='__main__':
    unittest.main()