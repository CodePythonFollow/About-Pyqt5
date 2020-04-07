#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QPushButton.py
@time: 2020/4/7 18:25
QPushButton 的使用，结合槽和传参的匿名函数综合案例
'''

from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import sys

class PushButton(QWidget):
    def __init__(self):
        super(PushButton, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('QPushButton')
        self.resize(400, 300)
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        layout = QVBoxLayout()

        button1 = QPushButton('第一个按钮')

        # 设置可勾选的就是按住是一种状态不会自动回复
        button1.setCheckable(True)

        # 切换  所以刚开始的状态就是被点击的
        button1.toggle()

        button1.clicked.connect(lambda: self.whichButton(button1))
        button1.clicked.connect(lambda: self.ButtonState(button1))

        layout.addWidget(button1)

        button2 = QPushButton('图像按钮')
        button2.setIcon(QIcon(QPixmap('../images/python.png')))
        button2.clicked.connect(lambda: self.whichButton(button2))
        layout.addWidget(button2)

        # 不可用的
        button3 = QPushButton('不可用的按钮')
        button3.setEnabled(False)
        button3.clicked.connect(lambda: self.whichButton(button3))
        layout.addWidget(button3)


        # 默认的按钮  加热键效果
        button4 = QPushButton('&M默认的按钮')
        button4.clicked.connect(lambda: self.whichButton(button4))
        layout.addWidget(button4)


        self.setLayout(layout)

    def ButtonState(self, btn):
        print('现在被点击的的状态是：' + str(btn.isChecked()))

    def whichButton(self, btn):
        print('被点击的按钮是<' + btn.text() + '>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = PushButton()
    mainwindow.show()
    sys.exit(app.exec_())
