#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QlineValidator.py
@time: 2020/4/4 18:24
Validator 验证器
'''
import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
# 正则验证器，整数和浮点验证器
from  PyQt5.QtGui import QRegExpValidator, QIntValidator, QDoubleValidator
# 导入正则表达式工具
from PyQt5.QtCore import QRegExp

class Validator(QWidget):
    def __init__(self):
        super(Validator, self).__init__()
        self.InitUi()

    def InitUi(self):
        self.setWindowTitle('验证器')

        # 表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        DoubleLineEdit = QLineEdit()
        RegExpLineEdit1 = QLineEdit()
        RegExpLineEdit2 = QLineEdit()

        formLayout.addRow('&IntLineEdit', intLineEdit)
        formLayout.addRow('&DoubleLineEdit', DoubleLineEdit)
        formLayout.addRow('&RegExpLineEdit', RegExpLineEdit1)
        formLayout.addRow('&RegExpLineEdit', RegExpLineEdit2)

        # 提示文本
        intLineEdit.setPlaceholderText('请输入数字')
        DoubleLineEdit.setPlaceholderText('请输入数字')
        RegExpLineEdit1.setPlaceholderText('请输入数字')
        RegExpLineEdit2.setPlaceholderText('请输入数字')

        # 创建验证器对象
        intValidator = QIntValidator()
        intValidator.setRange(1, 999)
        # 创建浮点验证器
        doubleValidator = QDoubleValidator()
        doubleValidator.setRange(1, 999)
        # 标准符号
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        # 保留两位小数
        doubleValidator.setDecimals(2)
        # 创建表达式验证器
        regExp = QRegExpValidator()
        regExp.setRegExp(QRegExp('^[a-zA-Z]*[0-9]{2}'))

        # 设置验证器
        intLineEdit.setValidator(intValidator)
        DoubleLineEdit.setValidator(doubleValidator)
        RegExpLineEdit1.setValidator(regExp)
        RegExpLineEdit2.setValidator(regExp)

        # 布局放入窗口
        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Validator()
    mainwindow.show()
    sys.exit(app.exec_())
