#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: Buddy.py
@time: 2020/4/4 16:59
'''
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QGridLayout, QApplication
import sys

# 对话窗口 Dialog
class QlabelBuddy(QDialog):
    def __init__(self):
        super(QlabelBuddy, self).__init__()
        self.initUI()

    def initUI(self):
        # 设置标题
        self.setWindowTitle('设置伙伴关系')

        # 提示文本(&Name 即热键为N  Alt + N 即可控制光标)
        name = QLabel('&Name：', self)
        # 输入框
        nameLine = QLineEdit()
        # 设置伙伴关系
        name.setBuddy(nameLine)

        # 提示文本
        password = QLabel('&Password：', self)
        # 输入框
        passwordline = QLineEdit()
        # 设置伙伴关系
        password.setBuddy(passwordline)

        # 确认按钮和取消按钮、
        sureButton = QPushButton('完成')
        cancelButton = QPushButton('取消')

        # 网格布局   （四个参数意思为放在哪行哪列， 占据几行几列）
        layout = QGridLayout()
        layout.addWidget(name, 0, 0, 1, 1)
        layout.addWidget(nameLine, 0, 1, 1, 2)
        layout.addWidget(password, 1, 0, 1, 1)
        layout.addWidget(passwordline, 1, 1, 1, 2)
        layout.addWidget(sureButton, 2, 1, 1, 1)
        layout.addWidget(cancelButton, 2, 2, 1, 1)

        # 将布局放到窗口
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QlabelBuddy()
    mainwindow.show()
    sys.exit(app.exec_())