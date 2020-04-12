#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: drawPoint_.py
@time: 2020/4/11 16:12

绘制像素点
"""

import sys
import math

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter


class DrawPoint(QWidget):
    def __init__(self):
        super(DrawPoint, self).__init__()
        self.setWindowTitle('绘制像素点')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        painter.setFont(QFont('SimSun', 50))

        for i in range(1001):
            x = self.width()/2 - 250 + i / 2
            y = (self.height()/2) + 100 * math.sin(4 * math.pi/1000 * i)
            painter.drawPoint(x, y)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DrawPoint()
    main_window.show()
    sys.exit(app.exec_())


