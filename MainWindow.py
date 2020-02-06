
import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
from SchedulDialog import ScheduleDialog

path = 'C:/PythonScheduler'

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dialog = ScheduleDialog() # 다이얼로그는 별개로 생성

    def initUI(self):
        self.createEveryday() # 최초 실행 시 파일 체크. 없으면 생성

        # 그룹박스 layout에 추가 (Grid)
        grid = QGridLayout()
        grid.addWidget(self.createCalendarBox(),0,0,3,4)
        grid.addWidget(self.createToDoBox(),0,4,3,2)
        self.setLayout(grid)

        self.readEveryday() # 텍스트 브라우저에 파일 읽어옴


    # Calendar 박스 생성 함수
    def createCalendarBox(self):
        groupBox = QGroupBox('Calendar')
        groupBox.setFlat(True) # 테두리 없음

        self.cal = QCalendarWidget(self) # self 쓰지 않으면 다른 메소드에서 사용에 문제됨
        self.cal.setGridVisible(True)

        self.cal.activated[QDate].connect(self.showDialog) # 더블 클릭
        self.cal.clicked[QDate].connect(self.showDate) # 한번 클릭

        self.lb = QLabel(self) # 날짜 출력할 라벨
        date = self.cal.selectedDate() # 처음에 출력할 때
        self.lb.setText(date.toString())

        calendarBox = QVBoxLayout()
        calendarBox.addWidget(self.cal)
        calendarBox.addWidget(self.lb)
        # calendarBox.addStretch() 한쪽으로 미는 효과?
        groupBox.setLayout(calendarBox)

        return groupBox


    # ToDo 박스 생성 함수
    def createToDoBox(self):
        groupBox = QGroupBox('ToDo')

        self.everydayLb = QLabel(self)
        self.everydayLb.setText('# Everyday')

        self.everyday = QTextBrowser()
        self.everyday.setAcceptRichText(True) # 서식 있는 텍스트 입력 가능
        self.everyday.setOpenExternalLinks(True) # 하이퍼링크 연결 가능

        self.checkLb = QLabel(self)
        self.checkLb.setText('# Day to Day')

        self.check = QTextBrowser()
        self.check.setAcceptRichText(True)
        self.check.setOpenExternalLinks(True)

        # 수정 버튼
        self.modifyBtn = QPushButton('Modification')
        self.modifyBtn.clicked.connect(self.showDialog) # 다이얼로그 불러오고 텍스트 브라우저 최신화

        toDoBox = QVBoxLayout()
        toDoBox.addWidget(self.everydayLb)
        toDoBox.addWidget(self.everyday)
        toDoBox.addWidget(self.checkLb)
        toDoBox.addWidget(self.check)
        toDoBox.addWidget(self.modifyBtn)
        groupBox.setLayout(toDoBox)

        return groupBox

    # 날짜를 라벨에 보여주는 함수
    def showDate(self, date):
        self.lb.setText(date.toString())

    # 최초 실행시 폴더와 파일 체크하고 없으면 생성
    def createEveryday(self):
        if not os.path.isdir(path): # 폴더 없으면 폴더 생성
            os.mkdir(path)
        elif not os.path.isfile(path + '/Everyday.txt'): # 폴더 있고, 파일 없으면 파일 생성
        # 메모장이 사전에 존재하거나 새로 만들때? 문제 또는 예외 처리 / 직접 접근할때
            with open(path + '/Everyday.txt', 'w') as f:
                f.write('')

    # 메모장 읽어들여서 텍스트 브라우저에 출력하는 함수
    def readEveryday(self):
        with open(path + '/Everyday.txt', 'r') as f:
            self.list = f.read()
            self.everyday.append(self.list)

    # dialog 호출하고 텍스트 브라우저 초기화 함수
    def showDialog(self):
        self.dialog.exec() # 포커스 텍스트브라우저로 
        self.everyday.clear()
        self.readEveryday()