import sys, datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from CalWindow import CalWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #디자인부분
        now = datetime.datetime.now()
        self.Headlabel = QLabel(now.strftime('Today: %Y-%m-%d'), self)
        self.Headlabel.move(10, 0)
        self.Headlabel.resize(150, 30)
        self.calbtn = QPushButton('달력', self)
        self.calbtn.move(30, 30)
        self.calbtn.clicked.connect(self.calshow)

        self.setGeometry(1400,200, 400, 500)
        self.setWindowTitle('스케줄러')
        self.show()

    def calshow(self):
        win = CalWindow()
        r = win.showModal()


    def show(self):
        super().show()