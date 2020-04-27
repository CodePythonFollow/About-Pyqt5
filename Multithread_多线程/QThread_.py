#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QThread_.py
@time: 2020/4/27 12:59

线程类
这里用到信号槽的知识。

写两个信号
        第一个是线程执行完发送的信号  就是每次事件执行完计数加一
        第二个是结束信号，结束时执行的操作，这里是显示消息对话框
"""

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

sec = 0


# 创建线程
class WorkThread(QThread):
    timer = pyqtSignal()   # 每隔1秒发送一次信号
    end = pyqtSignal()     # 计数完成后发送一次信号

    def run(self):
        global sec
        while True:
            self.sleep(1)  # 休眠1秒
            if sec == 10:
                self.end.emit()   # 发送end信号
                break
            self.timer.emit()   # 发送timer信号


# 界面显示部分
class Thread(QWidget):

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
        self.setWindowTitle('计时器控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(600, 500)

        layout = QVBoxLayout()

        # 显示屏控件
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        layout.addWidget(button)

        # 调用线程
        self.workThread = WorkThread()

        # 收到timer信号进行的事件
        self.workThread.timer.connect(self.count_time)
        # 收到end信号进行的事件
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    # 计数事件
    def count_time(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    # 线程调用start方法开始进行
    def work(self):
        self.workThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Thread()
    main_window.show()
    sys.exit(app.exec_())
