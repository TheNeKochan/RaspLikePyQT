from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush, QFont
from PyQt5.QtWidgets import QTableWidget, \
                            QTableWidgetItem, \
                            QAbstractItemView
from widgets.WidgetTools import WidgetTools


class DayScheduleRowLesson(QTableWidget):
    def __init__(self, width: int, height: int, data: dict):
        super().__init__(2, 1)
        WidgetTools.setup_table_widget(self)
        self.setFixedSize(width, height)
        self.setRowHeight(0, height // 2)
        self.setRowHeight(1, height // 2)
        self.setColumnWidth(0, width)
        lesson_n = QTableWidgetItem(data['lesson_name'])
        lesson_n.setTextAlignment(Qt.AlignLeft + Qt.AlignBottom)
        lesson_n.setForeground(QBrush(QColor(35, 35, 123)))
        lesson_n.setFont(QFont('Arial', 10, QFont.Bold))
        self.setItem(0, 0, lesson_n)

        teacher_cabinet_view = QTableWidget(1, 2)
        WidgetTools.setup_table_widget(teacher_cabinet_view)
        teacher_cabinet_view.setFixedSize(width, height // 2)

        teacher_t = QTableWidgetItem(data['teacher'])
        teacher_t.setTextAlignment(Qt.AlignLeft + Qt.AlignTop)
        teacher_t.setForeground(QBrush(QColor(52, 87, 81)))
        teacher_t.setFont(QFont('Arial', 10, italic=True))
        teacher_cabinet_view.setItem(0, 0, teacher_t)

        cabinet_t = QTableWidgetItem(f"({data['cabinet']})")
        cabinet_t.setTextAlignment(Qt.AlignLeft + Qt.AlignTop)
        cabinet_t.setFont(QFont('Arial', 10, QFont.Bold))
        teacher_cabinet_view.setItem(0, 1, cabinet_t)

        teacher_cabinet_view.resizeColumnsToContents()

        self.setCellWidget(1, 0, teacher_cabinet_view)


class DayScheduleRowTime(QTableWidget):
    def __init__(self, width: int, height: int, begin: str, end: str):
        super().__init__(2, 1)
        WidgetTools.setup_table_widget(self)
        self.setFixedSize(width, height)
        self.setRowHeight(0, height // 2)
        self.setRowHeight(1, height // 2)
        self.setColumnWidth(0, width)
        begin_t = QTableWidgetItem(begin)
        begin_t.setTextAlignment(Qt.AlignHCenter + Qt.AlignBottom)
        begin_t.setForeground(QBrush(QColor(41, 108, 41)))
        self.setItem(0, 0, begin_t)
        end_t = QTableWidgetItem(end)
        end_t.setTextAlignment(Qt.AlignHCenter + Qt.AlignTop)
        end_t.setForeground(QBrush(QColor(41, 108, 41)))
        self.setItem(1, 0, end_t)


class DayScheduleRow(QTableWidget):
    def __init__(self, width, height, data: dict):
        super().__init__(1, 3)
        WidgetTools.setup_table_widget(self)
        self.setFixedSize(width, height)
        self.setRowHeight(0, height)
        self.setColumnWidth(0, 20)
        self.setColumnWidth(1, 35)
        self.setColumnWidth(2, width - 55)
        line_n = QTableWidgetItem(data['index'])
        line_n.setTextAlignment(Qt.AlignCenter)
        line_n.setFont(QFont('Arial', 10, QFont.Bold))
        line_n.setForeground(QBrush(QColor(170, 170, 170)))
        self.setItem(0, 0, line_n)
        self.setCellWidget(0, 1, DayScheduleRowTime(35, height, data['time']['begin'], data['time']['end']))
        self.setCellWidget(0, 2, DayScheduleRowLesson(width - 55, height, data['lesson']))
        # print(self.size(), self.columnWidth(0), height)


class DaySchedule(QTableWidget):
    def __init__(self, width: int, min_height: int, lessons: list):
        n_rows = len(lessons)
        super().__init__(n_rows, 1)
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFocusPolicy(Qt.NoFocus)
        self.setStyleSheet("border: 0px")
        self.setFixedWidth(width)
        self.setMinimumHeight(min_height)
        self.setColumnWidth(0, width)
        self.setShowGrid(True)
        self.__width = width
        for i in range(n_rows):
            row = DayScheduleRow(width, 40, lessons[i])
            self.setRowHeight(i, row.height() + 1)
            self.setCellWidget(i, 0, row)

    def updateData(self, lessons: list) -> None:
        n_rows = len(lessons)
        self.setRowCount(n_rows)
        for i in range(n_rows):
            row = DayScheduleRow(self.__width, 40, lessons[i])
            self.setRowHeight(i, row.height() + 1)
            self.setCellWidget(i, 0, row)
