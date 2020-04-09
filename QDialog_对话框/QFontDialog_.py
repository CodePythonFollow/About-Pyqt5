#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QFontDialog_.py
@time: 2020/4/9 12:35
"""
import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel,\
    QFontDialog


class FontDialog(QWidget):
    # 初始化
    def __init__(self):
        super(FontDialog, self).__init__()
        self.unit_ui()

    def unit_ui(self):
        # 窗口标题和图标
        self.setWindowTitle('文字对话框')
        self.resize(500, 300)
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))

        # 设置布局并运用
        layout = QVBoxLayout()
        self.setLayout(layout)

        font_button = QPushButton('字体调试')
        font_label = QLabel('你好（测试）')
        layout.addWidget(font_label)
        layout.addWidget(font_button)

        font_button.clicked.connect(lambda: self.get_font(font_label))

    def get_font(self, font_label):
        font, ok = QFontDialog.getFont(self)
        if ok:
            font_label.setFont(font)


if __name__ == '__main__':
    # 创建app
    app = QApplication(sys.argv)
    # 创建窗口并显示窗口
    main_window = FontDialog()
    main_window.show()
    # 退出app
    sys.exit(app.exec_())
