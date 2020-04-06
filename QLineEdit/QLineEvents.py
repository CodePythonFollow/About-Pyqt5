#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QLineEvents.py
@time: 2020/4/6 17:30
'''
from PyQt5.QtGui import QIntValidator, QFont, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit
from PyQt5.QtCore import Qt
import sys

class InputEvevts(QWidget):
    def __init__(self):
        super(InputEvevts, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QLine综合案例')
        formlayout = QFormLayout()

        # edit使用int检验   最多一个四位数
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial', 20))
        formlayout.addRow('数字(四位)：', edit1)

        # edit2设置float检验
        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99, 99.99, 2))
        edit2.setAlignment(Qt.AlignRight)
        edit2.setFont(QFont('Arial', 15))
        formlayout.addRow('支持浮点数：', edit2)

        # edit3设置掩码
        edit3 = QLineEdit()
        edit3.setInputMask('000-000-000;#')
        edit3.setAlignment(Qt.AlignRight)
        edit3.setFont(QFont('Arial', 15))
        formlayout.addRow('数字掩码：', edit3)

        # edit4设置文本变化信号槽
        edit4 = QLineEdit()
        # 实时打印
        edit4.textChanged.connect(self.textchange)
        formlayout.addRow('text回调数字：', edit4)

        # edit5密码类型信号槽 回显
        edit5 = QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        formlayout.addRow('&Password(alt + p) 写完打印完成：', edit5)
        # 编辑完打印
        edit5.editingFinished.connect(self.printPw)

        self.setLayout(formlayout)

        # 只读模式
        edit6 = QLineEdit('Hello Word')
        edit6.setReadOnly(True)
        formlayout.addRow('只读模式：', edit6)


    def textchange(self, text):
        print(text)

    def printPw(self):
        print('已输入值')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = InputEvevts()
    mainwindow.show()
    sys.exit(app.exec_())