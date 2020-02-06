
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QIcon
import sys

path = 'C:/PythonScheduler'

class EverydayTab(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.textEdit = QTextEdit()
        # self.textEdit.setFocusPolicy(Qt.StrongFocus) # Focus 설정
        # self.textEdit.setFocus()
        layout.addWidget(self.textEdit)

        #textedit 부분
        # 불러와서 읽어놔야 함
        with open(path + '/Everyday.txt', 'r') as f:
            self.str = f.read()
            self.textEdit.append(self.str)

        self.setLayout(layout)

class ScheduleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Modification')
        self.setWindowIcon(QIcon('python.png'))
        self.center_and_size()

        layout = QVBoxLayout()

        # tab 부분
        tabs = QTabWidget()
        # day to day 탭
        # tabs.addTab(,'Check')
        # everyday탭
        self.everydayTab = EverydayTab()
        tabs.addTab(self.everydayTab,'Everyday')
        layout.addWidget(tabs)

        # 다이얼로그 버튼박스 부분
        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.modify)
        buttonbox.rejected.connect(self.reject)
        layout.addWidget(buttonbox)

        self.setLayout(layout)
        #self.exec() # Modal / show()는 Modaless / 모달리스로 하니까 창 바로 사라짐

    #확인 시 text 저장
    def modify(self):
        with open(path + '/Everyday.txt', 'w') as f:
            text = self.everydayTab.textEdit.toPlainText() # public 문제?
            f.write(text)
        self.accept()

    # 창 사이즈 위치
    def center_and_size(self):
        self.setFixedSize(550,550) # 창크기 고정
        #self.resize(750, 550)

        # 프로그램을 모니터 중앙에 배치
        frameInfo = self.frameGeometry()  # 창의 위치와 크기 정보
        center = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치
        frameInfo.moveCenter(center)  # 창크기의 직사각형을 중앙으로 설정
        self.move(frameInfo.topLeft())  # 창을 직사각형으로 이동