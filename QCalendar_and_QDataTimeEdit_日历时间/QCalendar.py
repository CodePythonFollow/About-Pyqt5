#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: Calendar.py
@time: 2020/4/13 23:01

日历控件
"""

import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class Calendar(QWidget):
    def __init__(self):
        super(Calendar, self).__init__()
        self.label = QLabel(self)
        self.unit_ui()

    def unit_ui(self):
        self.setWindowTitle('日历控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 500)

        # 日历控件
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)   # 网格显示
        calendar.move(80, 10)
        calendar.setFixedSize(600, 400)
        data = calendar.selectedDate()

        # 显示当前选定的时间
        self.label.setText(data.toString('yyyy-MM-dd dddd'))
        self.label.move(80, 480)

        calendar.clicked.connect(self.show_data)

    def show_data(self, data):
        # print(data)
        self.label.setText(data.toString('yyyy-MM-dd dddd'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Calendar()
    main_window.show()
    sys.exit(app.exec_())

