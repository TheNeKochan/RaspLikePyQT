import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from widgets.ScheduleContainer import ScheduleContainer

app = QApplication(sys.argv)
win = QMainWindow()
base = ScheduleContainer()
win.resize(300, 500)
win.setCentralWidget(base)
win.setMinimumSize(300, 500)
win.show()
sys.exit(app.exec_())
