#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QRadioButton.py
@time: 2020/4/8 1:05
'''

from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import sys


class RadioButton(QWidget):
    def __init__(self):
        super(RadioButton, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('单选框')
        self.resize(400, 300)
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        layout = QHBoxLayout()
        self.setLayout(layout)

        button1 = QRadioButton('第一个按钮')
        # button1.setChecked(True)
        button1.clicked.connect(lambda: self.whichButton(button1))
        layout.addWidget(button1)

        button2 = QRadioButton('第二个按钮')
        button2.clicked.connect(lambda: self.whichButton(button2))
        layout.addWidget(button2)


    def whichButton(self, btn):
        print('被点击的按钮是<' + btn.text() + '>')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = RadioButton()
    mainwindow.show()
    sys.exit(app.exec_())