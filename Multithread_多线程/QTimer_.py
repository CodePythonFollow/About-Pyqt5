#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTimer_.py
@time: 2020/4/27 11:37

计时器
timer  是一个线程对象
timer.timeout是绑定的线程事件

start开始线程，每隔1000毫秒执行
end  结束线程
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Timer(QWidget):
    def __init__(self):
        super(Timer, self).__init__()
        self.setWindowTitle('计时器控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(600, 500)
        self.unit_ui()

    def unit_ui(self):
        layout = QGridLayout()
        self.setLayout(layout)

        # 计时器控件
        self.timer = QTimer()
        # 显示时间
        self.timer.timeout.connect(self.showtime)

        # 放置显示时间的label
        self.label = QLabel('等待开始')
        self.label.setFont(QFont('Arial', 20))
        layout.addWidget(self.label, 0, 0, 1, 3)

        # 起始和终止按钮
        self.start_button = QPushButton('开始')
        self.end_button = QPushButton('结束')
        self.delay_start = QPushButton('5秒后开始')
        layout.addWidget(self.start_button, 1, 0)
        layout.addWidget(self.end_button, 1, 1)
        layout.addWidget(self.delay_start, 1, 2)

        # 点击事件
        self.start_button.clicked.connect(self.start_event)
        self.end_button.clicked.connect(self.end_event)
        self.delay_start.clicked.connect(self.single_shot)

    # 每个线程事件
    def showtime(self):
        # 也可写'yyyy-MM-dd ··· 'ctrl+alt+b查看自带的样式        self.label.setText(time)
        time = QDateTime.currentDateTime().toString(Qt.DateFormat(5))
        self.label.setText(time)

    # 开始线程，设置每次运行事件1000毫秒
    def start_event(self):
        self.timer.start(1000)
        # 将开始按钮设置不可点击防止多开
        self.start_button.setEnabled(False)
        self.end_button.setEnabled(True)

    def end_event(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.end_button.setEnabled(False)

    def single_shot(self):
        self.timer.singleShot(5000, self.start_event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Timer()
    main_window.show()
    sys.exit(app.exec_())
