#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: statusbar.py
@time: 2020/4/14 22:33

状态栏
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class StatusBar(QMainWindow):

    def __init__(self):
        super(StatusBar, self).__init__()
        self.setWindowTitle('工具栏')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(500, 400)
        self.unit_ui()

    def unit_ui(self):

        menu = QMenu('菜单', self)
        self.menuBar().addMenu(menu)
        action = QAction(QIcon('../images/new.png'), '新建', self)
        menu.addAction(action)
        menu.triggered.connect(self.status_change)

    def status_change(self, action):
        # 创建菜单栏，跟随事件显示消息
        status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        if action.text() == '新建':
            ''' showMessage(self, str, msecs: int = 0) 毫秒'''
            status_bar.showMessage('新建一个文件', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = StatusBar()
    main_window.show()
    sys.exit(app.exec_())
