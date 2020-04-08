#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QMessageBox_.py
@time: 2020/4/9 0:54

消息对话框
1. 关于对话框
2. 错误对话框
3. 警告对话框
4. 提问对话框
5. 消息对话框
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class MessageBox(QWidget):
    def __init__(self):
        super(MessageBox, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('下拉框')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.button1 = QPushButton(self)  # 相当于加入了窗体
        self.button1.setText('关于对话框')
        layout.addWidget(self.button1)
        self.button1.clicked.connect(self.alter)

        self.button2 = QPushButton(self)  # 相当于加入了窗体
        self.button2.setText('消息对话框')
        layout.addWidget(self.button2)
        self.button2.clicked.connect(self.alter)

        self.button3 = QPushButton(self)  # 相当于加入了窗体
        self.button3.setText('警告对话框')
        layout.addWidget(self.button3)
        self.button3.clicked.connect(self.alter)

        self.button4 = QPushButton(self)  # 相当于加入了窗体
        self.button4.setText('错误对话框')
        layout.addWidget(self.button4)
        self.button4.clicked.connect(self.alter)

        self.button5 = QPushButton(self)  # 相当于加入了窗体
        self.button5.setText('提问对话框')
        layout.addWidget(self.button5)
        self.button5.clicked.connect(self.alter)

        # self.button2.move(100, 50)


    def alter(self):
        sender = self.sender()
        if sender.text() == '关于对话框':
            QMessageBox.about(self, '关于', '这是一个关于对话框')
        elif sender.text() == '消息对话框':
            reply = QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply == QMessageBox.Yes)
        elif sender.text() == '警告对话框':
            QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        elif sender.text() == '错误对话框':
            QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        else:
            QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MessageBox()
    mainwindow.show()
    sys.exit(app.exec_())
