"""
@file: tombala.py

@author: Ceren Yaşa

@date: June 3, 2020

@brief: Tombala Game with Qt Designer and Python
"""

from PyQt5 import QtCore, QtGui, QtWidgets

from tombala import Ui_MainWindow

import sys

## The driver main function that executes the program
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QtWidgets.QApplication([])

MainWindow =mywindow()
MainWindow.show()

sys.exit(app.exec_())