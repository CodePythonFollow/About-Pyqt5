#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: FillRect.py
@time: 2020/4/12 20:00

用笔刷填充
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QBrush


class DrawRect(QWidget):
    def __init__(self):
        super(DrawRect, self).__init__()
        self.setWindowTitle('用笔刷填充区域')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)

        brush = QBrush(Qt.Dense1Pattern)
        painter.setBrush(brush)
        painter.drawRect(30, 20, 100, 100)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DrawRect()
    main_window.show()
    sys.exit(app.exec_())
