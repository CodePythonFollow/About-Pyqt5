#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: windowSignal.py
@time: 2020/5/17 0:19
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WindowSignal(QWidget):

    window_signal = pyqtSignal()

    def __init__(self):
        super(WindowSignal, self).__init__()
        self.resize(500, 300)
        button = QPushButton(self)
        button.setText('关闭')
        button.clicked.connect(self.click_button)
        # 点击信号绑定
        self.window_signal.connect(self.window_click)

    def click_button(self):
        print('button被点击')
        self.window_signal.emit()

    def window_click(self):
        print('window_signal发送了信号')
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WindowSignal()
    main_window.show()
    sys.exit(app.exec_())
