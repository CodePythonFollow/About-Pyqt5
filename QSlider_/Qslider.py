#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: Qslider.py
@time: 2020/4/8 14:55

滑块控件
'''
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QSlider, QVBoxLayout, QWidget, QLabel
import sys

class Qslider(QWidget):
    def __init__(self):
        super(Qslider, self).__init__()
        self.unitUI()

    def unitUI(self):

        # 主界面信息
        self.setWindowTitle('滑块控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 300)

        # 布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 设置水平  步长和最值  刻度位置
        self.label = QLabel('Hello World')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        slider = QSlider(Qt.Horizontal)
        slider.setMaximum(100)
        slider.setMinimum(10)
        slider.setSingleStep(3)   # 步长
        slider.setValue(18)   # 当前值
        slider.setTickPosition(QSlider.TicksBelow)  # 刻度在下方
        slider.setTickInterval(6)  # 设置刻度间隔
        slider.valueChanged.connect(lambda: self.getvalue(slider))

        layout.addWidget(slider)

    def getvalue(self, slider):
        print('当前大小：' + str(slider.value()))

        self.label.setFont(QFont('Arial', slider.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Qslider()
    mainwindow.show()
    sys.exit(app.exec_())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = Qslider()
    mainwindow.show()
    sys.exit(app.exec_())


