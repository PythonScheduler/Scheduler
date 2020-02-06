
import sys
from MainWindow import MainWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Scheduler')
        self.setWindowIcon(QIcon('python.png'))
        self.center_and_size()

        wid = MainWidget() # QMainWindow에 QWidget을 담는다는 느낌?
        self.setCentralWidget(wid)

        self.show()

    # 프로그램을 모니터 중앙에 배치하고 사이즈 지정 함수(시작할 때)
    def center_and_size(self):
        self.setFixedSize(750, 550)  # 창크기 고정
        # self.resize(750, 550)

        # 프로그램을 모니터 중앙에 배치
        frameInfo = self.frameGeometry()  # 창의 위치와 크기 정보
        center = QDesktopWidget().availableGeometry().center()  # 사용하는 모니터 화면의 가운데 위치
        frameInfo.moveCenter(center)  # 창크기의 직사각형을 중앙으로 설정
        self.move(frameInfo.topLeft())  # 창을 직사각형으로 이동

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())

# 해결할 것들
# 배경색
# 쓰레드?
# 경로 다루기, 메모장 저장 위치
# 달력 내리기
# 날짜나 텍스트브라우저 클릭시 시그널 처리
# 윈도우, 다이얼로그, 위젯
# 크롤링
# 부팅시 시작되는 api, 위치고정, 투명화, 배경화면으로?
# 툴팁 추가
# Focus 설정 문제
# 파일 이름 바꾸기
# 예외 처리

# 변수, 함수 기록해가면서 사용하기