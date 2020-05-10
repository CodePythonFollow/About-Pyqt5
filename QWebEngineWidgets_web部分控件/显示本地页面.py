#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: 显示本地页面.py
@time: 2020/5/2 23:10
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
        browser = QWebEngineView()
        # 得到当前文件目录   由于Qurl不识别相对路径
        url = os.getcwd()
        print(url)
        browser.load(QUrl.fromLocalFile(url + '/测试.html'))
        self.setCentralWidget(browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WebEngineView()
    main_window.show()
    sys.exit(app.exec_())
