from PyQt5.QtWidgets import QTableWidget, QAbstractItemView
from PyQt5.QtCore import Qt


class WidgetTools:
    @staticmethod
    def setup_table_widget(widget: QTableWidget):
        widget.verticalHeader().hide()
        widget.horizontalHeader().hide()
        widget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        widget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        widget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        widget.setFocusPolicy(Qt.NoFocus)
        widget.setShowGrid(False)
        widget.horizontalHeader().setMinimumSectionSize(1)
        widget.verticalHeader().setMinimumSectionSize(1)
