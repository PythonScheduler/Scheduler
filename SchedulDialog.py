from PyQt5.QtWidgets import (QVBoxLayout, QTextEdit, QPushButton, QDialog)
from PyQt5.QtCore import QDate
import sys

class SchedulDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #프레임 설정
        self.setWindowTitle('스케줄 추가하기')
        self.setGeometry(890, 200, 500, 500)
        layout = QVBoxLayout(self)

        #textedit 부분
        self.lineedit = QTextEdit(self)
        layout.addWidget(self.lineedit)
        #버튼 확인부분
        btnOK = QPushButton("확인")
        btnOK.clicked.connect(self.onOKButtonClicked)
        layout.addWidget(btnOK)
        #버튼 취소부분
        btnCancel = QPushButton("취소")
        btnCancel.clicked.connect(self.onCancelButtonClicked)
        layout.addWidget(btnCancel)

        self.setLayout(layout)

    #확인 시 text 저장
    def onOKButtonClicked(self):
        with open('test.txt', 'w') as f:
            my_text = self.lineedit.toPlainText()
            f.write(my_text)
            f.close()
        self.accept()
    def onCancelButtonClicked(self):
        self.reject()
    def showModal(self):
        return super().exec_()