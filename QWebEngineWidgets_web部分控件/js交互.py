#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: js交互.py
@time: 2020/5/2 23:31
"""


import os
import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('显示本地网页')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(1500, 700)
        self.unit_ui()

    def unit_ui(self):
        self.browser = QWebEngineView()
        # 得到当前文件目录   由于Qurl不识别相对路径
        url = os.getcwd()
        # print(url)
        self.browser.load(QUrl.fromLocalFile(url + '/测试.html'))
        self.layout().addWidget(self.browser)

        # button调用js
        button = QPushButton('改变颜色')
        self.layout().addWidget(button)
        button.move(800, 50)
        button.clicked.connect(self.get_div)

    # 调用js
    def get_div(self):
        self.browser.page().runJavaScript('get_p()', self.callback)

    # js回调
    @staticmethod
    def callback(result):
        print(result)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WebEngineView()
    main_window.show()
    sys.exit(app.exec_())
