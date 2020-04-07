#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QCheckBox.py
@time: 2020/4/8 1:21

三种状态
1、未选择
2、半选中
3、选中
'''
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QCheckBox, QApplication, QHBoxLayout, QWidget
import sys


class CheckBox(QWidget):
    def __init__(self):
        super(CheckBox, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('复选框')
        self.resize(400, 300)
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        layout = QHBoxLayout()
        self.setLayout(layout)

        checkBox1 = QCheckBox('第一个控件')
        checkBox1.setChecked(True)
        checkBox1.stateChanged.connect(lambda: self.GetStatue(checkBox1))
        layout.addWidget(checkBox1)

        checkBox2 = QCheckBox('第二个控件')
        checkBox2.stateChanged.connect(lambda: self.GetStatue(checkBox2))
        layout.addWidget(checkBox2)

        # tristate 三态就是三种状态
        checkBox3 = QCheckBox('第三个控件')
        checkBox3.setTristate(True)
        # checkBox3.setChecked(Qt.PartiallyChecked)    # 用来进行部分检测
        checkBox3.stateChanged.connect(lambda: self.GetStatue(checkBox3))
        layout.addWidget(checkBox3)

    def GetStatue(self, ck):
        print(ck.isChecked())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = CheckBox()
    mainwindow.show()
    sys.exit(app.exec_())
