#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QMdi_多子窗口.py
@time: 2020/4/26 23:28

QMdiArea   容器

QMdiSubWindow   子窗口容器

子窗口排版
.cascadeSubWindow  折叠
.tileSubWindow     平铺
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MdiArea(QMainWindow):

    def __init__(self):
        super(MdiArea, self).__init__()
        self.setWindowTitle('多子窗口控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(600, 500)
        self.unit_ui()
        self.count = 0

    def unit_ui(self):
        # 设置容器
        self.mdi_area = QMdiArea()
        self.setCentralWidget(self.mdi_area)

        # 设置菜单栏7
        menu = QMenu('文件', self)
        self.menuBar().addMenu(menu)
        menu.addActions([QAction('新建', self), QAction('折叠', self), QAction('平铺', self)])

        # 三种状态触发事件
        menu.triggered.connect(self.event_)

    def event_(self, action):

        if action.text() == '新建':
            # 子窗口
            sub_window_num = self.count + 1
            # 创建子窗口
            sub_window = QMdiSubWindow()
            # 子窗口设置空间
            sub_window.setWidget(QTextEdit())
            # 设置子窗口标题
            sub_window.setWindowTitle('子窗口' + str(sub_window_num))
            # 将子窗口加入到容器
            self.mdi_area.addSubWindow(sub_window)
            # 显示子窗口
            sub_window.show()

        elif action.text() == '折叠':
            # 重叠方法(级联)
            self.mdi_area.cascadeSubWindows()

        else:
            self.mdi_area.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MdiArea()
    main_window.show()
    sys.exit(app.exec_())
