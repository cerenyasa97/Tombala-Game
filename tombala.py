"""
@file: tombala.py

@author: Ceren Yaşa

@date: June 3, 2020

@brief: Tombala Game with Qt Designer and Python
"""

from PyQt5 import QtCore, QtGui, QtWidgets          ## Basic modules of PyQt5
import numpy as np                                  ## NumPy is the fundamental package for scientific computing with Python
import random                                       ## Random module implements pseudo-random number generators for various distributions
import sys

## Main Window class generated
class Ui_MainWindow(object):

    ## Build the widget tree on the parent widget.
    def setupUi(self, MainWindow):
        
        ## Main window generating
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 650)     ## Initialize main window sizes
        MainWindow.setMinimumSize(QtCore.QSize(850, 650))    ## Initialize minimum main window sizes
        MainWindow.setMaximumSize(QtCore.QSize(850, 650))    ## Initialize maximum main window sizes
        font = QtGui.QFont()                                  ## Sets main window font properties
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()                                  ## Adds icon to main window
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)    ## The main window is shown in the middle of the screen
        self.centralwidget.setObjectName("centralwidget")
        
        ## With QLabel's pixmap feature background image is added
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("wall.jpg"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        
        ## With QLabel's pixmap feature yellow card is added
        self.yellow = QtWidgets.QLabel(self.centralwidget)
        self.yellow.setGeometry(QtCore.QRect(40, 50, 440, 160))
        self.yellow.setText("")
        self.yellow.setPixmap(QtGui.QPixmap("yellow.png"))
        self.yellow.setScaledContents(True)
        self.yellow.setObjectName("yellow")
        
        ## With QLabel's pixmap feature purple card is added
        self.purple = QtWidgets.QLabel(self.centralwidget)
        self.purple.setGeometry(QtCore.QRect(40, 50, 440, 160))
        self.purple.setText("")
        self.purple.setPixmap(QtGui.QPixmap("purple.png"))
        self.purple.setScaledContents(True)
        self.purple.setObjectName("purple")
        
        ## With QLabel's pixmap feature red card is added
        self.red = QtWidgets.QLabel(self.centralwidget)
        self.red.setGeometry(QtCore.QRect(40, 50, 440, 160))
        self.red.setText("")
        self.red.setPixmap(QtGui.QPixmap("red.png"))
        self.red.setScaledContents(True)
        self.red.setObjectName("red")
        
        ## With QLabel's pixmap feature lila card is added
        self.lila = QtWidgets.QLabel(self.centralwidget)
        self.lila.setGeometry(QtCore.QRect(40, 322, 440, 160))
        self.lila.setText("")
        self.lila.setPixmap(QtGui.QPixmap("lila.png"))
        self.lila.setScaledContents(True)
        self.lila.setObjectName("lila")
        
        ## With QLabel's pixmap feature green card is added
        self.green = QtWidgets.QLabel(self.centralwidget)
        self.green.setGeometry(QtCore.QRect(40, 322, 440, 160))
        self.green.setText("")
        self.green.setPixmap(QtGui.QPixmap("green.png"))
        self.green.setScaledContents(True)
        self.green.setObjectName("green")
        
        ## With QLabel's pixmap feature pink card is added
        self.pink = QtWidgets.QLabel(self.centralwidget)
        self.pink.setGeometry(QtCore.QRect(40, 322, 440, 160))
        self.pink.setText("")
        self.pink.setPixmap(QtGui.QPixmap("pink.png"))
        self.pink.setScaledContents(True)
        self.pink.setObjectName("pink")
        
        ## With QLabel's pixmap feature claret red card is added
        self.claretred = QtWidgets.QLabel(self.centralwidget)
        self.claretred.setGeometry(QtCore.QRect(40, 50, 440, 160))
        self.claretred.setText("")
        self.claretred.setPixmap(QtGui.QPixmap("brown.png"))
        self.claretred.setScaledContents(True)
        self.claretred.setObjectName("claretred")
        
        ## With QLabel's pixmap feature blue card is added
        self.blue = QtWidgets.QLabel(self.centralwidget)
        self.blue.setGeometry(QtCore.QRect(40, 322, 440, 160))
        self.blue.setText("")
        self.blue.setPixmap(QtGui.QPixmap("blue.png"))
        self.blue.setScaledContents(True)
        self.blue.setObjectName("blue")
        
        ## Card color options are offered with QComboBox
        self.cardSelect_1 = QtWidgets.QComboBox(self.centralwidget)
        self.cardSelect_1.setGeometry(QtCore.QRect(205, 20, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cardSelect_1.setFont(font)
        self.cardSelect_1.setObjectName("cardSelect_1")
        self.cardSelect_1.addItem("")
        self.cardSelect_1.addItem("")
        self.cardSelect_1.addItem("")
        self.cardSelect_1.addItem("")
        
        ## Card color options are offered with QComboBox
        self.cardSelect_2 = QtWidgets.QComboBox(self.centralwidget)
        self.cardSelect_2.setGeometry(QtCore.QRect(205, 290, 111, 22))
        self.cardSelect_2.setFont(font)
        self.cardSelect_2.setObjectName("cardSelect_2")
        self.cardSelect_2.addItem("")
        self.cardSelect_2.addItem("")
        self.cardSelect_2.addItem("")
        self.cardSelect_2.addItem("")
        
        ## If there is a matching number on the card with the stamp drawn, the QPushButton is pressed
        self.takeStamp_1 = QtWidgets.QPushButton(self.centralwidget)
        self.takeStamp_1.setGeometry(QtCore.QRect(390, 15, 85, 28))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 150, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(92, 150, 244))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        self.takeStamp_1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.takeStamp_1.setFont(font)
        self.takeStamp_1.setStyleSheet("background-color: rgb(92, 150, 244);\n"
"border-color: rgb(30, 11, 243);\n"
"border-width:2px;\n"
"border-style:outset;\n"
"border-radius:10px;")
        self.takeStamp_1.setObjectName("takeStamp_1")
        ## If there is a matching number on the card with the stamp drawn, the QPushButton is pressed
        self.takeStamp_2 = QtWidgets.QPushButton(self.centralwidget)
        self.takeStamp_2.setGeometry(QtCore.QRect(390, 287, 85, 28))
        self.takeStamp_2.setPalette(palette)
        self.takeStamp_2.setFont(font)
        self.takeStamp_2.setStyleSheet("background-color: rgb(92, 150, 244);\n"
"border-color: rgb(30, 11, 243);\n"
"border-width:2px;\n"
"border-style:outset;\n"
"border-radius:10px;")
        self.takeStamp_2.setObjectName("takeStamp_2")
        
        ## QPushButton is used to generate 15 random numbers in the 1-90 range to be displayed on the cards
        self.initializeNumbers = QtWidgets.QPushButton(self.centralwidget)
        self.initializeNumbers.setGeometry(QtCore.QRect(170, 525, 120, 30))
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.initializeNumbers.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.initializeNumbers.setFont(font)
        self.initializeNumbers.setStyleSheet("background-color: rgb(92, 150, 244);\n"
"border-color: rgb(30, 11, 243);\n"
"border-width:2px;\n"
"border-style:outset;\n"
"border-radius:10px;")
        self.initializeNumbers.setObjectName("initializeNumbers")
        
        ## Pulls Stamp
        self.pickNumber = QtWidgets.QPushButton(self.centralwidget)
        self.pickNumber.setGeometry(QtCore.QRect(570, 525, 120, 30))
        self.pickNumber.setPalette(palette)
        self.pickNumber.setFont(font)
        self.pickNumber.setStyleSheet("background-color: rgb(92, 150, 244);\n"
"border-color: rgb(30, 11, 243);\n"
"border-width:2px;\n"
"border-style:outset;\n"
"border-radius:10px;")
        self.pickNumber.setObjectName("pickNumber")
        
        ## Play button on the menu starts the game
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(320, 330, 200, 50))
        self.play.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.play.setFont(font)
        self.play.setStyleSheet("background-color: rgb(92, 150, 244);\n"
"border-color: rgb(30, 11, 243);\n"
"border-width:4px;\n"
"border-style:outset;\n"
"border-radius:20px;")
        self.play.setObjectName("play")
        
        ## Exit button in the menu for the close game
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(320, 440, 200, 50))
        self.exit.setPalette(palette)
        self.exit.setFont(font)
        self.exit.setStyleSheet("background-color: rgb(92, 150, 244);\n"
"border-color: rgb(30, 11, 243);\n"
"border-width:4px;\n"
"border-style:outset;\n"
"border-radius:20px;")
        self.exit.setObjectName("exit")
        
        ## Users can add their names to the QTextEdit widgets on the cards
        self.playerName1 = QtWidgets.QLineEdit(self.centralwidget)
        self.playerName1.setGeometry(QtCore.QRect(40, 18, 113, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.playerName1.setFont(font)
        self.playerName1.setObjectName("playerName1")
        ## Users can add their names to the QTextEdit widgets on the cards
        self.PlayerName2 = QtWidgets.QLineEdit(self.centralwidget)
        self.PlayerName2.setGeometry(QtCore.QRect(40, 290, 113, 25))
        self.PlayerName2.setFont(font)
        self.PlayerName2.setObjectName("PlayerName2")
        
        ## Player 1's score Label
        self.player1 = QtWidgets.QLabel(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(540, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.player1.setFont(font)
        self.player1.setObjectName("player1")
        
        ## Player 2's score Label
        self.player2 = QtWidgets.QLabel(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(540, 380, 141, 41))
        self.player2.setFont(font)
        self.player2.setObjectName("player2")
        
        ## Player 1's score
        self.player1_score = QtWidgets.QTextBrowser(self.centralwidget)
        self.player1_score.setGeometry(QtCore.QRect(660, 100, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.player1_score.setFont(font)
        self.player1_score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.player1_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.player1_score.setObjectName("player1_score")
        
        
        ## Player 2's score
        self.player2_score = QtWidgets.QTextBrowser(self.centralwidget)
        self.player2_score.setGeometry(QtCore.QRect(680, 380, 111, 41))
        self.player2_score.setFont(font)
        self.player2_score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.player2_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.player2_score.setObjectName("player2_score")
        
        ## Picked stamp label
        self.pickedNumber = QtWidgets.QLabel(self.centralwidget)
        self.pickedNumber.setGeometry(QtCore.QRect(510, 240, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pickedNumber.setFont(font)
        self.pickedNumber.setObjectName("pickedNumber")
        
        ## Stamp image drawn
        self.stamp = QtWidgets.QLabel(self.centralwidget)
        self.stamp.setGeometry(QtCore.QRect(690, 210, 90, 90))
        self.stamp.setPixmap(QtGui.QPixmap("stamp.png"))
        self.stamp.setScaledContents(True)
        self.stamp.setObjectName("stamp")
        
        ## The number on the stamp drawn
        self.pickedStamp = QtWidgets.QLabel(self.centralwidget)
        self.pickedStamp.setGeometry(QtCore.QRect(690, 210, 90, 90))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pickedStamp.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.pickedStamp.setFont(font)
        self.pickedStamp.setAlignment(QtCore.Qt.AlignCenter)
        self.pickedStamp.setObjectName("pickedStamp")
        
        ## Players information label
        self.information = QtWidgets.QLabel(self.centralwidget)
        self.information.setGeometry(QtCore.QRect(50, 580, 750, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.information.setFont(font)
        self.information.setObjectName("information")
        
        ## QLabels in positions where 15 numbers produced in the 1-90 range are written on Card-1
        self.p1_11 = QtWidgets.QLabel(self.centralwidget)
        self.p1_11.setGeometry(QtCore.QRect(50, 58, 42, 42))
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.p1_11.setFont(font)
        self.p1_11.setText("")
        self.p1_11.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_11.setObjectName("p1_11")
        self.p1_12 = QtWidgets.QLabel(self.centralwidget)
        self.p1_12.setGeometry(QtCore.QRect(143, 58, 42, 42))
        self.p1_12.setFont(font)
        self.p1_12.setText("")
        self.p1_12.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_12.setObjectName("p1_12")
        self.p1_13 = QtWidgets.QLabel(self.centralwidget)
        self.p1_13.setGeometry(QtCore.QRect(240, 58, 42, 42))
        self.p1_13.setFont(font)
        self.p1_13.setText("")
        self.p1_13.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_13.setObjectName("p1_13")
        self.p1_14 = QtWidgets.QLabel(self.centralwidget)
        self.p1_14.setGeometry(QtCore.QRect(333, 58, 42, 42))
        self.p1_14.setFont(font)
        self.p1_14.setText("")
        self.p1_14.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_14.setObjectName("p1_14")
        self.p1_15 = QtWidgets.QLabel(self.centralwidget)
        self.p1_15.setGeometry(QtCore.QRect(381, 58, 42, 42))
        self.p1_15.setFont(font)
        self.p1_15.setText("")
        self.p1_15.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_15.setObjectName("p1_15")
        self.p1_21 = QtWidgets.QLabel(self.centralwidget)
        self.p1_21.setGeometry(QtCore.QRect(97, 109, 42, 42))
        self.p1_21.setFont(font)
        self.p1_21.setText("")
        self.p1_21.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_21.setObjectName("p1_21")
        self.p1_22 = QtWidgets.QLabel(self.centralwidget)
        self.p1_22.setGeometry(QtCore.QRect(191, 109, 42, 42))
        self.p1_22.setFont(font)
        self.p1_22.setText("")
        self.p1_22.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_22.setObjectName("p1_22")
        self.p1_23 = QtWidgets.QLabel(self.centralwidget)
        self.p1_23.setGeometry(QtCore.QRect(286, 109, 42, 42))
        self.p1_23.setFont(font)
        self.p1_23.setText("")
        self.p1_23.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_23.setObjectName("p1_23")
        self.p1_24 = QtWidgets.QLabel(self.centralwidget)
        self.p1_24.setGeometry(QtCore.QRect(381, 109, 42, 42))
        self.p1_24.setFont(font)
        self.p1_24.setText("")
        self.p1_24.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_24.setObjectName("p1_24")
        self.p1_25 = QtWidgets.QLabel(self.centralwidget)
        self.p1_25.setGeometry(QtCore.QRect(429, 109, 42, 42))
        self.p1_25.setFont(font)
        self.p1_25.setText("")
        self.p1_25.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_25.setObjectName("p1_25")
        self.p1_31 = QtWidgets.QLabel(self.centralwidget)
        self.p1_31.setGeometry(QtCore.QRect(50, 160, 42, 42))
        self.p1_31.setFont(font)
        self.p1_31.setText("")
        self.p1_31.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_31.setObjectName("p1_31")
        self.p1_32 = QtWidgets.QLabel(self.centralwidget)
        self.p1_32.setGeometry(QtCore.QRect(143, 160, 42, 42))
        self.p1_32.setFont(font)
        self.p1_32.setText("")
        self.p1_32.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_32.setObjectName("p1_32")
        self.p1_33 = QtWidgets.QLabel(self.centralwidget)
        self.p1_33.setGeometry(QtCore.QRect(240, 160, 42, 42))
        self.p1_33.setFont(font)
        self.p1_33.setText("")
        self.p1_33.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_33.setObjectName("p1_33")
        self.p1_34 = QtWidgets.QLabel(self.centralwidget)
        self.p1_34.setGeometry(QtCore.QRect(333, 160, 42, 42))
        self.p1_34.setFont(font)
        self.p1_34.setText("")
        self.p1_34.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_34.setObjectName("p1_34")
        self.p1_35 = QtWidgets.QLabel(self.centralwidget)
        self.p1_35.setGeometry(QtCore.QRect(430, 160, 42, 42))
        self.p1_35.setFont(font)
        self.p1_35.setText("")
        self.p1_35.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_35.setObjectName("p1_35")
        
        ## QLabels with stamps positioned on the Card 1 with format p1_xy_2 which xth row yth column
        self.p1_11_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_11_2.setGeometry(QtCore.QRect(46, 55, 48, 48))
        self.p1_11_2.setFont(font)
        self.p1_11_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_11_2.setScaledContents(True)
        self.p1_11_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_11_2.setObjectName("p1_11_2")
        self.p1_12_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_12_2.setGeometry(QtCore.QRect(142, 55, 48, 48))
        self.p1_12_2.setFont(font)
        self.p1_12_2.setText("")
        self.p1_12_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_12_2.setScaledContents(True)
        self.p1_12_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_12_2.setObjectName("p1_12_2")        
        self.p1_13_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_13_2.setGeometry(QtCore.QRect(237, 55, 48, 48))
        self.p1_13_2.setFont(font)
        self.p1_13_2.setText("")
        self.p1_13_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_13_2.setScaledContents(True)
        self.p1_13_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_13_2.setObjectName("p1_13_2")
        self.p1_14_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_14_2.setGeometry(QtCore.QRect(331, 55, 48, 48))
        self.p1_14_2.setFont(font)
        self.p1_14_2.setText("")
        self.p1_14_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_14_2.setScaledContents(True)
        self.p1_14_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_14_2.setObjectName("p1_14_2")
        self.p1_15_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_15_2.setGeometry(QtCore.QRect(379, 55, 48, 48))
        self.p1_15_2.setFont(font)
        self.p1_15_2.setText("")
        self.p1_15_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_15_2.setScaledContents(True)
        self.p1_15_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_15_2.setObjectName("p1_15_2")
        self.p1_21_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_21_2.setGeometry(QtCore.QRect(94, 107, 48, 48))
        self.p1_21_2.setFont(font)
        self.p1_21_2.setText("")
        self.p1_21_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_21_2.setScaledContents(True)
        self.p1_21_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_21_2.setObjectName("p1_21_2")
        self.p1_22_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_22_2.setGeometry(QtCore.QRect(189, 107, 48, 48))
        self.p1_22_2.setFont(font)
        self.p1_22_2.setText("")
        self.p1_22_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_22_2.setScaledContents(True)
        self.p1_22_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_22_2.setObjectName("p1_22_2")
        self.p1_23_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_23_2.setGeometry(QtCore.QRect(284, 107, 48, 48))
        self.p1_23_2.setFont(font)
        self.p1_23_2.setText("")
        self.p1_23_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_23_2.setScaledContents(True)
        self.p1_23_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_23_2.setObjectName("p1_23_2")
        self.p1_24_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_24_2.setGeometry(QtCore.QRect(379, 107, 48, 48))
        self.p1_24_2.setFont(font)
        self.p1_24_2.setText("")
        self.p1_24_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_24_2.setScaledContents(True)
        self.p1_24_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_24_2.setObjectName("p1_24_2")
        self.p1_25_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_25_2.setGeometry(QtCore.QRect(427, 107, 48, 48))
        self.p1_25_2.setFont(font)
        self.p1_25_2.setText("")
        self.p1_25_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_25_2.setScaledContents(True)
        self.p1_25_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_25_2.setObjectName("p1_25_2")
        self.p1_31_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_31_2.setGeometry(QtCore.QRect(47, 157, 48, 48))
        self.p1_31_2.setFont(font)
        self.p1_31_2.setText("")
        self.p1_31_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_31_2.setScaledContents(True)
        self.p1_31_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_31_2.setObjectName("p1_31_2")
        self.p1_32_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_32_2.setGeometry(QtCore.QRect(142, 157, 48, 48))
        self.p1_32_2.setFont(font)
        self.p1_32_2.setText("")
        self.p1_32_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_32_2.setScaledContents(True)
        self.p1_32_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_32_2.setObjectName("p1_32_2")
        self.p1_33_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_33_2.setGeometry(QtCore.QRect(237, 157, 48, 48))
        self.p1_33_2.setFont(font)
        self.p1_33_2.setText("")
        self.p1_33_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_33_2.setScaledContents(True)
        self.p1_33_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_33_2.setObjectName("p1_33_2")   
        self.p1_34_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_34_2.setGeometry(QtCore.QRect(332, 157, 48, 48))
        self.p1_34_2.setFont(font)
        self.p1_34_2.setText("")
        self.p1_34_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_34_2.setScaledContents(True)
        self.p1_34_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_34_2.setObjectName("p1_34_2")
        self.p1_35_2 = QtWidgets.QLabel(self.centralwidget)
        self.p1_35_2.setGeometry(QtCore.QRect(426, 157, 48, 48))
        self.p1_35_2.setFont(font)
        self.p1_35_2.setText("")
        self.p1_35_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p1_35_2.setScaledContents(True)
        self.p1_35_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p1_35_2.setObjectName("p1_35_2")
                
        ## QLabels in positions where 15 numbers produced in the 1-90 range are written on Card-2
        self.p2_11 = QtWidgets.QLabel(self.centralwidget)
        self.p2_11.setGeometry(QtCore.QRect(50, 331, 42, 42))
        self.p2_11.setFont(font)
        self.p2_11.setText("")
        self.p2_11.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_11.setObjectName("p2_11")
        self.p2_12 = QtWidgets.QLabel(self.centralwidget)
        self.p2_12.setGeometry(QtCore.QRect(97, 331, 42, 42))
        self.p2_12.setFont(font)
        self.p2_12.setText("")
        self.p2_12.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_12.setObjectName("p2_12")
        self.p2_13 = QtWidgets.QLabel(self.centralwidget)
        self.p2_13.setGeometry(QtCore.QRect(191, 331, 42, 42))
        self.p2_13.setFont(font)
        self.p2_13.setText("")
        self.p2_13.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_13.setObjectName("p2_13")
        self.p2_14 = QtWidgets.QLabel(self.centralwidget)
        self.p2_14.setGeometry(QtCore.QRect(287, 331, 42, 42))
        self.p2_14.setFont(font)
        self.p2_14.setText("")
        self.p2_14.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_14.setObjectName("p2_14")
        self.p2_15 = QtWidgets.QLabel(self.centralwidget)
        self.p2_15.setGeometry(QtCore.QRect(380, 331, 42, 42))
        self.p2_15.setFont(font)
        self.p2_15.setText("")
        self.p2_15.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_15.setObjectName("p2_15")
        self.p2_21 = QtWidgets.QLabel(self.centralwidget)
        self.p2_21.setGeometry(QtCore.QRect(97, 381, 42, 42))
        self.p2_21.setFont(font)
        self.p2_21.setText("")
        self.p2_21.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_21.setObjectName("p2_21")
        self.p2_22 = QtWidgets.QLabel(self.centralwidget)
        self.p2_22.setGeometry(QtCore.QRect(143, 381, 42, 42))
        self.p2_22.setFont(font)
        self.p2_22.setText("")
        self.p2_22.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_22.setObjectName("p2_22")
        self.p2_23 = QtWidgets.QLabel(self.centralwidget)
        self.p2_23.setGeometry(QtCore.QRect(240, 381, 42, 42))
        self.p2_23.setFont(font)
        self.p2_23.setText("")
        self.p2_23.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_23.setObjectName("p2_23")
        self.p2_24 = QtWidgets.QLabel(self.centralwidget)
        self.p2_24.setGeometry(QtCore.QRect(333, 381, 42, 42))
        self.p2_24.setFont(font)
        self.p2_24.setText("")
        self.p2_24.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_24.setObjectName("p2_24")   
        self.p2_25 = QtWidgets.QLabel(self.centralwidget)
        self.p2_25.setGeometry(QtCore.QRect(430, 381, 42, 42))
        self.p2_25.setFont(font)
        self.p2_25.setText("")
        self.p2_25.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_25.setObjectName("p2_25")
        self.p2_31 = QtWidgets.QLabel(self.centralwidget)
        self.p2_31.setGeometry(QtCore.QRect(50, 432, 42, 42))
        self.p2_31.setFont(font)
        self.p2_31.setText("")
        self.p2_31.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_31.setObjectName("p2_31")
        self.p2_32 = QtWidgets.QLabel(self.centralwidget)
        self.p2_32.setGeometry(QtCore.QRect(143, 432, 42, 42))
        self.p2_32.setFont(font)
        self.p2_32.setText("")
        self.p2_32.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_32.setObjectName("p2_32")
        self.p2_33 = QtWidgets.QLabel(self.centralwidget)
        self.p2_33.setGeometry(QtCore.QRect(192, 432, 42, 42))
        self.p2_33.setFont(font)
        self.p2_33.setText("")
        self.p2_33.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_33.setObjectName("p2_33")
        self.p2_34 = QtWidgets.QLabel(self.centralwidget)
        self.p2_34.setGeometry(QtCore.QRect(287, 432, 42, 42))
        self.p2_34.setFont(font)
        self.p2_34.setText("")
        self.p2_34.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_34.setObjectName("p2_34")
        self.p2_35 = QtWidgets.QLabel(self.centralwidget)
        self.p2_35.setGeometry(QtCore.QRect(381, 432, 42, 42))
        self.p2_35.setFont(font)
        self.p2_35.setText("")
        self.p2_35.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_35.setObjectName("p2_35")
        
        ## QLabels with stamps positioned on the Card 2 with format p2_xy_2 which xth row yth column
        self.p2_11_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_11_2.setGeometry(QtCore.QRect(47, 328, 48, 48))
        self.p2_11_2.setFont(font)
        self.p2_11_2.setText("")
        self.p2_11_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_11_2.setScaledContents(True)
        self.p2_11_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_11_2.setObjectName("p2_11_2")
        self.p2_12_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_12_2.setGeometry(QtCore.QRect(94, 328, 48, 48))
        self.p2_12_2.setFont(font)
        self.p2_12_2.setText("")
        self.p2_12_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_12_2.setScaledContents(True)
        self.p2_12_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_12_2.setObjectName("p2_12_2")
        self.p2_13_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_13_2.setGeometry(QtCore.QRect(188, 328, 48, 48))
        self.p2_13_2.setFont(font)
        self.p2_13_2.setText("")
        self.p2_13_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_13_2.setScaledContents(True)
        self.p2_13_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_13_2.setObjectName("p2_13_2")
        self.p2_14_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_14_2.setGeometry(QtCore.QRect(284, 328, 48, 48))
        self.p2_14_2.setFont(font)
        self.p2_14_2.setText("")
        self.p2_14_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_14_2.setScaledContents(True)
        self.p2_14_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_14_2.setObjectName("p2_14_2")
        self.p2_15_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_15_2.setGeometry(QtCore.QRect(379, 328, 48, 48))
        self.p2_15_2.setFont(font)
        self.p2_15_2.setText("")
        self.p2_15_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_15_2.setScaledContents(True)
        self.p2_15_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_15_2.setObjectName("p2_15_2")
        self.p2_21_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_21_2.setGeometry(QtCore.QRect(94, 378, 48, 48))
        self.p2_21_2.setFont(font)
        self.p2_21_2.setText("")
        self.p2_21_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_21_2.setScaledContents(True)
        self.p2_21_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_21_2.setObjectName("p2_21_2")
        self.p2_22_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_22_2.setGeometry(QtCore.QRect(142, 378, 48, 48))
        self.p2_22_2.setFont(font)
        self.p2_22_2.setText("")
        self.p2_22_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_22_2.setScaledContents(True)
        self.p2_22_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_22_2.setObjectName("p2_22_2")
        self.p2_23_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_23_2.setGeometry(QtCore.QRect(236, 378, 48, 48))
        self.p2_23_2.setFont(font)
        self.p2_23_2.setText("")
        self.p2_23_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_23_2.setScaledContents(True)
        self.p2_23_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_23_2.setObjectName("p2_23_2")
        self.p2_24_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_24_2.setGeometry(QtCore.QRect(331, 378, 48, 48))
        self.p2_24_2.setFont(font)
        self.p2_24_2.setText("")
        self.p2_24_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_24_2.setScaledContents(True)
        self.p2_24_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_24_2.setObjectName("p2_24_2")
        self.p2_25_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_25_2.setGeometry(QtCore.QRect(427, 378, 48, 48))
        self.p2_25_2.setFont(font)
        self.p2_25_2.setText("")
        self.p2_25_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_25_2.setScaledContents(True)
        self.p2_25_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_25_2.setObjectName("p2_25_2")
        self.p2_31_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_31_2.setGeometry(QtCore.QRect(47, 429, 48, 48))
        self.p2_31_2.setFont(font)
        self.p2_31_2.setText("")
        self.p2_31_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_31_2.setScaledContents(True)
        self.p2_31_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_31_2.setObjectName("p2_31_2")
        self.p2_32_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_32_2.setGeometry(QtCore.QRect(141, 429, 48, 48))
        self.p2_32_2.setFont(font)
        self.p2_32_2.setText("")
        self.p2_32_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_32_2.setScaledContents(True)
        self.p2_32_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_32_2.setObjectName("p2_32_2")
        self.p2_33_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_33_2.setGeometry(QtCore.QRect(189, 429, 48, 48))
        self.p2_33_2.setFont(font)
        self.p2_33_2.setText("")
        self.p2_33_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_33_2.setScaledContents(True)
        self.p2_33_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_33_2.setObjectName("p2_33_2")
        self.p2_34_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_34_2.setGeometry(QtCore.QRect(284, 429, 48, 48))
        self.p2_34_2.setFont(font)
        self.p2_34_2.setText("")
        self.p2_34_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_34_2.setScaledContents(True)
        self.p2_34_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_34_2.setObjectName("p2_34_2")
        self.p2_35_2 = QtWidgets.QLabel(self.centralwidget)
        self.p2_35_2.setGeometry(QtCore.QRect(379, 429, 48, 48))
        self.p2_35_2.setFont(font)
        self.p2_35_2.setText("")
        self.p2_35_2.setPixmap(QtGui.QPixmap("stamp.png"))
        self.p2_35_2.setScaledContents(True)
        self.p2_35_2.setAlignment(QtCore.Qt.AlignCenter)
        self.p2_35_2.setObjectName("p2_35_2")
        
        ## Card number is defined for 8 different card colors
        self.card_number_1 = QtWidgets.QLabel(self.centralwidget)
        self.card_number_1.setGeometry(QtCore.QRect(45, 105, 48, 48))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.card_number_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.card_number_1.setFont(font)
        self.card_number_1.setText("")
        self.card_number_1.setScaledContents(True)
        self.card_number_1.setAlignment(QtCore.Qt.AlignCenter)
        self.card_number_1.setObjectName("card_number_1")
        ## Card number is defined for 8 different card colors
        self.card_number_2 = QtWidgets.QLabel(self.centralwidget)
        self.card_number_2.setGeometry(QtCore.QRect(45, 380, 42, 42))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.card_number_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.card_number_2.setFont(font)
        self.card_number_2.setText("")
        self.card_number_2.setAlignment(QtCore.Qt.AlignCenter)
        self.card_number_2.setObjectName("card_number_2")
        
        ## Adds menu background with QLabel's pixmap feature
        self.intro = QtWidgets.QLabel(self.centralwidget)
        self.intro.setGeometry(QtCore.QRect(0, 0, 850, 650))
        self.intro.setText("")
        self.intro.setPixmap(QtGui.QPixmap("intro.png"))
        self.intro.setScaledContents(True)
        self.intro.setObjectName("intro")
        
        ## Widgets used are brought forward respectively
        self.background.raise_()
        self.stamp.raise_()
        self.red.raise_()
        self.playerName1.raise_()
        self.purple.raise_()
        self.yellow.raise_()
        self.claretred.raise_()
        self.blue.raise_()
        self.green.raise_()
        self.pink.raise_()
        self.lila.raise_()
        self.PlayerName2.raise_()
        self.takeStamp_1.raise_()
        self.takeStamp_2.raise_()
        self.initializeNumbers.raise_()
        self.pickNumber.raise_()
        self.player2.raise_()
        self.p1_11.raise_()
        self.player1.raise_()
        self.pickedNumber.raise_()
        self.player2_score.raise_()
        self.player1_score.raise_()
        self.pickedStamp.raise_()
        self.p1_11_2.raise_()
        self.p1_12.raise_()
        self.p1_12_2.raise_()
        self.p1_13.raise_()
        self.p1_13_2.raise_()
        self.p1_14.raise_()
        self.p1_14_2.raise_()
        self.p1_15.raise_()
        self.p1_15_2.raise_()
        self.p1_21_2.raise_()
        self.p1_21.raise_()
        self.p1_22.raise_()
        self.p1_22_2.raise_()
        self.p1_23.raise_()
        self.p1_23_2.raise_()
        self.p1_24.raise_()
        self.p1_24_2.raise_()
        self.p1_25.raise_()
        self.p1_25_2.raise_()
        self.p1_35.raise_()
        self.p1_35_2.raise_()
        self.p1_34_2.raise_()
        self.p1_34.raise_()
        self.p1_33.raise_()
        self.p1_33_2.raise_()
        self.p1_32_2.raise_()
        self.p1_32.raise_()
        self.p1_31.raise_()
        self.p1_31_2.raise_()
        self.p2_11.raise_()
        self.p2_11_2.raise_()
        self.p2_12_2.raise_()
        self.p2_12.raise_()
        self.p2_13.raise_()
        self.p2_13_2.raise_()
        self.p2_14.raise_()
        self.p2_14_2.raise_()
        self.p2_15.raise_()
        self.p2_15_2.raise_()
        self.p2_21_2.raise_()
        self.p2_21.raise_()
        self.p2_22.raise_()
        self.p2_22_2.raise_()
        self.p2_23.raise_()
        self.p2_23_2.raise_()
        self.p2_24.raise_()
        self.p2_24_2.raise_()
        self.p2_25.raise_()
        self.p2_25_2.raise_()
        self.p2_31_2.raise_()
        self.p2_31.raise_()
        self.p2_32.raise_()
        self.p2_32_2.raise_()
        self.p2_33.raise_()
        self.p2_33_2.raise_()
        self.p2_34.raise_()
        self.p2_34_2.raise_()
        self.p2_35_2.raise_()
        self.p2_35.raise_()
        self.cardSelect_2.raise_()
        self.cardSelect_1.raise_()
        self.card_number_1.raise_()
        self.card_number_2.raise_()
        self.information.raise_()
        self.intro.raise_()
        self.exit.raise_()
        self.play.raise_()
        
        ## The top menu and under actions are created
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 21))
        self.menubar.setObjectName("menubar")
        ## File menu created
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        ## Menu action created to return menu
        self.actionMenu = QtWidgets.QAction(MainWindow)
        self.actionMenu.setIconVisibleInMenu(True)
        self.actionMenu.setObjectName("actionMenu")
        ## Exit action created to quit 
        self.actionExit = QtWidgets.QAction(MainWindow)
        ## Adds icon for the exit action
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionMenu)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        ## Member function retranslateUi handles the translation of the string properties of the form
        self.retranslateUi(MainWindow)
        
        ## With the Signal-Slot mechanism, when players add their names, score labels also change according to the names
        self.playerName1.textChanged['QString'].connect(self.player1.setText)
        self.PlayerName2.textChanged['QString'].connect(self.player2.setText)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ## PlayGame function is called when the play button is pressed
        self.play.clicked.connect(self.playGame)
        ## Pressing the Exit button will quit the game
        self.exit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        ## Exit action is exited when triggered
        self.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        ## returnMenu function is called to the menu when the menu action is triggered
        self.actionMenu.triggered.connect(self.returnMenu)

        ## selectCard function is called when cards are selected from combo boxes
        self.cardSelect_1.activated[str].connect(self.selectCard)
        self.cardSelect_2.activated[str].connect(self.selectCard)
        
        ## When the button is pressed, take_stamp functions are called
        self.takeStamp_1.clicked.connect(self.take_stamp_1)
        self.takeStamp_2.clicked.connect(self.take_stamp_2)

        ## When the button is pressed, the setCardNumbers function is called
        self.initializeNumbers.clicked.connect(self.setCardNumbers)

        ## Stamp is drawn when the button is pressed
        self.pickNumber.clicked.connect(self.picked_stamp)

    ## Game start settings
    def start_settings(self):
            ## Cards are hidden when the game starts
            self.purple.hide()
            self.yellow.hide()
            self.red.hide()
            self.lila.hide()
            self.green.hide()
            self.pink.hide()
            self.blue.hide()
            self.claretred.hide()

            ## Labels containing card numbers and card stamps are listed
            self.label_lists()

            ## Empty lists containing row-by-row numbers of cards are created for later use
            self.c1row=[]
            ## Empty lists containing row-by-row numbers of cards are created for later use
            self.c2row=[]
        
            ## Score values ​​of Player 1 and Player 2 are initialized to 0
            self.player_1_score=0
            self.player_2_score=0

            ## A numpy array containing numbers 1-90 is created so that the stamp to be drawn does not show the same number twice
            self.stamps = np.arange(1,91)
        


    ## Function that hides the menu
    def playGame(self):
            self.intro.hide()
            self.play.hide()
            self.exit.hide()
            self.purple.hide()
            self.yellow.hide()
            self.red.hide()
            self.lila.hide()
            self.green.hide()
            self.pink.hide()
            self.blue.hide()
            self.claretred.hide()

            self.takeStamp_1.setEnabled(False)
            self.takeStamp_2.setEnabled(False)

            self.cardSelect_1.setEnabled(True)
            self.cardSelect_2.setEnabled(True)

            self.label_lists()
            self.black_color()

            self.stamps = np.arange(1,91)
            self.pickedStamp.setText("0")

            ## Empty lists containing row-by-row numbers of cards are created for later use
            self.c1row=[]
            self.c2row=[]

            ## Score values ​​of Player 1 and Player 2 are initialized to 0
            self.player_1_score=0
            self.player_2_score=0

            ## The buttons matches the stamp with the numbers on the players cards is deactive
            self.takeStamp_1.setEnabled(False)
            self.takeStamp_2.setEnabled(False)

            self.card_number_1.setText(" ")
            self.card_number_2.setText(" ")

            self.playerName1.setText("Player 1")
            self.PlayerName2.setText("Player 2")

            self.initializeNumbers.setEnabled(True)
            self.pickNumber.setEnabled(True)

            self.information.setText("Information")


    ## Function that shows the menu again
    def returnMenu(self):
            self.intro.show()
            self.play.show()
            self.exit.show()
            self.intro.raise_()
            self.play.raise_()
            self.exit.raise_()

    ## The function that brings the cards in the colors selected from the combobox to the show status
    def selectCard(self,text):
        if text.lower() == "claret red":
            self.claretred.show()
            self.claretred.raise_()

        if text.lower() == "blue":
            self.blue.show()
            self.blue.raise_()

        if text.lower() == "green":
            self.green.show()
            self.green.raise_()

        if text.lower() == "lila":
            self.lila.show()
            self.lila.raise_()

        if text.lower() == "purple":
            self.purple.show()
            self.purple.raise_()

        if text.lower() == "red":
            self.red.show()
            self.red.raise_()

        if text.lower() == "pink":
            self.pink.show()
            self.pink.raise_()

        if text.lower() == "yellow":
            self.yellow.show()
            self.yellow.raise_()

        ## The numbers are brought forward according to the card color between 1-8
        self.card_number_1.raise_()
        self.card_number_2.raise_()
        
        ## Numbers 1-90 on the cards are brought to the front of the card
        for i in range(3):
                for j in range(5):
                        self.card1[i][j].raise_()
                        self.card2[i][j].raise_()
    
    ## The labels showing the numbers and stamps are listed on the cards
    def label_lists(self):
        ## card1 is QLabel list on the card 1 numbers
        self.card1=[[self.p1_11, self.p1_12, self.p1_13, self.p1_14, self.p1_15], [self.p1_21, self.p1_22, self.p1_23, self.p1_24, self.p1_25], [self.p1_31, self.p1_32, self.p1_33, self.p1_34, self.p1_35]]
        ## card2 is QLabel list on the card 2 numbers
        self.card2=[[self.p2_11, self.p2_12, self.p2_13, self.p2_14, self.p2_15], [self.p2_21, self.p2_22, self.p2_23, self.p2_24, self.p2_25], [self.p2_31, self.p2_32, self.p2_33, self.p2_34, self.p2_35]]
        ## card1 is QLabel list on the card 1 stamps
        self.card1_stamp=[[self.p1_11_2, self.p1_12_2, self.p1_13_2, self.p1_14_2, self.p1_15_2], [self.p1_21_2, self.p1_22_2, self.p1_23_2, self.p1_24_2, self.p1_25_2], [self.p1_31_2, self.p1_32_2, self.p1_33_2, self.p1_34_2, self.p1_35_2]]
        ## card1 is QLabel list on the card 2 stamps
        self.card2_stamp=[[self.p2_11_2, self.p2_12_2, self.p2_13_2, self.p2_14_2, self.p2_15_2], [self.p2_21_2, self.p2_22_2, self.p2_23_2, self.p2_24_2, self.p2_25_2], [self.p2_31_2, self.p2_32_2, self.p2_33_2, self.p2_34_2, self.p2_35_2]]

        ## Labels showing numbers and stamps on the cards are hidden at the start of the game
        for i in range(3):
                for j in range(5):
                        self.card1[i][j].setText(" ")
                        self.card2[i][j].setText(" ")
                        self.card1_stamp[i][j].hide()
                        self.card2_stamp[i][j].hide()

                        self.card1[i][j].raise_()
                        self.card2[i][j].raise_()
    
    ## Function that generates random numbers from 1 to 90 to be displayed on the cards and displays on labels
    def setCardNumbers(self):
        ## Once the numbers on the cards are initialized, the button is deactivated so that it cannot be changed again
        self.initializeNumbers.setEnabled(False)
        
        ## Once the numbers on the cards are initialized, the button is deactivated so that it cannot be changed again
        card_numbers = np.array(random.sample(range(1,9),2))
        self.card_number_1.setText(str(card_numbers[0]))
        self.card_number_2.setText(str(card_numbers[1]))
        self.card_number_1.raise_()
        self.card_number_2.raise_()
        
        ## In order to remove the possibility of seeing the same numbers on the same card, 15 numbers between 1-90 are generated at once and three rows and five columns are reshaped
        self.card1_numbers = np.array(random.sample(range(1,91),15)).reshape(3,5)
        
        ## In order to remove the possibility of seeing the same numbers on the same card, 15 numbers between 1-90 are generated at once and three rows and five columns are reshaped
        self.card2_numbers = np.array(random.sample(range(1,91),15)).reshape(3,5)
        
        ## The numbers on the cards are sorted from small to large in each row
        self.card1_numbers.sort(axis=1)
        self.card2_numbers.sort(axis=1)
        
        ## The generated fifteen numbers are set at the correct positions on the cards
        for i in range(3):
                for j in range(5):
                        self.card1[i][j].raise_()
                        self.card2[i][j].raise_()
                        self.card1[i][j].setText(str(self.card1_numbers[i][j]))
                        self.card2[i][j].setText(str(self.card2_numbers[i][j]))
                        
        ## Each row with the generated numbers is added to a list                
        for i in range(3):
                self.c1row.append(list(self.card1_numbers[i]))
        for i in range(3):
                self.c2row.append(list(self.card2_numbers[i]))   
    
    ## Draws a stamp each time it is called
    def picked_stamp(self):
            ## The button that matches the stamp with the numbers on the players cards is activated
            self.takeStamp_1.setEnabled(True)
            self.takeStamp_2.setEnabled(True)
            
            ## As long as 90 stamps arrays produced between 1-90 are not empty, new stamps are drawn
            if len(self.stamps)!=0:
                    ## Random number is selected from stamps array and stamp label is set
                    self.picked = random.choice(self.stamps)
                    self.stamps = np.delete( self.stamps, np.where(self.stamps==self.picked)[0][0])
                    self.pickedStamp.setText(str(self.picked))
                    self.pickedStamp.raise_()
 
            ## The game ends when the Stamps series is empty
            else:
                    self.msg = QtWidgets.QMessageBox()
                    self.msg.setWindowTitle("Game Over")
                    self.msg.setText("Game Over!\nStamps are over!")
                    x = self.msg.exec_()
                    self.pickNumber.setEnabled(False)

    ## From the numbers on the drawn card 1, there is a number that matches the stamp and the stamp that is in the same index with the label of that number is set
    def take_stamp_1(self):
            j=0
            ## The drawn stamp is checked on each line
            for i in range(3):
                        if (self.picked in self.c1row[i]):
                                j = self.c1row[i].index(self.picked)
                                
                                ## The stamp in the index containing the same number as the stamp is displayed on the card
                                self.card1_stamp[i][j].show()
                                self.card1_stamp[i][j].raise_()
                                ## Stamp and number brought to the show status are deleted from the list
                                self.c1row[i].remove(self.picked)
                                del self.card1_stamp[i][j]
                                self.white_color(self.card1,i,j)
                                self.card1[i][j].raise_()
                                self.card1[i][j].setText(str(self.picked))
                                del self.card1[i][j]
                                
                                ## When any line is empty on Card 1, bingo1 function is called
                                if len(self.c1row[i]) == 0:
                                        self.bingo1()
        
    ## From the numbers on the drawn card 2, there is a number that matches the stamp and the stamp that is in the same index with the label of that number is set
    def take_stamp_2(self):
            j=0
            ## The drawn stamp is checked on each line
            for i in range(3):
                        if (self.picked in self.c2row[i]):
                                j = self.c2row[i].index(self.picked)
                                
                                ## The stamp in the index containing the same number as the stamp is displayed on the card
                                self.card2_stamp[i][j].show()
                                self.card2_stamp[i][j].raise_()
                                ## Stamp and number brought to the show status are deleted from the list
                                del self.card2_stamp[i][j]
                                self.c2row[i].remove(self.picked)
                                self.white_color(self.card2,i,j)
                                self.card2[i][j].raise_()
                                self.card2[i][j].setText(str(self.picked))
                                del self.card2[i][j]
                                
                                ## When any line is empty on Card 1, bingo1 function is called
                                if len(self.c2row[i]) == 0:
                                        self.bingo2()

    ## If the stamps on the cards are turned into show status, the text will appear in white
    def white_color(self,card,i,j):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        card[i][j].setPalette(palette)

    ## Gives the numbers on the cards black when the stamps are hidden
    def black_color(self):
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        for i in range(3):
                for j in range(5):
                        self.card1[i][j].setPalette(palette)
                        self.card2[i][j].setPalette(palette)

    ## Function that determines which line is empty when any line is empty and gives Player 1 score
    def bingo1(self):
        ## The player gets 10 points when the first line is completed
        if self.player_1_score == 0:
                self.information.setText("Player 1 : First Bingo! You take 10 points.")
                self.player_1_score += 10
        ## The player gets 20 points when the second line is completed
        elif self.player_1_score == 10:
                self.information.setText("Player 1 : Second Bingo! You take 20 points.")
                self.player_1_score += 20
        ## The player gets 40 points when the third line is completed and The game ends when the player gets 70 points and completes three lines
        elif self.player_1_score == 30:
                self.information.setText("Player 1 : Third Bingo! You take 40 points.YOU WIN!!!")
                self.player_1_score += 40
                self.msg = QtWidgets.QMessageBox()
                self.msg.setWindowTitle("Game Over")
                self.msg.setText("Winner Player 1!")
                x = self.msg.exec_()
                self.pickNumber.setEnabled(False)
        self.player1_score.setText(str(self.player_1_score))

    ## Function that determines which line is empty when any line is empty and gives Player 2 score
    def bingo2(self):
        ## The player gets 10 points when the first line is completed
        if self.player_2_score == 0:
                self.information.setText("Player 2 : First Bingo! You take 10 points.")
                self.player_2_score += 10
        ## The player gets 20 points when the second line is completed
        elif self.player_2_score == 10:
                self.information.setText("Player 2 : Second Bingo! You take 20 points.")
                self.player_2_score += 20
        ## The player gets 40 points when the third line is completed and The game ends when the player gets 70 points and completes three lines
        elif self.player_2_score == 30:
                self.information.setText("Player 2 : Third Bingo! You take 40 points.YOU WIN!!!")
                self.player_2_score += 40
                self.msg = QtWidgets.QMessageBox()
                self.msg.setGeometry(575,425,100,50)
                self.msg.setText("Winner Player 2!")
                x = self.msg.exec_()
                self.pickNumber.setEnabled(False)
        self.player2_score.setText(str(self.player_2_score))

    ## Member function that handles the translation of the string properties of the form
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "                                                                                                                           TOMBALA"))
        self.playerName1.setText(_translate("MainWindow", "PLAYER1"))
        self.PlayerName2.setText(_translate("MainWindow", "PLAYER1"))
        self.takeStamp_1.setText(_translate("MainWindow", "Take Stamp"))
        self.takeStamp_2.setText(_translate("MainWindow", "Take Stamp"))
        self.initializeNumbers.setText(_translate("MainWindow", "Initialize Numbers"))
        self.pickNumber.setText(_translate("MainWindow", "Pick Number"))
        self.player2.setText(_translate("MainWindow", "PLAYER 2"))
        self.player1.setText(_translate("MainWindow", "PLAYER 1"))
        self.pickedNumber.setText(_translate("MainWindow", "PICKED NUMBER"))
        self.player2_score.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.player1_score.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">0</p></body></html>"))
        self.pickedStamp.setText(_translate("MainWindow", "0"))
        self.cardSelect_2.setItemText(0, _translate("MainWindow", "Blue"))
        self.cardSelect_2.setItemText(1, _translate("MainWindow", "Green"))
        self.cardSelect_2.setItemText(2, _translate("MainWindow", "Lila"))
        self.cardSelect_2.setItemText(3, _translate("MainWindow", "Pink"))
        self.cardSelect_1.setItemText(0, _translate("MainWindow", "Claret Red"))
        self.cardSelect_1.setItemText(1, _translate("MainWindow", "Purple"))
        self.cardSelect_1.setItemText(2, _translate("MainWindow", "Red"))
        self.cardSelect_1.setItemText(3, _translate("MainWindow", "Yellow"))
        self.information.setText(_translate("MainWindow", "Information"))
        self.play.setText(_translate("MainWindow", "PLAY"))
        self.exit.setText(_translate("MainWindow", "EXIT"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionMenu.setText(_translate("MainWindow", "Menu"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))