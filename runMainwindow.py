#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: runMainwindow、.py
@time: 2020/4/2 16:38
'''

from PyQt5.QtWidgets import QApplication, QMainWindow
import signalSlot
import sys

if __name__ == '__main__':
    # 应用绑定到系统
    app = QApplication(sys.argv)
    # 主界面
    mainwindow = QMainWindow()
    # 设置布局
    ui = signalSlot.Ui_MainWindow()
    ui.setupUi(mainwindow)
    # 显示界面
    mainwindow.show()
    # 终端等待界面退出，否则闪退
    sys.exit(app.exec_())