from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, \
                            QPushButton
from widgets.WidgetTools import WidgetTools


class ScheduleButtons(QTableWidget):
    def __init__(self, width, height):
        super().__init__(1, 2)
        WidgetTools.setup_table_widget(self)
        self.setShowGrid(True)
        self.setFixedSize(width, height)
        self.setRowHeight(0, height)
        self.setColumnWidth(0, width // 2)
        self.setColumnWidth(1, width // 2)
        self.setStyleSheet('border: 0')

        gradient = "background-color: qlineargradient(spread:pad,x1:0 y1:0, x2:0 y2:1,stop:0 #2ca8f0,stop:1 #1c67a1); color: white"
        gradient_selected = "background-color: qlineargradient(spread:pad,x1:0 y1:0, x2:0 y2:1,stop:0 #60a9ca,stop:1 #63a4b8); color: #1c67a1"
        button_width = (width // 2) - 1

        self.CalendarButton = QPushButton("Календарь")
        self.CalendarButton.setFont(QFont("Arial", 10, QFont.Bold))
        self.CalendarButton.setFixedSize(button_width, height)
        self.CalendarButton.setStyleSheet(gradient)
        self.setCellWidget(0, 0, self.CalendarButton)

        self.MyClassButton = QPushButton("Это мой класс")
        self.MyClassButton.setFont(QFont("Arial", 10, QFont.Bold))
        self.MyClassButton.setFixedSize(button_width, height)
        self.MyClassButton.setStyleSheet(gradient_selected)
        self.setCellWidget(0, 1, self.MyClassButton)
