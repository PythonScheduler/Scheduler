
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QCalendarWidget, QDesktopWidget, QGridLayout,
                             QGroupBox, QTextBrowser, QPushButton, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('"야 꿀벌"')  # ('Scheduler')
        self.setWindowIcon(QIcon('bee.png'))

        grid = QGridLayout()
        grid.addWidget(self.createCalendarBox(),0,0,3,4)
        grid.addWidget(self.createToDoBox(),0,4,3,2)
        self.setLayout(grid)

        self.center_and_size()
        self.show()  # 순서 구애 받음

    # 달력 박스 생성 함수
    def createCalendarBox(self):
        groupBox = QGroupBox('Calendar')
        groupBox.setFlat(True)

        self.cal = QCalendarWidget(self) # self 쓰지 않으면 다른 메소드에서 사용에 문제됨
        self.cal.setGridVisible(True)
        self.cal.clicked[QDate].connect(self.showDate)

        self.lb = QLabel(self)
        date = self.cal.selectedDate()
        self.lb.setText(date.toString())

        calendarBox = QVBoxLayout()
        calendarBox.addWidget(self.cal)
        calendarBox.addWidget(self.lb)
        calendarBox.addStretch()
        groupBox.setLayout(calendarBox)

        return groupBox

    # ToDo 박스 생성 함수
    def createToDoBox(self):
        groupBox = QGroupBox('ToDo')

        self.everydayLb = QLabel(self)
        self.everydayLb.setText('매일 할 일')

        self.everyday = QTextBrowser()
        self.everyday.setAcceptRichText(True)
        self.everyday.setOpenExternalLinks(True)

        self.checkLb = QLabel(self)
        self.checkLb.setText('체크')

        self.check = QTextBrowser()
        self.check.setAcceptRichText(True)
        self.check.setOpenExternalLinks(True)

        # 확인 버튼
        self.btnOK = QPushButton('확인')
        # btnOK.clicked.connect(self.함수추가)

        # 취소 버튼
        self.btnCancel = QPushButton('취소')
        # btnOK.clicked.connect(self.함수추가)

        toDoBox = QVBoxLayout()
        toDoBox.addWidget(self.everydayLb)
        toDoBox.addWidget(self.everyday)
        toDoBox.addWidget(self.checkLb)
        toDoBox.addWidget(self.check)
        toDoBox.addWidget(self.btnOK)
        toDoBox.addWidget(self.btnCancel)
        groupBox.setLayout(toDoBox)

        return groupBox

    # 날짜를 라벨에 보여주는 함수
    def showDate(self, date):
        self.lb.setText(date.toString())

    # 프로그램을 모니터 중앙에 배치하고 사이즈 지정 함수(시작할 때)
    def center_and_size(self):
        self.setFixedSize(750,550) # 창크기 고정
        #self.resize(750, 550)

        # 프로그램을 모니터 중앙에 배치
        frameInfo = self.frameGeometry()  # 창의 위치와 크기 정보
        center = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치
        frameInfo.moveCenter(center)  # 창크기의 직사각형을 중앙으로 설정
        self.move(frameInfo.topLeft())  # 창을 직사각형으로 이동

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

# 해결할 것들

# 텍스트 브라우저 하나(체크버튼 기능), 버튼 2개(성덕이 짠거, 여기에 다이얼로그 연결) 추가하기
# QmainWindow?
# accpet, reject -> Dialog 문제
# 배경색

# def onOKButtonClicked(self):
    #     self.accept()
    # def onCancelButtonClicked(self):
    #     self.reject()
    # def showModal(self):
    #     return super().exec_()