import sqlite3
from playsound import playsound
from random import shuffle
from Song import Song
from Album import Album
from Band import Band
from Artist import Artist
from Playlist import Playlist
import sys
from PyQt4 import QtGui, QtCore
import Database
import winsound


def viewPlaylists(playlist):
    print "---------------------"
    for i in range(0, playlist.__len__()):
        print i + 1, ": ", playlist[i].name, " # of songs: ", playlist[i].num_of_songs
    print "---------------------"


def viewSongs(songs):
    print "---------------------"
    for i in range(0, songs.__len__()):
        print i + 1, ": ", songs[i].name, " Duration: ", songs[i].length
    print "---------------------"

def viewAlbums(albums):
    print "---------------------"
    for i in range(0, albums.__len__()):
        print i + 1, ": ", albums[i].name, " ", albums[i].num_of_songs
    print "---------------------"


def viewArtists(artists):
    print "---------------------"
    print "Name"
    for i in range(0, artists.__len__()):
        print i + 1, ": ", artists[i].name, artists[i].band.name
    print "---------------------"

def viewBands(bands):
    print "---------------------"
    print "Name"
    for i in range(0, bands.__len__()):
        print i + 1, ": ", bands[i].name
    print "---------------------"

# gui
'''
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Window(QtGui.QMainWindow):
    songs = []
    playlists = []
    albums = []
    artists = []
    bands = []
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(450,250,400,200)
        self.setWindowTitle("Musicly")
        self.setWindowIcon(QtGui.QIcon('imgs/musicly.png'))
/
        extractAction = QtGui.QAction("&blah", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave app')
        extractAction.triggered.connect(self.close_application)

        self.statusBar()

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(extractAction)

        loadMusic(self.songs, self.playlists, self.albums, self.artists, self.bands)
        self.home()


    def home(self):
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)

        self.table = QtGui.QTableWidget(self)
        playlistBtn = QtGui.QPushButton("Playlists",self)
        playlistBtn.clicked.connect(self.viewPlaylists2)
        playlistBtn.setFont(font)
        playlistBtn.resize(playlistBtn.sizeHint())
        playlistBtn.move(50,50)

        albumBtn = QtGui.QPushButton("Albums", self)
        albumBtn.clicked.connect(self.close_application)
        albumBtn.setFont(font)
        albumBtn.resize(albumBtn.sizeHint())
        albumBtn.move(250, 50)

        artistBtn = QtGui.QPushButton("Artists", self)
        artistBtn.clicked.connect(self.close_application)
        artistBtn.setFont(font)
        artistBtn.resize(artistBtn.sizeHint())
        artistBtn.move(50, 100)

        bandBtn = QtGui.QPushButton("Bands", self)
        bandBtn.clicked.connect(self.close_application)
        bandBtn.setFont(font)
        bandBtn.resize(bandBtn.sizeHint())
        bandBtn.move(250, 100)
        print "ehhd"
        songBtn = QtGui.QPushButton("Songs", self)
        songBtn.clicked.connect(self.close_application)
        songBtn.setFont(font)
        songBtn.resize(songBtn.sizeHint())
        songBtn.move(50, 150)
        print "heh"
        btn = QtGui.QPushButton("Quit", self)
        btn.clicked.connect(self.close_application)
        btn.setFont(font)
        btn.resize(btn.sizeHint())
        btn.move(250, 150)
        print "wefw"
        self.show()

    def viewPlaylists2(self):
        tableHeaders = ["Name", "# of Tracks"]
        self.table.setHorizontalHeaderLabels(tableHeaders)
        for j in range(self.playlists.__len__()):
            name = self.playlists[j].name
            print name
            num_of_songs = self.playlists[j].num_of_songs
            newname = QtGui.QTableWidgetItem(name)
            newnum = QtGui.QTableWidgetItem(num_of_songs)
            self.table.setItem(j, 0, newname)
            self.table.setItem(j, 1, newnum)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
#        self.table.setGeometry(100,100, 500, 500)
 #       self.show()
        
        for i in self.songs:
            btn = QtGui.QPushButton(i.name, self)
            label = QtGui.QLabel(i.name)
            label.setText(i.name)
            label.show()

            btn.move(250, 70)


    def close_application(self):
        sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()
'''


def home():
    print "Welcome to Musicly!"
    print "1 - Playlists"
    print "2 - Albums"
    print "3 - Artists"
    print "4 - Songs"
    print "5 - Bands"
    print "6- Quit"
    choice = int(raw_input("Enter choice: "))
    if choice == 1:
        playlistsView()
    elif choice == 2:
        albumsView()
    elif choice == 3:
        artistsView()
    elif choice == 4:
        songsView()
    elif choice == 5:
        bandsView()


def playlistsView():
    done = False
    while not done:
        playlists = Database.getPlaylists()
        songs = Database.getSongs()
        viewPlaylists(playlists)
        print "1- View Playlist"
        print "2- Add Playlist"
        print "3- Delete Playlist"
        print "4- Home"
        print "5- Quit"
        choice = int(raw_input("Enter choice: "))
        if choice == 5:
            done = True
        if choice == 4:
            done = True
            home()
        elif choice == 1:  # view a specific playlist
            playlistChoice = int(raw_input("Enter playlist id: "))
            if playlistChoice > playlists.__len__():
                print("Invalid playlist ID")
            else:
                view = True
                while view:
                    playlists = Database.getPlaylists()
                    currentPlaylist = playlists[playlistChoice - 1]
                    print "---------------------"
                    currentPlaylist.viewPlaylist()
                    print "---------------------"
                    print("1- Reorder")
                    print("2- Shuffle")
                    print("3- Play")
                    print("4- Delete songs")
                    print("5- Add songs")
                    print("6- Back")
                    viewChoice = int(raw_input("Enter choice: "))
                    if viewChoice == 1:
                        print("Order by: ")
                        print("1- Genre 2- Date 3- Album 4- Artist 5- Length")
                        orderChoice = int(raw_input("Enter choice: "))
                        aOrD = int(raw_input("1- Ascending? 2- Descending? "))
                        desc = False
                        if aOrD == 2:
                            desc = True
                        if orderChoice == 1:
                            currentPlaylist.orderPlaylist("genre", desc)
                        elif orderChoice == 2:
                            currentPlaylist.orderPlaylist("date", desc)
                        elif orderChoice == 3:
                            currentPlaylist.orderPlaylist("album", desc)
                        elif orderChoice == 4:
                            currentPlaylist.orderPlaylist("artist", desc)
                        elif orderChoice == 5:
                            currentPlaylist.orderPlaylist("length", desc)
                    elif viewChoice == 2:
                        currentPlaylist.orderPlaylist("shuffle")
                    elif viewChoice == 3:
                        currentPlaylist.playPlaylist()
                        stop = raw_input("To stop enter 'q': ")
                        if stop == "q":
                            winsound.PlaySound(None, winsound.SND_FILENAME)
                    elif viewChoice == 4:
                        deleteMore = True
                        songsToDelete = []
                        while deleteMore:
                            deleteID = int(raw_input("Enter song ID to delete: "))
                            if deleteID > currentPlaylist.songs.__len__():
                                print("Invalid song ID")
                            else:
                                deleteConfirm = int(
                                    raw_input("Are you sure you want to delete this song? 1- Yes 2- No"))
                                if deleteConfirm == 1:
                                    songsToDelete.append(deleteID)
                            moreConfirm = int(raw_input("Delete more? 1- Yes 2- No"))
                            if moreConfirm == 2:
                                currentPlaylist.deleteFromPlaylist(songsToDelete)
                                deleteMore = False
                    elif viewChoice == 5:
                        addMore = True
                        songsToAdd = []
                        while addMore:
                            viewSongs(songs)
                            songChoice = int(raw_input("Enter song ID to add: "))
                            if songChoice > songs.__len__():
                                print ("Invalid song ID")
                            else:
                                songsToAdd.append(songs[songChoice - 1])
                            moreConfirm = int(raw_input("Add more songs? 1- Yes 2- No"))
                            if moreConfirm == 2:
                                currentPlaylist.addToPlaylist(songsToAdd)
                                addMore = False

                    elif viewChoice == 6:
                        view = False

        elif choice == 2:  # add playlist
            name = raw_input("Enter playlist name: ")
            description = raw_input("Enter playlist description: ")
            addSongs = True
            playlistSongs = []
            while addSongs:
                viewSongs(songs)
                songID = int(raw_input("Enter song id:"))
                if songID > songs.__len__():
                    print("Invalid song id")
                else:
                    playlistSongs.append(songs[songID - 1])
                new = int(raw_input("Enter another song? 1 - Yes 2 - No: "))
                if (new == 2):
                    addSongs = False
            p = Playlist(name=name, description=description, songs=playlistSongs, num_of_songs=playlistSongs.__len__())
            p.addPlaylist()
        elif choice == 3:  # delete playlist
            playlistID = int(raw_input("Enter playlist ID to delete: "))
            if playlistID > playlists.__len__():
                print("Invalid playlist ID")
            else:
                playlistToDelete = playlists[playlistID - 1]
            deleteChoice = int(raw_input("Are you sure you want to delete? 1- Yes 2- No: "))
            if deleteChoice == 1:
                deleted = playlistToDelete.deletePlaylist()
                if deleted == 0:
                    print ("Playlist successfully deleted.")


def albumsView():
    done = False
    while not done:
        albums = Database.getAlbums()
        viewAlbums(albums)
        print "1- View Album"
        print "2- Add Album"
        print "3- Delete Album"
        print "4- Home"
        print "5- Quit"
        choice = int(raw_input("Enter choice: "))
        if choice == 5:
            done = True
        if choice == 4:
            done = True
            home()
        elif choice == 1:  # view a specific album
            albumChoice = int(raw_input("Enter album id: "))
            if albumChoice > albums.__len__():
                print("Invalid album ID")
            else:
                currentAlbum = albums[albumChoice - 1]
                print "---------------------"
                currentAlbum.viewAlbum()
                print "---------------------"
                view = int(raw_input("1- Play 2- Back"))
                if view == 1:
                    currentAlbum.playAlbumSongs()
        elif choice == 2:  # add album
            name = raw_input("Enter album's name: ")
            newAlbum = Album(name=name)
            newAlbum.addAlbum()
        elif choice == 3:  # delete album
            albumID = int(raw_input("Enter album ID to delete: "))
            if albumID > albums.__len__():
                print("Invalid album ID")
            else:
                albumToDelete = albums[albumID - 1]
            deleteChoice = int(raw_input("Are you sure you want to delete? 1- Yes 2- No: "))
            if deleteChoice == 1:
                deleted = albumToDelete.deleteAlbum()
                if deleted == 0:
                    print ("Album successfully deleted.")


def artistsView():
    done = False
    while not done:
        artists = Database.getArtists()
        viewArtists(artists)
        print "1- View Artist"
        print "2- Add Artist"
        print "3- Delete Artist"
        print "4- Home"
        print "5- Quit"
        choice = int(raw_input("Enter choice: "))
        if choice == 5:
            done = True
        if choice == 4:
            done = True
            home()
        elif choice == 1:  # view a specific artist
            artistChoice = int(raw_input("Enter artist id: "))
            if artistChoice > artists.__len__():
                print("Invalid artist ID")
            else:
                currentArtist = artists[artistChoice - 1]
                print "---------------------"
                currentArtist.viewArtist()
                print "---------------------"
                view = int(raw_input("1- Play 2- Back"))
                if view == 1:
                    currentArtist.playArtistSongs()
        elif choice == 2:  # add artist
            name = raw_input("Enter artist's name: ")
            dob = raw_input("Enter artist's date of birth: ")
            newArtist = Artist(name=name, date_of_birth=dob)
            newArtist.addArtist()
        elif choice == 3:  # delete artist
            artistID = int(raw_input("Enter artist ID to delete: "))
            if artistID > artists.__len__():
                print("Invalid artist ID")
            else:
                artistToDelete = artists[artistID - 1]
            deleteChoice = int(raw_input("Are you sure you want to delete? 1- Yes 2- No: "))
            if deleteChoice == 1:
                deleted = artistToDelete.deleteArtist()
                if deleted == 0:
                    print ("Artist successfully deleted.")


def songsView():
    done = False
    while not done:
        songs = Database.getSongs()
        viewSongs(songs)
        print "1- View Song"
        print "2- Add Song"
        print "3- Delete Song"
        print "4- Home"
        print "5- Quit"
        choice = int(raw_input("Enter choice: "))
        if choice == 5:
            done = True
        if choice == 4:
            done = True
            home()
        elif choice == 1:  # view a specific song
            songChoice = int(raw_input("Enter song id: "))
            if songChoice > songs.__len__():
                print("Invalid song ID")
            else:
                currentSong = songs[songChoice - 1]
                print "---------------------"
                currentSong.viewSong()
                print "---------------------"
                view = int(raw_input("1- Play 2- Back"))
                if view == 1:
                    currentSong.playSong()
        elif choice == 2:  # add song
            name = raw_input("Enter song's name: ")
            release_date = raw_input("Enter song's release date: ")
            genre = raw_input("Enter song's genre: ")
            length = raw_input("Enter song's length: ")
            lyrics = raw_input("Enter song's lyrics: ")
            path = raw_input("Enter song's path: ")

            newSong = Song(name=name, release_date=release_date, genre=genre, length=length, lyrics=lyrics, path=path)
            newSong.addSong()
        elif choice == 3:  # delete song
            songID = int(raw_input("Enter song ID to delete: "))
            if songID > songs.__len__():
                print("Invalid song ID")
            else:
                songToDelete = songs[songID - 1]
            deleteChoice = int(raw_input("Are you sure you want to delete? 1- Yes 2- No: "))
            if deleteChoice == 1:
                deleted = songToDelete.deleteSong()
                if deleted == 0:
                    print ("Song successfully deleted.")


def bandsView():
    done = False
    while not done:
        bands = Database.getBands()
        songs = Database.getSongs()
        viewBands(bands)
        print "1- View Band"
        print "2- Add Band"
        print "3- Delete Band"
        print "4- Home"
        print "5- Quit"
        choice = int(raw_input("Enter choice: "))
        if choice == 5:
            done = True
        if choice == 4:
            done = True
            home()
        elif choice == 1:  # view a specific band
            bandChoice = int(raw_input("Enter band id: "))
            if bandChoice > bands.__len__():
                print("Invalid band ID")
            else:
                currentBand = bands[bandChoice - 1]
                print "---------------------"
                currentBand.viewBand()
                print "---------------------"
                view = int(raw_input("1- Play 2- Back"))
                if view == 1:
                    currentBand.playBandSongs()
        elif choice == 2:  # add band
            name = raw_input("Enter band's name: ")
            addSongs = True
            bandSongs = []
            addChoice = int(raw_input("Add songs? 1- Yes 2- No"))
            if addChoice == 2:
                addSongs = False
            elif addChoice == 1:
                addSongs = True
            while addSongs:
                viewSongs(songs)
                songID = int(raw_input("Enter song id:"))
                if songID > songs.__len__():
                    print("Invalid song id")
                else:
                    bandSongs.append(songs[songID - 1])
                new = int(raw_input("Enter another song? 1 - Yes 2 - No: "))
                if new == 2:
                    addSongs = False

            newBand = Band(name=name, songs=bandSongs)
            newBand.addBand()
        elif choice == 3:  # delete band
            bandID = int(raw_input("Enter band ID to delete: "))
            if bandID > bands.__len__():
                print("Invalid band ID")
            else:
                bandToDelete = bands[bandID - 1]
            deleteChoice = int(raw_input("Are you sure you want to delete? 1- Yes 2- No: "))
            if deleteChoice == 1:
                deleted = bandToDelete.deleteBand()
                if deleted == 0:
                    print ("Band successfully deleted.")


home()
