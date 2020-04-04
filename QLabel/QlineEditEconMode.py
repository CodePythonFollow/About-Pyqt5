#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QlineEditEconMode.py
@time: 2020/4/4 17:56

QLineEdit  四种回显模式
1: normal 正常显示
2: noEchol 不显示
3: password 密码不可见
4: passwordEchoOnEditLineEdit  密码可见
'''
from PyQt5.QtWidgets import QFormLayout, QLineEdit, QWidget, QApplication
import sys

class QlineEditEconMode(QWidget):
    def __init__(self):
        super(QlineEditEconMode, self).__init__()
        self.unitUI()

    def unitUI(self):
        # 设置标题

        self.setWindowTitle('四种回显')

        # 四个输入框
        normal = QLineEdit()
        noEchol = QLineEdit()
        password = QLineEdit()
        passwordEchoOn = QLineEdit()

        # 定义表单布局
        formLayout = QFormLayout()

        # 这种方法追加控件好处是不需要再设置QLabel  还默认了伙伴控件
        formLayout.addRow('&normal', normal)
        formLayout.addRow('&noEchol', noEchol)
        formLayout.addRow('&password', password)
        formLayout.addRow('&passwordEchoOn', passwordEchoOn)

        # 设置提示文本
        normal.setPlaceholderText('nomal')
        noEchol.setPlaceholderText('noEchol')
        password.setPlaceholderText('password')
        passwordEchoOn.setPlaceholderText('passwordEchoOn')

        # 设置输入行回显属性
        normal.setEchoMode(QLineEdit.Normal)
        noEchol.setEchoMode(QLineEdit.NoEcho)
        password.setEchoMode(QLineEdit.Password)
        passwordEchoOn.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 把布局放进窗口
        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QlineEditEconMode()
    mainwindow.show()
    sys.exit(app.exec_())


