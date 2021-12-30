from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, \
                            QTableWidget, \
                            QTableWidgetItem, \
                            QHBoxLayout, \
                            QPushButton
from widgets.WidgetTools import WidgetTools
from widgets.QPixmaps import back_pixmap, next_pixmap


class DayInfoSelector(QTableWidget):
    def __init__(self, width, height):
        super().__init__(1, 3)
        WidgetTools.setup_table_widget(self)
        self.setFixedSize(width, height)
        self.setRowHeight(0, height)
        self.setColumnWidth(0, height)
        self.setColumnWidth(1, width - 2 * height)
        self.setColumnWidth(2, height)
        self.setStyleSheet('background-color: qlineargradient(spread:pad,x1:0 y1:0, x2:0 y2:1,stop:0 #dbdbdb,stop:1 #bababa);')

        btn_size = int(round(height * 0.5))

        BackButtonContainer = QWidget()
        BackButtonContainer.setFixedSize(height, height)
        BackButtonBox = QHBoxLayout(BackButtonContainer)
        BackButtonBox.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        BackButton = QPushButton()
        BackButton.setFixedSize(btn_size - 2, btn_size - 2)
        BackButton.setStyleSheet(f'border-radius: {(btn_size - 2) // 2}; border: 2px solid white; background: #959595')
        BackButtonPixmap = back_pixmap()
        BackButtonPixmap = BackButtonPixmap.scaled(btn_size - 12, btn_size - 12)
        BackButton.setIcon(QIcon(BackButtonPixmap))

        BackButtonWidget = QWidget()
        BackButtonWidget.setFixedSize(btn_size, btn_size)
        BackButtonWidget.setStyleSheet(f'border-radius: {btn_size // 2}; background: #959595')
        BackButtonWidgetBox = QHBoxLayout(BackButtonWidget)
        BackButtonWidgetBox.setAlignment(Qt.AlignCenter)
        BackButtonWidgetBox.setContentsMargins(0, 0, 0, 0)
        BackButtonWidgetBox.addWidget(BackButton)

        BackButtonBox.addWidget(BackButtonWidget)
        self.setCellWidget(0, 0, BackButtonContainer)

        NextButtonContainer = QWidget()
        NextButtonContainer.setFixedSize(height, height)
        NextButtonBox = QHBoxLayout(NextButtonContainer)
        NextButtonBox.setAlignment(Qt.AlignVCenter | Qt.AlignRight)

        NextButton = QPushButton()
        NextButton.setFixedSize(btn_size - 2, btn_size - 2)
        NextButton.setStyleSheet(f'border-radius: {(btn_size - 2) // 2}; border: 2px solid white; background: #959595')
        NextButtonPixmap = next_pixmap()
        NextButtonPixmap = NextButtonPixmap.scaled(btn_size - 12, btn_size - 12)
        NextButton.setIcon(QIcon(NextButtonPixmap))

        NextButtonWidget = QWidget()
        NextButtonWidget.setFixedSize(btn_size, btn_size)
        NextButtonWidget.setStyleSheet(f'border-radius: {btn_size // 2}; background: #959595')
        NextButtonWidgetBox = QHBoxLayout(NextButtonWidget)
        NextButtonWidgetBox.setAlignment(Qt.AlignCenter)
        NextButtonWidgetBox.setContentsMargins(0, 0, 0, 0)
        NextButtonWidgetBox.addWidget(NextButton)

        NextButtonBox.addWidget(NextButtonWidget)
        self.setCellWidget(0, 2, NextButtonContainer)

        Text = QTableWidgetItem("Понедельник, 13 Декабря")
        Text.setTextAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        Text.setFont(QFont("Arial", 10, QFont.Bold))
        self.setItem(0, 1, Text)



