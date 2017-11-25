from playsound import playsound
from random import shuffle
import sqlite3
import winsound


class Playlist:
    id = 0
    name = ""
    description = ""
    songs = []
    num_of_songs = 0

    def __init__(self, id="", name="", description="", songs=[], num_of_songs=0):
        self.id = id
        self.name = name
        self.description = description
        self.songs = songs
        self.num_of_songs = num_of_songs

    def viewPlaylist(self):
        print "Name: ", self.name
        print self.description
        print "Number of songs: ", self.num_of_songs
        for i in range(0, self.songs.__len__()):
            print i+1,": " , self.songs[i].name, "     ", self.songs[i].length

    def orderPlaylist(self, order="", boolDesc=False):
        if order == "genre":
            self.songs = sorted(self.songs, key=lambda song: song.genre, reverse=boolDesc)
        elif order == "date":
            self.songs = sorted(self.songs, key=lambda song: song.release_date, reverse=boolDesc)
        elif order == "album":
            self.songs = sorted(self.songs, key=lambda song: song.album, reverse=boolDesc)
        elif order == "artist":
            self.songs = sorted(self.songs, key=lambda song: song.artists, reverse=boolDesc)
        elif order == "length":
            self.songs = sorted(self.songs, key=lambda song: song.length, reverse=boolDesc)
        elif order == "shuffle":
            shuffle(self.songs)
        self.viewPlaylist()

    def playPlaylist(self):
        for song in self.songs:
            winsound.PlaySound(song.path, winsound.SND_FILENAME)

    def addToPlaylist(self, songs):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        for song in songs:
            values = [song.id, self.id]
            cur.execute('INSERT INTO song_playlist(song, playlist)\
                                    VALUES(?, ?)', values)
        sql.commit()
        sql.close()

    def addPlaylist(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.name, self.description]
        cur.execute('INSERT INTO playlist(name, description) \
                            VALUES (?, ?)', values)
        res = sql.execute("SELECT MAX(id) from playlist")
        playlistId = 0
        for p in res:
            playlistId = p[0]
        for song in self.songs:
            value = [song.id, playlistId]
            cur.execute('INSERT INTO song_playlist(song, playlist)\
                        VALUES(?, ?)', value)
        sql.commit()
        sql.close()

    def deleteFromPlaylist(self, songs):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        for song in songs:
            values = [self.songs[song - 1].id, self.id]
            print values
            cur.execute('DELETE FROM song_playlist WHERE song = (?) and playlist = (?)', values)
        sql.commit()
        sql.close()
        return 0

    def deletePlaylist(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.id]
        cur.execute('DELETE FROM song_playlist WHERE playlist = (?)', values)
        cur.execute('DELETE FROM playlist WHERE id=(?)', values)
        sql.commit()
        sql.close()
