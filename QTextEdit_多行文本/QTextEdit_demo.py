#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QTextEdit_demo.py
@time: 2020/4/7 17:46
'''


from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QVBoxLayout
import sys


class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.unitUI()

    def unitUI(self):

        self.setWindowTitle('多行文本输入框')
        self.resize(500, 300)
        vboxlayout = QVBoxLayout()

        self.text = QTextEdit()

        buttontext = QPushButton('显示文本')
        buttontext.clicked.connect(self.Buttontext)

        buttonhtml = QPushButton('显示HTML')
        buttonhtml.clicked.connect(self.Buttonhtml)

        buttonTotext = QPushButton('打印文本')
        buttonTotext.clicked.connect(self.ButtonTotext)

        buttonTohtml = QPushButton('打印HTML')
        buttonTohtml.clicked.connect(self.ButtonTohtml)


        vboxlayout.addWidget(self.text)
        vboxlayout.addWidget(buttontext)
        vboxlayout.addWidget(buttonhtml)
        vboxlayout.addWidget(buttonTotext)
        vboxlayout.addWidget(buttonTohtml)

        self.setLayout(vboxlayout)

    # 显示文本
    def Buttontext(self):
        self.text.setText('Hello Python')

    # 显示Html
    def Buttonhtml(self):
        self.text.setHtml('<font color="red" size="20">Hello Word</font>')

    # 打印文本
    def ButtonTotext(self):
        print(self.text.toPlainText())

    # 打印Html
    def ButtonTohtml(self):
        print(self.text.toHtml())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QTextEditDemo()
    mainwindow.show()
    sys.exit(app.exec_())




