#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: ThreadSignal.py
@time: 2020/5/17 11:11
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Thread(QThread):
    time_show = pyqtSignal(str)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            date = date.toString("yyyy-MM-dd hh:mm:ss")
            self.time_show.emit(str(date))


class ShowTime(QDialog):
    # noinspection PyArgumentList
    def __init__(self):
        super(ShowTime, self).__init__()
        self.setWindowTitle('显示时间')
        self.resize(300, 100)
        self.line = QLineEdit(self)
        self.line.resize(300, 100)
        self.init_ui()

    def init_ui(self):

        thread_time = Thread()
        thread_time.time_show.connect(self.display)
        # 开启线程
        thread_time.start()
        thread_time.wait(1)

    def display(self, data):
        self.line.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ShowTime()
    main_window.show()
    sys.exit(app.exec())
