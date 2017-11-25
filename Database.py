from Playlist import Playlist
from Song import Song
from Album import Album
from Artist import Artist
from Band import Band
import sqlite3

sql = sqlite3.connect('musicly.db')
cur = sql.cursor()


def getSongs():
    songs = []
    songRes = sql.execute("SELECT * FROM song")
    for row in songRes:
        artistRes = sql.execute("SELECT * FROM artist_song WHERE song = (?)", (row[0],))
        songArtists = []
        sql.commit()
        for i in artistRes:
            artist = sql.execute("SELECT * FROM artist WHERE id = (?)", (i[0],))
            for j in artist:
                # songArtists.append(j[0]) # create artist obj #old
                songArtist = Artist(id=j[0], name=j[1], date_of_birth=j[2], band=j[3])
                songArtists.append(songArtist)
        bandRes = sql.execute("SELECT * FROM band WHERE id = (?)", (row[6],))
        songBand = Band()
        for i in bandRes:
            songBand = Band(id=i[0], name=i[1])
        albumRes = sql.execute("SELECT * FROM album WHERE id = (?)", (row[5],))
        songAlbum = Album()
        for i in albumRes:
            songAlbum = Album(id=i[0], name=i[1])
        song = Song(row[0], row[1], row[2], row[3], row[4], songAlbum, songArtists, songBand, row[7], row[8])
        songs.append(song)
    sql.commit()
    return songs


def getArtists():
    artists = []
    artistsRes = sql.execute("SELECT * FROM artist")
    for row in artistsRes:
        # for i in row:
        artistBand = Band()
        bandRes = sql.execute("SELECT * FROM band WHERE id=(?)", (row[3],))
        for i in bandRes:
            artistBand = Band(id=i[0], name=i[1])
        artistsSongs = []
        songs = getSongs()
        for i in songs:
            for j in i.artists:
                if j.id == row[0]:
                    artistsSongs.append(i)
            if i.band.id == row[3] and i.band is not None:
                artistsSongs.append(i)
        artist = Artist(row[0], row[1], row[2], artistBand, artistsSongs)
        artists.append(artist)
    sql.commit()
    return artists


def getBands():
    bands = []
    bandRes = sql.execute("SELECT * FROM band")
    for row in bandRes:
        bandArtists = []
        artists = getArtists()
        for i in artists:
            if i.band.id == row[0]:
                bandArtists.append(i)
        bandSongs = []
        songs = getSongs()
        for i in songs:
            if i.band.id == row[0]:
                bandSongs.append(i)
        band = Band(row[0], row[1], bandArtists, bandSongs)
        bands.append(band)
    return bands


def getAlbums():
    albums = []
    songs = getSongs()
    bands = getBands()
    artists = getArtists()
    albumRes = sql.execute("SELECT * FROM album")
    for row in albumRes:
        albumSongs = []
        albumArtist = Artist()
        albumBand = Band()
        for i in songs:
            if i.album.id == row[0]:
                albumSongs.append(i)
        for i in bands:
            if i.id == row[2]:
                albumBand = i
        for i in artists:
            if i.id == row[3]:
                albumArtist = i
        album = Album(row[0], row[1], albumBand, albumArtist, row[4], albumSongs)
        albums.append(album)

    return albums


def getPlaylists():
    playlists = []
    songs = getSongs()
    playlistRes = sql.execute("SELECT * FROM playlist")
    for row in playlistRes:
        playlistSongs = []
        songsID = sql.execute("SELECT song FROM song_playlist WHERE playlist = (?)", (row[0],))
        for i in songsID:
            for j in songs:
                if i[0] == j.id:
                    playlistSongs.append(j)
        playlist = Playlist(row[0], row[1], row[2], playlistSongs, playlistSongs.__len__())
        playlists.append(playlist)
    return playlists
