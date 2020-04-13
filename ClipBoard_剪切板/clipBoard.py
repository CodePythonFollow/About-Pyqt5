#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: clipBoard.py
@time: 2020/4/13 16:16

剪切板
"""

import sys
from PyQt5.QtCore import QMimeData
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap


class ClipBoard(QDialog):
    def __init__(self):
        super(ClipBoard, self).__init__()
        self.setWindowTitle('剪切板')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 400)

        # 剪切板定义在app上   在别的软件复制的文本也可粘贴到此app
        self.clip_board = QApplication.clipboard()

        layout = QGridLayout()
        self.setLayout(layout)

        self.text_label = QLabel('用来测试文本')
        self.image_label = QLabel('用来放图片')
        copy_text = QPushButton('复制文本')
        paste_text = QPushButton('粘贴文本')
        copy_image = QPushButton('复制图片')
        paste_image = QPushButton('粘贴图片')
        copy_html = QPushButton('复制html')
        paste_html = QPushButton('粘贴html')

        layout.addWidget(self.text_label, 0, 0)
        layout.addWidget(self.image_label, 0, 1)
        layout.addWidget(copy_text, 1, 0)
        layout.addWidget(paste_text, 1, 1)
        layout.addWidget(copy_image, 2, 0)
        layout.addWidget(paste_image, 2, 1)
        layout.addWidget(copy_html, 3, 0)
        layout.addWidget(paste_html, 3, 1)

        copy_text.clicked.connect(self.copy_text)
        paste_text.clicked.connect(self.paste_text)
        copy_image.clicked.connect(self.copy_image)
        paste_image.clicked.connect(self.paste_image)
        copy_html.clicked.connect(self.copy_html)
        paste_html.clicked.connect(self.paste_html)

    def copy_text(self):
        self.clip_board.setText(self.text_label.text())

    def paste_text(self):
        self.text_label.setText(self.clip_board.text())

    def copy_image(self):
        self.clip_board.setPixmap(QPixmap('../images/python.jpg'))

    def paste_image(self):
        self.image_label.setPixmap(self.clip_board.pixmap())

    def copy_html(self):
        mime_data = QMimeData()
        mime_data.setHtml('<b>Bold and <font color=red>Red</font></b>')
        self.clip_board.setMimeData(mime_data)
        print(1)

    def paste_html(self):
        mime_data = self.clip_board.mimeData()
        if mime_data.hasHtml():
            self.text_label.setText(mime_data.html())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ClipBoard()
    main_window.show()
    sys.exit(app.exec_())

