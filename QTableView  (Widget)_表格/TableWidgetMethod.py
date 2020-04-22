#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTableWidgetContextMenu.py
@time: 2020/4/18 12:53

查找符合条件的表格并设置
findItems

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TableWidgetMethod(QWidget):
    def __init__(self):
        super(TableWidgetMethod, self).__init__()
        self.setWindowTitle("在表格中显示上下文菜单")
        self.resize(800, 500)
        self.unit_ui()

    def unit_ui(self):
        table_widget = QTableWidget(self)
        table_widget.setRowCount(30)
        table_widget.setColumnCount(3)
        table_widget.resize(500, 500)
        table_widget.setHorizontalHeaderLabels(['id', 'name', 'old'])
        # 设置行高和列宽
        table_widget.setRowHeight(0, 80)
        table_widget.setColumnWidth(0, 100)
        for r in range(30):
            for c in range(3):
                table_widget.setItem(r, c, QTableWidgetItem(f"({r}, {c})"))
        # 查找以匹配规则开始的item
        items = table_widget.findItems('(1', Qt.MatchStartsWith)
        # 对每个item设置一定的样式
        if items:
            for item in items:
                item.setBackground(QBrush(QPixmap('../images/python.jpg')))
                item.setForeground(QBrush(QColor(255, 0, 0)))
                item.setFont(QFont('SimSun', 15, 10))
                item.setTextAlignment(Qt.AlignRight)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = TableWidgetMethod()
    example.show()
    sys.exit(app.exec_())
