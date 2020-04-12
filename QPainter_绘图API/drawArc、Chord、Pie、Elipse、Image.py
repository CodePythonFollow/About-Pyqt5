#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: drawArc、Chord、Pie、Ellipse、Image.py
@time: 2020/4/12 14:31

# drawArc     弧形
# drawChord   带弦的弧形
# drawPie     扇形
# drawEllipse 椭圆
# drawPolygon 多边形(QPolygon多边形对象)
"""

import sys

from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QPolygon, QImage


class DrawPoint(QWidget):

    def __init__(self):
        super(DrawPoint, self).__init__()
        self.setWindowTitle('绘制各种图形')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(900, 800)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(Qt.blue)
        painter.setFont(QFont('SimSun', 50))

        # 绘制弧形
        rect = QRect(0, 10, 800, 800)    # 位置和大小
        painter.drawArc(rect, 180*16, 30*16)  # rect 区域，0起始位置，50*16表示50度 1度=16a

        # 绘制带弦的弧
        painter.drawChord(rect, 90*16, 30*16)

        # 绘制扇形
        painter.drawPie(10, 240, 100, 100, 12, 120*16)

        # 绘制椭圆
        painter.drawEllipse(50, 50, 50, 100)

        # 绘制多边形(多边形对象)
        point1 = QPoint(130, 120)
        point2 = QPoint(130, 150)
        point3 = QPoint(220, 180)
        point4 = QPoint(220, 170)
        point5 = QPoint(200, 150)
        # 多边形对象
        polygon = QPolygon([point1, point2, point3, point4, point5])
        painter.drawPolygon(polygon)

        # 绘制图片
        image = QImage(QPixmap('../images/ajax-loading.gif'))
        rect = QRect(100, 100, image.width(), image.height())
        painter.drawImage(rect, image)

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DrawPoint()
    main_window.show()
    sys.exit(app.exec_())
