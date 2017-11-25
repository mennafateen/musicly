from playsound import playsound
import sqlite3
import winsound


class Song:
    id = 0
    name = ""
    release_date = ""
    artists = []
    album = ""
    band = ""
    genre = ""
    length = ""
    lyrics = ""
    path = ""

    def __init__(self, id="", name="", release_date="", length="", genre="", album="", artists=[], band="", lyrics="",
                 path=""):
        self.id = id
        self.name = name
        self.release_date = release_date
        self.lyrics = lyrics
        self.length = length
        self.genre = genre
        self.album = album
        self.artists = artists
        self.band = band
        self.path = path

    def viewSong(self):
        print "Title: ", self.name
        print "Release date: ", self.release_date
        print "Duration: ", self.length
        print "Genre: ", self.genre
        print "Album: ", self.album.name
        # if self.album is not None:
        #     print albums[self.album - 1].name
        # else:
        #     print self.album
        print "Band: ", self.band.name
        # if self.band is not None:
        #     print bands[self.band - 1].name
        # else:
        #     print self.band
        print "Artists: "
        for i in self.artists:
            print i.name
        print "Lyrics: ", self.lyrics
        #  playsound(self.path)

    def playSong(self):
        winsound.PlaySound(self.path, winsound.SND_FILENAME)

    def deleteSong(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.id]
        cur.execute('DELETE FROM song WHERE id = (?)', values)
        cur.execute('DELETE FROM song_playlist WHERE song =(?)', values)
        cur.execute('DELETE FROM artist_song WHERE song = (?)', values)
        sql.commit()
        sql.close()
        return 0

    def addSong(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.name, self.release_date, self.genre, self.length, self.lyrics, self.path]
        cur.execute('INSERT INTO song(name, release_date, genre, length, lyrics, path) \
                    VALUES(?,?,?,?,?,?)', values)
        sql.commit()
        sql.close()
