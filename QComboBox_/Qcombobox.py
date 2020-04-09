#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: Qcombobox.py
@time: 2020/4/8 1:50

下拉框
'''
import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QComboBox, QVBoxLayout, QWidget, QLabel


class comboBox(QWidget):
    def __init__(self):
        super(comboBox, self).__init__()
        self.unitUI()

    def unitUI(self):
        self.setWindowTitle('下拉框')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.label = QLabel('请选择编程语言：')
        layout.addWidget(self.label)

        self.comboBox1 = QComboBox()
        self.comboBox1.addItem('c++')
        self.comboBox1.addItems(['python', 'java', 'php'])
        layout.addWidget(self.comboBox1)

        # 绑定时间到当前选择的item, 默认传递两个参数一个是本身，一个是索引
        self.comboBox1.currentIndexChanged.connect(self.selectionChange)


    def selectionChange(self, index):
        self.label.setText(self.comboBox1.currentText())
        # 根据内容自适应大小
        self.label.adjustSize()
        print('current index is ' + str(index), 'current text is ' + str(self.comboBox1.currentText()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = comboBox()
    mainwindow.show()
    sys.exit(app.exec_())