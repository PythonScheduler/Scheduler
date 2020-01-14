from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
import sys

class CalWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #프레임 설정
        self.setWindowTitle('달력')
        self.setGeometry(890, 200, 500, 500)
        layout = QVBoxLayout(self)
        #달력
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        #cal.clicked[QDate].connect(self.showDate)
        layout.addWidget(cal)
        # 라벨
       # self.callabel = QLabel(self)
       # date = cal.selectedDate()
       # self.callabel.setText(date.tostring())
       # layout.addWidget(self.callabel)
        # 텍스트박스
       # textedit = QTextEdit(self)
       # layout.addWidget(textedit)
        #버튼 확인부분
        btnOK = QPushButton("확인")
        btnOK.clicked.connect(self.onOKButtonClicked)
        layout.addWidget(btnOK)
        #버튼 취소부분
        btnCancel = QPushButton("취소")
        btnCancel.clicked.connect(self.onCancelButtonClicked)
        layout.addWidget(btnCancel)

        self.setLayout(layout)

    def showDate(self, date):
        self.callabel.setText(date.tostring())
    def onOKButtonClicked(self):
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
    def showModal(self):
        return super().exec_()