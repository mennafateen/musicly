from playsound import playsound
import sqlite3
import winsound


class Artist:
    id = 0
    name = ""
    date_of_birth = ""
    band = ""
    songs = []

    def __init__(self, id=" ", name="", date_of_birth="", band="", songs=[]):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.band = band
        self.songs = songs

    def viewArtist(self):
        print "Name: ", self.name
        print "Date of birth: ", self.date_of_birth
        print "Band: ",
        if self.band is not None:
            print self.band.name
        else:
            print self.band
        print "Songs: "
        for song in self.songs:
            print "* ", song.name, "    ", song.length

    def playArtistSongs(self):
        for song in self.songs:
            winsound.PlaySound(song.path, winsound.SND_FILENAME)

    def addArtist(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.name, self.date_of_birth]
        cur.execute('INSERT INTO artist(name, date_of_birth) \
                    VALUES (?, ?)', values)
        sql.commit()
        sql.close()

    def deleteArtist(self):
        sql = sqlite3.connect('musicly.db')
        cur = sql.cursor()
        values = [self.id]
        cur.execute('DELETE FROM artist \
                           WHERE id = (?)', values)
        sql.commit()
        sql.close()
