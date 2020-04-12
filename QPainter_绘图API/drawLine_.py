#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: drawLine_.py
@time: 2020/4/11 23:45

绘制不同类型的直线
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QPen


class DrawLine(QWidget):
    def __init__(self):
        super(DrawLine, self).__init__()
        self.setWindowTitle('绘制不同的线')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(pen)

        painter.drawLine(20, 80, 780, 80)

        pen.setStyle(Qt.DashLine)
        painter.setPen(pen)
        painter.drawLine(20, 100, 780, 100)

        pen.setStyle(Qt.DashDotDotLine)
        painter.setPen(pen)
        painter.drawLine(20, 120, 780, 120)

        pen.setStyle(Qt.DotLine)
        painter.setPen(pen)
        painter.drawLine(20, 140, 780, 140)

        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1, 2, 3, 4])
        painter.setPen(pen)
        painter.drawLine(20, 160, 780, 160)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DrawLine()
    main_window.show()
    sys.exit(app.exec_())
