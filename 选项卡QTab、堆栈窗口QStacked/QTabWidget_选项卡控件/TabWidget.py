#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: TabWidget.py
@time: 2020/4/23 21:44

每个选项卡都是一个页面，将每个页面写成一个函数结果更清晰
"""

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class TabWidget(QTabWidget):
    def __init__(self):
        super(TabWidget, self).__init__()
        self.setWindowTitle('选项卡控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(400, 300)
        self.unit_ui()

    def unit_ui(self):
        # 创建一个选项卡控件
        # 创建三个窗口
        self.tab1 = QWidget()
        self.addTab(self.tab1, '基本详细')
        self.tab2 = QWidget()
        self.addTab(self.tab2, '详细信息')
        self.tab3 = QWidget()
        self.addTab(self.tab3, '确认')

        # 默认执行选项卡界面函数，否则不显示，我本来想着点击，但是没看到这个方法
        self.tab1_show()
        self.tab2_show()
        self.tab3_show()

    def tab1_show(self):
        layout = QFormLayout()
        self.tab1.setLayout(layout)
        layout.addRow('姓名：', QLineEdit())
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))
        layout.addRow('性别：', sex)

    def tab2_show(self):
        layout = QFormLayout()
        self.tab2.setLayout(layout)
        combobox = QComboBox()
        for i in range(16, 60):
            combobox.addItem(str(i) + '岁')

        layout.addRow('年龄', combobox)
        layout.addRow('地址', QLineEdit())

    def tab3_show(self):

        button = QPushButton(self.tab3)
        button.move(120, 120)
        button.setText('确认')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TabWidget()
    main_window.show()
    sys.exit(app.exec_())
