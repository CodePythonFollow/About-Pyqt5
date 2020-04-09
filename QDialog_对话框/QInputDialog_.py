#!/user/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Code
@contact: 1284954990@qq.com
@file: QInputDialog_.py
@time: 2020/4/9 11:12

1. QInputDialog.getItem
2. QInputDialog.getText
3. QInputDialog.getInt
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QFormLayout, QPushButton, QLineEdit, QInputDialog, QApplication


class InputDialog(QWidget):

    # 初始化
    def __init__(self):
        super(InputDialog, self).__init__()
        self.unit_ui()

    def unit_ui(self):
        # 窗口标题和图标
        self.setWindowTitle('输入对话框')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        # 设置布局并运用
        layout = QFormLayout()
        self.setLayout(layout)

        button1 = QPushButton('请选择语言(item)：')
        line_edit1 = QLineEdit()
        line_edit1.setFont(QFont('Arial', 14, 10, False))
        line_edit1.setAlignment(Qt.AlignCenter)
        line_edit1.setFixedSize(200, 34)
        layout.addRow(button1, line_edit1)
        button1.clicked.connect(lambda: self.get_items(line_edit1))

        button2 = QPushButton('请输入文本：')
        line_edit2 = QLineEdit()
        line_edit2.setFont(QFont('Arial', 14, 10, False))
        line_edit2.setAlignment(Qt.AlignCenter)
        line_edit2.setFixedSize(200, 34)
        layout.addRow(button2, line_edit2)
        button2.clicked.connect(lambda: self.get_text(line_edit2))

        button3 = QPushButton('请输入整数：')
        line_edit3 = QLineEdit()
        line_edit3.setFont(QFont('Arial', 14, 10, False))
        line_edit3.setAlignment(Qt.AlignCenter)
        line_edit3.setFixedSize(200, 34)
        layout.addRow(button3, line_edit3)
        button3.clicked.connect(lambda: self.get_int(line_edit3))

    def get_items(self, line_edit1):
        items = ['python', 'c', 'c++', 'php', 'java']
        item, ok = QInputDialog.getItem(self, 'items', '请输入你要选择的语言：', items)
        if ok and item:
            line_edit1.setText(item)

    def get_text(self, line_edit2):
        text, ok = QInputDialog.getText(self, '文本', '请输入文本：')
        if ok and text:
            line_edit2.setText(text)

    def get_int(self, line_edit3):
        num, ok = QInputDialog.getInt(self, '数字', '请选择整数：')
        if ok and num:
            line_edit3.setText(str(num))


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 创建窗口并显示窗口
    main_window = InputDialog()
    main_window.show()
    # 退出app
    sys.exit(app.exec_())
