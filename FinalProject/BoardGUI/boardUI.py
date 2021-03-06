# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

EMPTY = 0
BLACK = 1
WHITE = 2
PIECE = 34 ## Even Number

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QIcon, QPalette, QPainter, QBrush
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QLineF, QRectF, Qt
from PyQt5.QtWidgets import QLabel, QMainWindow,QWidget
import os
from chess_board import ChessBoard

class LaBel(QLabel):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)

    def enterEvent(self, e):
       e.ignore()

class Filter(QtCore.QObject):
    def __init__(self):
        super(QtCore.QObject, self).__init__()

    def eventFilter(self, obj, event):
        #print event.type()
        return False

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.move(300,10)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 760, 780))
        self.graphicsView.setObjectName("graphicsView")

        self.scene = QtWidgets.QGraphicsScene()
        #self.scene.addPixmap(QPixmap('C:\\Users\Jiaming Nie\Documents\GitHub\CS534-AI-18S\FinalProject\BoardGUI\source\background.jpg'))
        self.graphicsView.setScene(self.scene)
        #self.graphicsView.setMouseTracking(True)
        self.graphicsView.setCursor(QtCore.Qt.ClosedHandCursor)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 70, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 122, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(790, 190, 81, 31))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(790, 230, 82, 31))
        self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File_Menu = QtWidgets.QMenu(self.menubar)
        self.menu_File_Menu.setObjectName("menu_File_Menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Game = QtWidgets.QAction(MainWindow)
        self.actionSave_Game.setObjectName("actionSave_Game")
        self.actionLoad_Game = QtWidgets.QAction(MainWindow)
        self.actionLoad_Game.setObjectName("actionLoad_Game")
        self.menu_File_Menu.addAction(self.actionSave_Game)
        self.menu_File_Menu.addAction(self.actionLoad_Game)
        self.menubar.addAction(self.menu_File_Menu.menuAction())

        ## Set the chess
        dirname = os.path.dirname(__file__)
        self.graphicsView.black = QPixmap(dirname + '/source/black.png')
        self.graphicsView.white = QPixmap(dirname + '/source/white.png')

        self.graphicsView.setMouseTracking(True)
        MainWindow.setMouseTracking(True)
        self.DrawBackground()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chess Board GUI"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "End"))
        self.radioButton.setText(_translate("MainWindow", "Go"))
        self.radioButton_2.setText(_translate("MainWindow", "Backgammon"))
        self.menu_File_Menu.setTitle(_translate("MainWindow", "&File Menu"))
        self.actionSave_Game.setText(_translate("MainWindow", "Save Game"))
        self.actionLoad_Game.setText(_translate("MainWindow", "Load Game"))

    def DrawBackground(self):

        dirname = os.path.dirname(__file__)

        img = QtGui.QPixmap(dirname + '/source/new_back.jpg')
        self.scene.addPixmap(img)
        w_ = 2
        pen = QtGui.QPen(QtCore.Qt.black,w_)
        lengt = 40
        for i in range(19):
            self.scene.addLine(QLineF(20, 20 + i * lengt, 20 + 18 * lengt, 20 + i * lengt),pen)
            self.scene.addLine(QLineF(20 + i * lengt, 20, 20 + i * lengt, 20 + 18 * lengt),pen)
        radius = 10
        for i in range(3):
            x_cor_1 = 20 + 3 * lengt
            y_cor_1 = 20 + 3 * lengt + i * 6 * lengt

            for j in range(3):
                x_cor = x_cor_1 + j * 6 * lengt
                y_cor = y_cor_1
                #self.scene.addEllipse(QRectF(x_cor - radius, y_cor - radius, x_cor + radius, y_cor + radius),pen)
                self.scene.addEllipse(x_cor -0.5*radius ,y_cor - 0.5*radius, radius,radius,pen,QBrush(QColor(0,0,0)))


class DisplayMW(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.graphicsView.setMouseTracking(True)
        self.filter = Filter()
        #self.ui.graphicsView.installEventFilter(self.filter)
        self.installEventFilter(self.filter)
        #### Black and White

        self.setCursor(Qt.PointingHandCursor)
        self.mouse_point = LaBel(self)  # 将鼠标图片改为棋子
        self.mouse_point.setScaledContents(True)
        self.mouse_point.setPixmap(self.ui.graphicsView.black)  # Black chess piece, human always hold
        self.mouse_point.setGeometry(270, 270, PIECE, PIECE)

        # settings for the mouse
        self.mouse_point.raise_()
        self.setMouseTracking(True)
        self.AI_down = True

        self.chess_board = ChessBoard()
        self.pieces = [LaBel(self) for i in range(361)] # All the chess pieces , 19*19 chess board

        for piece in self.pieces:
            piece.setVisible(True)  # Set Picture Visible
            piece.setScaledContents(True)  #

    def mouseMoveEvent(self, event):
        if event.x() <= 760 and event.y() <= 760:
            self.mouse_point.move(event.x() - PIECE/2,event.y() - PIECE/2)
        #print("Moved")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Pressed")

    def coordinate_transform_map2pixel(self):

        return

    def coordinate_transform_pixel2map(self):

        return



import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # w = QtWidgets.QMainWindow()
    # ex = Ui_MainWindow()
    # ex.setupUi(w)
    # w.show()

    win = DisplayMW()
    win.show()

    sys.exit(app.exec_())