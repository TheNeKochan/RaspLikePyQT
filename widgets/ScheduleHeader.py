from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon, QBrush, QFont
from PyQt5.QtWidgets import QWidget, \
    QTableWidget, \
    QTableWidgetItem, \
    QHBoxLayout, \
    QPushButton
from widgets.QPixmaps import home_pixmap
from widgets.WidgetTools import WidgetTools


class ScheduleHeader(QTableWidget):
    def __init__(self, width, height, class_name):
        super().__init__(1, 2)
        WidgetTools.setup_table_widget(self)
        self.setFixedSize(width, height)
        self.setRowHeight(0, height)
        self.setColumnWidth(0, height)
        self.setColumnWidth(1, width - height)
        self.setStyleSheet('background: #1e89d9; border: 0px')

        self.text = QTableWidgetItem(f'РАСПИСАНИЕ {class_name}')
        self.text.setTextAlignment(Qt.AlignCenter)
        self.text.setForeground(QBrush(QColor(255, 255, 255)))
        self.text.setFont(QFont('Arial', 11, QFont.Bold))
        self.setItem(0, 1, self.text)

        self.homeButtonBox = QWidget()
        self.homeButtonBox.setFixedSize(height, height)
        btn_size = int(round(height * 0.75))
        self.homeButton = QPushButton()
        self.homeButton.setFixedSize(btn_size - 2, btn_size - 2)
        self.homeButton.setStyleSheet(f'border-radius: {(btn_size - 2) // 2}; border: 2px solid #38a5e8; background: #124c72')
        pixmap = home_pixmap()
        pixmap = pixmap.scaled(btn_size - 10, btn_size - 10)
        self.homeButton.setIcon(QIcon(pixmap))
        container1 = QHBoxLayout(self.homeButtonBox)
        container1.setContentsMargins(0, 0, 0, 0)
        container1.setAlignment(Qt.AlignCenter)

        btn_widget = QWidget()
        btn_widget.setFixedSize(btn_size, btn_size)
        btn_widget.setStyleSheet(f'border-radius: {btn_size // 2}; background: #124c72')
        container2 = QHBoxLayout(btn_widget)
        container2.setContentsMargins(0, 0, 0, 0)
        container2.setAlignment(Qt.AlignCenter)
        container2.addWidget(self.homeButton)

        container1.addWidget(btn_widget)
        self.setCellWidget(0, 0, self.homeButtonBox)

        self.homeButton.clicked.connect(self.__click_handler)

        def dummy(*args, **kwargs):
            pass

        self.onClick = dummy

    def __click_handler(self):
        self.onClick(self)

    def setOnHomePress(self, handler):
        self.onClick = handler

    def setClassName(self, class_name):
        self.text.setText(f'РАСПИСАНИЕ {class_name}')

