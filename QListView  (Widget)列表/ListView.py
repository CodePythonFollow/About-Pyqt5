#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: ListView.py
@time: 2020/4/20 11:09
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ListView(QWidget):

    def __init__(self):
        super(ListView, self).__init__()
        self.setWindowTitle('列表控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(500, 300)
        self.unit_ui()

    def unit_ui(self):
        # 列表视图
        list_view = QListView(self)
        # 列表数据
        model = QStringListModel()
        model.setStringList(['row1', 'row2', 'row3'])
        # 绑定
        list_view.setModel(model)

        # 可以按住ctrl发现clicked里面有个QModelIndex对象
        list_view.clicked.connect(self.get_index)

    @staticmethod
    def get_index(index):
        # 可看到是QModelIndex对象我们可以进入写一个这个对象来查看它的方法
        # print(index)
        # a = QModelIndex()   可以看到有关方法
        # 弹出消息对话框  并阻塞
        QMessageBox(QMessageBox.Icon(4), '您选择了：', index.data(),
                    QMessageBox.Yes | QMessageBox.No).exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ListView()
    main_window.show()
    sys.exit(app.exec_())
