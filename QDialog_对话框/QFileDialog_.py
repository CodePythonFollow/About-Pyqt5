#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QFileDialog_.py
@time: 2020/4/9 15:19

文件对话框
"""

import sys
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel, \
    QTextEdit, QFileDialog


class FileDialog(QWidget):
    # 初始化
    def __init__(self):
        super(FileDialog, self).__init__()
        self.unit_ui()

    def unit_ui(self):
        # 窗口标题和图标
        self.setWindowTitle('颜色对话框')
        self.resize(500, 300)
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        # 设置布局并运用
        layout = QVBoxLayout()
        self.setLayout(layout)

        button = QPushButton('加载图片')
        layout.addWidget(button)


        image_label = QLabel()
        layout.addWidget(image_label)

        button2 = QPushButton('加载文本')
        layout.addWidget(button2)

        contents = QTextEdit()
        layout.addWidget(contents)

        button.clicked.connect(lambda: self.get_image(image_label))
        button2.clicked.connect(lambda: self.get_file(contents))

    def get_image(self, image_label):
        # _ 就是打开文件的限制条件
        filename, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件 (*.jpg *.png)')
        # print(filename)
        image_label.setPixmap(QPixmap(filename))

    @staticmethod
    def get_file(contents):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        # 维持窗口
        if dialog.exec():
            # 返回的是列表
            file_names = dialog.selectedFiles()
            # print(file_names)
            with open(file_names[0], 'r', encoding='utf-8') as fi:
                data = fi.read()
                contents.setText(data)


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 创建窗口并显示窗口
    main_window = FileDialog()
    main_window.show()
    # 退出app
    sys.exit(app.exec_())

