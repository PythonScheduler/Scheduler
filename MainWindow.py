import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QCalendarWidget, QDesktopWidget, QGridLayout,
                             QGroupBox, QTextBrowser, QPushButton, QLabel)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from SchedulDialog import SchedulDialog

class ClickHandler():
    def __init__(self, time):
        self.timer = QTimer()
        self.timer.setInterval(time)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.timeout)
        self.click_count = 0

    def timeout(self):
        if self.click_count > 1:
            win = SchedulDialog()
            r = win.showModal()
            if r:
                self.click_count = 0
        self.click_count = 0

    def __call__(self):
        self.click_count += 1
        if not self.timer.isActive():
            self.timer.start()
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

        self.load_schedul()
        self.center_and_size()
        self.show()  # 순서 구애 받음

    # 달력 박스 생성 함수
    def createCalendarBox(self):
        groupBox = QGroupBox('Calendar')
        groupBox.setFlat(True)

        self.cal = QCalendarWidget(self)  # self 쓰지 않으면 다른 메소드에서 사용에 문제됨
        self.cal.setGridVisible(True)

        self.click_handler = ClickHandler(300)  # 달력 위젯에 클릭 핸들러 넣기 전에
        self.cal.clicked.connect(self.click_handler)  # 더블클릭 감지 핸들러 추가

        calendarBox = QVBoxLayout()
        calendarBox.addWidget(self.cal)
        groupBox.setLayout(calendarBox)

        return groupBox

    # ToDo 박스 생성 함수
    def createToDoBox(self):
        groupBox = QGroupBox('ToDo')

        self.textBrowser = QTextBrowser()
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)

        # 확인 버튼
        self.btnOK = QPushButton('확인')
        # btnOK.clicked.connect(self.함수추가)

        # 취소 버튼
        self.btnCancel = QPushButton('취소')
        # btnOK.clicked.connect(self.함수추가)

        toDoBox = QVBoxLayout()
        toDoBox.addWidget(self.textBrowser)
        toDoBox.addWidget(self.btnOK)
        toDoBox.addWidget(self.btnCancel)
        groupBox.setLayout(toDoBox)

        return groupBox


    def center_and_size(self):
        self.resize(750, 550)

        # 프로그램을 모니터 중앙에 배치
        frameInfo = self.frameGeometry()  # 창의 위치와 크기 정보
        center = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치
        frameInfo.moveCenter(center)  # 창크기의 직사각형을 중앙으로 설정
        self.move(frameInfo.topLeft())  # 창을 직사각형으로 이동

    def load_schedul(self):
        try:
            with open('test.txt', 'r') as f:
                for text in f:
                    self.textBrowser.append(text)
        except:
            self.textBrowser.append('스케줄이 없습니다!')

# 해결할 것들

# 텍스트 브라우저 하나, 버튼 2개(성덕이 짠거, 여기에 다이얼로그 연결) 추가하기
# QmainWindow?
# accpet, reject -> Dialog 문제
