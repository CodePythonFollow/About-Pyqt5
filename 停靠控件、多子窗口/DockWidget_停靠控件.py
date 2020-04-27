#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: DockWidget.py
@time: 2020/4/26 21:10

停靠控件
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class DockWidget(QMainWindow):
    def __init__(self):
        super(DockWidget, self).__init__()
        self.setWindowTitle('选项卡控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(600, 500)
        self.unit_ui()

    def unit_ui(self):

        # 首先放一个主控件在窗口
        list_widget = QListWidget()
        list_widget.addItems(['第一行', '第二行', '第三行'])

        # 设置Label成主控件
        self.setCentralWidget(QLabel())

        # 设置一个停靠的控件(这里设置在顶部)
        dock_widget = QDockWidget('停靠控件', self)
        dock_widget.setWidget(list_widget)
        # 默认停靠状态   这里设置为初始浮动
        # dock_widget.setFloating(True)

        # 默认左上方停靠  界面设置停靠控件(这里设置在顶部)   
        self.addDockWidget(Qt.TopDockWidgetArea, dock_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DockWidget()
    main_window.show()
    sys.exit(app.exec_())
