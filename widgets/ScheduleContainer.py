from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, \
                            QAbstractItemView
from widgets.DayInfoSelector import DayInfoSelector
from widgets.DaySchedule import DaySchedule
from widgets.ScheduleButtons import ScheduleButtons
from widgets.ScheduleHeader import ScheduleHeader
from LessonsArray import LessonsArray, Lesson

ls = LessonsArray()
ls.add_lesson(Lesson('физика', 'Заковряшина О.В.', '212', '8:15', '9:00'))
ls.add_lesson(Lesson('физика', 'Заковряшина О.В.', '212', '9:10', '9:55'))
ls.add_lesson(Lesson('физкультура', 'Физкультура 11', 'спортзал4', '10:15', '11:00'))
ls.add_lesson(Lesson('физкультура', 'Физкультура 11', 'спортзал4', '11:15', '12:00'))
ls.add_lesson(Lesson('математика', 'Подолян Е.В.', '209', '12:10', '12:55'))
ls.add_lesson(Lesson('математика', 'Подолян Е.В.', '209', '13:05', '13:50'))
ls.add_lesson(Lesson('математика', 'Подолян Е.В.', '209', '14:00', '14:45'))
ls.add_lesson(Lesson('математика', 'Подолян Е.В.', '209', '14:55', '15:35'))


class ScheduleContainer(QTableWidget):
    def __init__(self):
        super().__init__(4, 1)
        self.verticalHeader().hide()
        self.horizontalHeader().hide()
        self.setFixedSize(300, 500)
        self.setColumnWidth(0, 300)
        self.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setFocusPolicy(Qt.NoFocus)
        self.setShowGrid(False)
        header = ScheduleHeader(300, 30, '11-1')
        self.setCellWidget(0, 0, header)
        self.setRowHeight(0, header.height())
        buttons = ScheduleButtons(300, 60)
        self.setCellWidget(1, 0, buttons)
        self.setRowHeight(1, buttons.height())
        selector = DayInfoSelector(300, 45)
        self.setCellWidget(2, 0, selector)
        self.setRowHeight(2, selector.height())
        schedule = DaySchedule(300, 400, ls.to_list())
        self.setCellWidget(3, 0, schedule)
        self.setRowHeight(3, schedule.height())



