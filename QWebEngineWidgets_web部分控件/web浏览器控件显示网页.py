#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: web浏览器控件显示网页.py
@time: 2020/5/2 22:57
"""

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('显示外部网页控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(1500, 700)
        self.unit_ui()

    def unit_ui(self):
        browser = QWebEngineView()
        browser.load(QUrl('http://www.baidu.com'))
        self.setCentralWidget(browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WebEngineView()
    main_window.show()
    sys.exit(app.exec_())
