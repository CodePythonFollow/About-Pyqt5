#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: 控件边界拖拽.py
@time: 2020/5/11 14:21

QSplitter

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Splitter(QWidget):
    def __init__(self):
        super(Splitter, self).__init__()
        self.setWindowTitle('对齐方式和伸缩量')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(1500, 700)
        self.unit_ui()

    def unit_ui(self):
        layout = QHBoxLayout()
        self.setLayout(layout)
        splitter = QSplitter()
        splitter.addWidget(QPushButton('11'))
        splitter.addWidget(QPushButton('22'))
        layout.addWidget(splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Splitter()
    main_window.show()
    sys.exit(app.exec_())



