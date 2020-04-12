#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: drag_drop.py
@time: 2020/4/12 22:46

a: 让a控件支持拖拽 a.setDragEnabled(True)


b: 让b控件支持被拖拽 b.setAcceptDrops(True)
还需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发

实例label的文本拖到下拉框里
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QDragEnterEvent


# 下拉框接收拖拽
class Drag(QComboBox):
    def __init__(self):
        super(Drag, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        print(e)
        self.addItem(e.mimeData().text())


# 主界面下拉框并设置拖拽事件
class ComboBox(QWidget):
    def __init__(self):
        super(ComboBox, self).__init__()
        self.setWindowTitle('拖拽事件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 400)

        layout = QFormLayout()
        self.setLayout(layout)

        # 设置下拉框
        combobox = Drag()

        line_edit = QLineEdit()
        line_edit.setDragEnabled(True)

        layout.addRow(line_edit, combobox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ComboBox()
    main_window.show()
    sys.exit(app.exec_())



