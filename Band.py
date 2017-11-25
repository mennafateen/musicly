from playsound import playsound
import sqlite3
import winsound


class Band:
    id = 0
    name = ""
    artists = []
    songs = []

    def __init__(self, id="", name="", artists=[], songs=[]):
        self.id = id
        self.name = name
        self.artists = artists
        self.songs = songs

    def viewBand(self):
        print "Name: ", self.name
        print "Artists: ",
        for artist in self.artists:
            print artist.name
        print "Songs: ",
        for song in self.songs:
            print "* ", song.name, "   ", song.length

    def playBandSongs(self):
        for song in self.songs:
            winsound.PlaySound(song.path, winsound.SND_FILENAME)

    def addBand(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        value = [self.name]
        cur.execute('INSERT INTO band(name) \
                    VALUES (?)', value)
        sql.commit()
        sql.close()

    def deleteBand(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.id]
        cur.execute('DELETE FROM band \
                           WHERE id = (?)', values)
        sql.commit()
        sql.close()
        return 0
