#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QSpinder.py
@time: 2020/4/8 22:26

计数器控件(QSpinBox)
'''
import sys

from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QSpinBox, QLabel
from PyQt5.QtCore import Qt

class SpinBox(QWidget):
    def __init__(self):
        super(SpinBox, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('计数器控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 400)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel()
        self.label.setText('这个值是:')
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        spinBox = QSpinBox()
        spinBox.setMinimum(10)
        spinBox.setMaximum(100)
        spinBox.setValue(18)
        layout.addWidget(spinBox)

        spinBox.valueChanged.connect(lambda: self.get_value(spinBox))

    def get_value(self, spinbox):
        print(spinbox.value())
        self.label.setFont(QFont('Arial', spinbox.value()))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = SpinBox()
    mainwindow.show()
    sys.exit(app.exec_())


