from playsound import playsound
import sqlite3

class Album:
    id = 0
    name = ""
    band = ""
    artist = ""
    num_of_songs = ""
    songs = []
    def __init__(self, id="", name="", band="", artist="", num_of_songs="", songs=[]):
        self.id = id
        self.name = name
        self.band = band
        self.artist = artist
        self.num_of_songs = num_of_songs
        self.songs = songs
    def viewAlbum(self):
        print "Name: ", self.name
        print "Band: ",
        if self.band is not None:
            print self.band.name
        else:
            print self.band
        print "Artist: ",
        if self.artist is not None:
            print self.artist.name
        else:
            print self.artist
        for song in self.songs:
            print "* ", song.name, "    ", song.length
    def playAlbumSongs(self):
        for song in self.songs:
            playsound(song.path)
    def deleteAlbum(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.id]
        cur.execute('DELETE FROM album \
                           WHERE id = (?)', values)
        sql.commit()
        sql.close()
    def addAlbum(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        value = [self.name]
        cur.execute('INSERT INTO album(name) \
                            VALUES (?)', value)
        sql.commit()
        sql.close()
