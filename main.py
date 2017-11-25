# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(696, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.songBtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)
        self.songBtn.setFont(font)
        self.songBtn.setObjectName(_fromUtf8("songBtn"))
        self.gridLayout.addWidget(self.songBtn, 2, 0, 1, 1)
        self.quitBtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)
        self.quitBtn.setFont(font)
        self.quitBtn.setObjectName(_fromUtf8("quitBtn"))
        self.gridLayout.addWidget(self.quitBtn, 2, 1, 1, 1)
        self.albumBtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.albumBtn.setFont(font)
        self.albumBtn.setObjectName(_fromUtf8("albumBtn"))
        self.gridLayout.addWidget(self.albumBtn, 0, 1, 1, 1)
        self.playlistBtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)
        self.playlistBtn.setFont(font)
        self.playlistBtn.setObjectName(_fromUtf8("playlistBtn"))
        self.gridLayout.addWidget(self.playlistBtn, 0, 0, 1, 1)
        self.artistBtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)
        self.artistBtn.setFont(font)
        self.artistBtn.setObjectName(_fromUtf8("artistBtn"))
        self.gridLayout.addWidget(self.artistBtn, 1, 0, 1, 1)
        self.bandBtn = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Source Sans Pro"))
        font.setPointSize(11)
        self.bandBtn.setFont(font)
        self.bandBtn.setObjectName(_fromUtf8("bandBtn"))
        self.gridLayout.addWidget(self.bandBtn, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 696, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.songBtn.setText(_translate("MainWindow", "Songs", None))
        self.quitBtn.setText(_translate("MainWindow", "Quit", None))
        self.albumBtn.setText(_translate("MainWindow", "Albums", None))
        self.playlistBtn.setText(_translate("MainWindow", "Playlists", None))
        self.artistBtn.setText(_translate("MainWindow", "Artists", None))
        self.bandBtn.setText(_translate("MainWindow", "Bands", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

