#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: ListWidget.py
@time: 2020/4/20 11:44
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ListWidget(QWidget):

    def __init__(self):
        super(ListWidget, self).__init__()
        self.setWindowTitle('列表控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(500, 300)
        self.unit_ui()

    def unit_ui(self):
        list_widget = QListWidget(self)
        list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单一'))
        list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单二'))
        list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单三'))
        list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单四'))

        # 绑定事件
        list_widget.clicked.connect(self.get_index)

    def get_index(self, index):
        QMessageBox.information(self, '菜单', f'您选择的是{index.data()}', QMessageBox.Yes | QMessageBox.No)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ListWidget()
    main_window.show()
    sys.exit(app.exec_())

