#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QDialog_demo.py
@time: 2020/4/9 0:23

QMessageBox
QColorDialog
QFileDialog
QFontDialog
QInputDialog
'''

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class QDialog_(QWidget):
    def __init__(self):
        super(QDialog_, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('下拉框')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 300)
        # layout = QVBoxLayout()
        # self.setLayout(layout)

        self.button = QPushButton(self)  # 相当于加入了窗体
        self.button.setText('弹出对话框')
        self.button.move(50, 50)
        # layout.addWidget(self.button)
        self.button.move(100, 50)

        self.button.clicked.connect(self.alter)

    def alter(self):
        dialog = QDialog()
        button = QPushButton('确定', dialog)
        button.move(50, 50)
        button.clicked.connect(dialog.close)
        dialog.setWindowTitle('对话框')
        # 对话框以模式的状态显示，这样在弹出对话框时阻止窗口不能操作
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QDialog_()
    mainwindow.show()
    sys.exit(app.exec_())


