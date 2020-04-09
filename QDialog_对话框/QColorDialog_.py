#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QColorDialog_.py
@time: 2020/4/9 13:14

颜色对话框
"""
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel, \
    QColorDialog



class ColorDialog(QWidget):
    # 初始化
    def __init__(self):
        super(ColorDialog, self).__init__()
        self.unit_ui()

    def unit_ui(self):
        # 窗口标题和图标
        self.setWindowTitle('颜色对话框')
        self.resize(500, 300)
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        # 设置布局并运用
        layout = QVBoxLayout()
        self.setLayout(layout)

        font_button = QPushButton('颜色调试')
        bg_button = QPushButton('背景调试')
        font_label = QLabel('你好（测试）')
        font_label.setFont(QFont('Arial', 20))
        font_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(font_label)
        layout.addWidget(font_button)
        layout.addWidget(bg_button)

        font_button.clicked.connect(lambda: self.get_color(font_label))
        bg_button.clicked.connect(lambda: self.set_bgco(font_label))

    # 设置文本颜色
    @staticmethod
    def get_color(font_label):
        color = QColorDialog.getColor()
        # 创建调色板并把QColor对象传入调色板
        palette = QPalette()
        palette.setColor(QPalette.WindowText, color)
        font_label.setPalette(palette)

    # 设置背景颜色
    def set_bgco(self, font_label):
        color = QColorDialog.getColor()
        # 创建调色板并把QColor对象传入调色板
        palette = QPalette()
        palette.setColor(QPalette.Background, color)
        font_label.setAutoFillBackground(True)
        font_label.setPalette(palette)


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 创建窗口并显示窗口
    main_window = ColorDialog()
    main_window.show()
    # 退出app
    sys.exit(app.exec_())
