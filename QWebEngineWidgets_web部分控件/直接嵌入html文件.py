#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: 直接嵌入html文件.py
@time: 2020/5/2 23:28
"""

import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle('嵌入html')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(1500, 700)
        self.unit_ui()

    def unit_ui(self):
        browser = QWebEngineView()
        browser.setHtml('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>测试</title>
            <style>
                div {
                    width: 500px;
                    height: 300px;
                    background-color: skyblue;
                    margin: 30px auto;
                }
            </style>
        </head>
        <body>
            <h1 align="center">PyQt测试本地页面</h1>
            <div></div>
        </body>
        </html>
        ''')
        self.setCentralWidget(browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = WebEngineView()
    main_window.show()
    sys.exit(app.exec_())
