#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: toolbar.py
@time: 2020/4/14 18:29

工具栏

工具栏默认按钮：只显示图标，将文本作为悬停提示展示

工具栏按钮有3种显示状态

1.  只显示图标
2.  只显示文本
3.  同时显示文本和图标
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Toolbar(QWidget):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.setWindowTitle('工具栏')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(500, 400)
        self.unit_ui()

    def unit_ui(self):

        file_toolbar = QToolBar(self)
        file_toolbar.setObjectName('File')
        file_toolbar.move(0, 0)
        new = QAction(QIcon('../images/new.png'), 'new', self)
        file_toolbar.addAction(new)

        edit_toolbar = QToolBar(self)
        edit_toolbar.setObjectName('Edit')
        edit_toolbar.move(50, 0)
        open_ = QAction(QIcon('../images/open.png'), 'open', self)
        edit_toolbar.addAction(open_)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Toolbar()
    main_window.show()
    sys.exit(app.exec_())
