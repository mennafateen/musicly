import sqlite3
import ttk
from playsound import playsound
from Tkinter import *
from random import shuffle

# gui
'''
root = Tk()

frame = Frame(root)

Button(frame, text="Click").pack(side=LEFT, fill=Y)
Button(frame, text="Click2").pack(side=TOP, fill=X)
Button(frame, text="Click3").pack(side=RIGHT, fill=X)
Button(frame, text="Click4").pack(side=LEFT, fill=X)
frame.pack()
root.mainloop()
'''

sql = sqlite3.connect('music.db')
cur = sql.cursor()


def loadMusic(songs, playlists, albums, artists, bands):
    #load songs w/ all details
    songRes = sql.execute("SELECT * FROM song")
    for row in songRes:
        artistRes = sql.execute("SELECT * FROM artist_song WHERE song = (?)", (row[0],))
        songArtists = []
        sql.commit()
        for i in artistRes:
            artist = sql.execute("SELECT * FROM artist WHERE id = (?)", (i[0],))
            for j in artist:
                songArtists.append(j[0])
        song = Song(row[0], row[1], row[2], row[3], row[4], row[5], songArtists, row[6], row[7], row[8])

        songs.append(song)
    sql.commit()
    #load all artists
    artistsRes = sql.execute("SELECT * FROM artist")
    for row in artistsRes:
        artistsSongs = []
        for i in songs:
            for j in i.artists:
                if j == row[0]:
                    artistsSongs.append(i)
            if i.band == row[3] and i.band is not None:
                artistsSongs.append(i)
        artst = Artist(row[0], row[1], row[2], row[3], artistsSongs)
        artists.append(artst)
    sql.commit()
    #load all albums
    albumRes = sql.execute("SELECT * FROM album")
    for row in albumRes:
        albumSongs = []
        for i in songs:
            if i.album == row[0]:
                albumSongs.append(i)
        album = Album(row[0], row[1], row[2], row[3], row[4], albumSongs)
        albums.append(album)



    playlistRes = sql.execute("SELECT * FROM playlist")
    for row in playlistRes:
        playlistSongs = []
        songsID = sql.execute("SELECT song FROM song_playlist WHERE playlist = (?)", (row[0],))
        for i in songsID:
            for j in songs:
                if i[0] == j.id:
                    playlistSongs.append(j)
        plylist = Playlist(row[0], row[1], row[2], playlistSongs, playlistSongs.__len__())
        playlists.append(plylist)

    bandRes = sql.execute("SELECT * FROM band")
    for row in bandRes:
        bandArtists = []
        for i in artists:
            if i.band == row[0]:
                bandArtists.append(i)
        bandSongs = []
        for i in songs:
            if i.band == row[0]:
                bandSongs.append(i)
        band = Band(row[0], row[1], bandArtists, bandSongs)
        bands.append(band)

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
    def __init__(self, id, name, release_date, length, genre, album, artists, band, lyrics, path):
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
    def viewSong(self, albums, bands, artists):
        print "Title: ", self.name
        print "Release date: ", self.release_date
        print "Duration: ", self.length
        print "Genre: ", self.genre
        print "Album: ",
        if self.album is not None:
            print albums[self.album - 1].name
        else:
            print self.album
        print "Band: ",
        if self.band is not None:
            print bands[self.band - 1].name
        else:
            print self.band
        print "Artists: "
        for i in self.artists:
            print artists[i - 1].name
        print "Lyrics: ", self.lyrics
      #  playsound(self.path)

class Playlist:
    id = 0
    name = ""
    description = ""
    songs = []
    num_of_songs = 0
    def __init__(self, id, name, description, songs, num_of_songs):
        self.id = id
        self.name = name
        self.description = description
        self.songs = songs
        self.num_of_songs = num_of_songs
    def viewPlaylist(self, order, boolDesc):
        print "Name: ", self.name
        print self.description
        print "Number of songs: ", self.num_of_songs
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
        for song in self.songs:
            print "*", song.name, "     ", song.length
    def playPlaylist(self):
        for song in self.songs:
            playsound(song.path)

class Artist:
    id = 0
    name = ""
    date_of_birth = ""
    band = ""
    songs = []
    def __init__(self, id, name, date_of_birth, band, songs):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.band = band
        self.songs = songs
    def viewArtist(self, bands):
        print "Name: ", self.name
        print "Date of birth: ", self.date_of_birth
        print "Band: ",
        if self.band is not None:
            print bands[self.band - 1].name
        else:
            print self.band
        print "Songs: "
        for song in self.songs:
            print "* ", song.name, "    ", song.length
    def playArtistSongs(self):
        for song in self.songs:
            playsound(song.path)



class Band:
    id = 0
    name = ""
    artists = []
    songs = []
    def __init__(self, id, name, artists, songs):
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
            playsound(song.path)
class Album:
    id = 0
    name = ""
    band = ""
    artist = ""
    num_of_songs = ""
    songs = []
    def __init__(self, id, name, band, artist, num_of_songs, songs):
        self.id = id
        self.name = name
        self.band = band
        self.artist = artist
        self.num_of_songs = num_of_songs
        self.songs = songs
    def viewAlbum(self, artists, bands):
        print "Name: ", self.name
        print "Band: ",
        if self.band is not None:
            print bands[self.band - 1].name
        else:
            print self.band
        print "Artist: ",
        if self.artist is not None:
            print artists[self.artist - 1].name
        else:
            print self.artist
        for song in self.songs:
            print "* ", song.name, "    ", song.length
    def playAlbumSongs(self):
        for song in self.songs:
            playsound(song.path)

def viewPlaylists(playlist):
    print "Name             Num of Songs"
    for i in range(0, playlist.__len__()):
        print i+1, ": ", playlist[i].name, " ", playlist[i].num_of_songs
def viewSongs(songs):
    print "Song         Duration"
    for i in range(0, songs.__len__()):
        print i+1, ": ", songs[i].name, " ", songs[i].length
def viewAlbums(albums):
    print "Name         Num of Songs"
    for i in range(0, albums.__len__()):
        print i+1, ": ", albums[i].name, " ", albums[i].num_of_songs
def viewArtists(artists):
    print "Name"
    for i in range(0, artists.__len__()):
        print i+1, ": ", artists[i].name
def viewBands(bands):
    print "Name"
    for i in range(0, bands.__len__()):
        print i+1, ": ", bands[i].name


def main():
    songs = []
    playlists = []
    albums =[]
    artists = []
    bands = []
    loadMusic(songs, playlists, albums, artists, bands)

    viewPlaylists(playlists)

#    Tkinter._test()
    print "-------------Songs-------------"
    for i in songs:
      #  print i
        i.viewSong(albums, bands, artists)
    print "----------Artists-------------"
    for i in artists:
        print i.viewArtist(bands)
    print "----------------Albums-----------"
    for i in albums:
        i.viewAlbum(artists, bands)
    print "---------------Bands---------------"
    for i in bands:
        i.viewBand()
 #       i.playBandSongs()
    print "--------------Playlists-----------"
    for i in playlists:
        i.viewPlaylist("shuffle", False)
        i.playPlaylist()

main()