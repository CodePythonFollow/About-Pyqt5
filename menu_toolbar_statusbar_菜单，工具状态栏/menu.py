#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: menu.py
@time: 2020/4/14 17:48

菜单结构
菜单栏： menuBar
    菜单： menu
        操作：Action 快捷键等。
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# 注意QWidget无菜单栏 所以要用的话得创建一个菜单栏，而QMainWindow有所以直接self设置即可
class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.unit_ui()

    def unit_ui(self):
        self.setWindowTitle('菜单栏')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 300)

        # 这里只是给menuBar起个名字，可以直接用self.menu.add***
        bar = self.menuBar()

        project = bar.addMenu('文件')
        project.addAction('新建文件')

        save = QAction('保存文件', self)
        save.setShortcut('Ctrl + S')
        project.addAction(save)

        save.triggered.connect(self.save)

    # 这个a是triggered传入的参数所以a是False进入triggered方法里可看到a默认传参False
    # sender()就是传入了调用该方法的对象之前的匿名函数也是同理。
    def save(self, a):
        print(a)
        print(self.sender())
        print(self.sender().text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Menu()
    main_window.show()
    sys.exit(app.exec_())
