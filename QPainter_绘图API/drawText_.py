#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: drawText.py
@time: 2020/4/9 23:10

绘制文本
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QColor, QIcon, QPixmap, QPainter


class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('绘制文本')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(300, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(200, 120, 60))
        painter.setFont(QFont('SimSun', 50))

        painter.drawText(event.rect(), Qt.AlignCenter, 'Hello World')
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DrawText()
    main_window.show()
    sys.exit(app.exec_())
