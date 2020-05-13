#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: 对齐方式和伸缩量.py
@time: 2020/5/4 17:09

对齐方式：
    Qt.AlignLeft/Right/Top/Bottom
伸缩量：
    addStretch  里面的数值表示左侧伸缩部分
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Aliment(QWidget):
    def __init__(self):
        super(Aliment, self).__init__()
        self.setWindowTitle('对齐方式和伸缩量')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(1500, 700)
        self.unit_ui()

    def unit_ui(self):
        layout = QHBoxLayout()
        layout.setSpacing(40)
        self.setLayout(layout)
        # layout.addWidget(QPushButton('按钮1'), 2, Qt.AlignLeft | Qt.AlignTop)
        # layout.addWidget(QPushButton('按钮2'), 1, Qt.AlignLeft | Qt.AlignTop)
        # layout.addWidget(QPushButton('按钮3'), 1, Qt.AlignRight | Qt.AlignBottom)
        # layout.addWidget(QPushButton('按钮4'), 1, Qt.AlignRight | Qt.AlignBottom)

        # 这里设置一个伸缩量
        h_layout = QHBoxLayout()
        layout.addLayout(h_layout)
        h_layout.addStretch(0)
        h_layout.addWidget(QPushButton('1'))
        h_layout.addWidget(QPushButton('2'))
        h_layout.addWidget(QPushButton('3'))
        h_layout.addWidget(QPushButton('4'))

        h_layout.addStretch(1)
        h_layout.addWidget(QPushButton('确认'))
        h_layout.addWidget(QPushButton('取消'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Aliment()
    main_window.show()
    sys.exit(app.exec_())
