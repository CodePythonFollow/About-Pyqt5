#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: ScrollBar.py
@time: 2020/4/27 10:54

滚动条   控制字体大小  类似之前的滑块

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class ScrollBar(QWidget):
    def __init__(self):
        super(ScrollBar, self).__init__()
        self.setWindowTitle('多子窗口控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(600, 500)
        self.unit_ui()

    def unit_ui(self):

        layout = QHBoxLayout()
        self.setLayout(layout)
        # 创建一个label
        self.label = QLabel('测试文本', self)
        layout.addWidget(self.label)

        # 创建一个滚动条
        scroll = QScrollBar(self)
        scroll.setMaximum(100)
        scroll.setMinimum(10)
        layout.addWidget(scroll)

        scroll.sliderMoved.connect(self.move)

    def move(self, int_value):
        print(int_value)
        self.label.setFont(QFont('Arial', int_value))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ScrollBar()
    main_window.show()
    sys.exit(app.exec_())
