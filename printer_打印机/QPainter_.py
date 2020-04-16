#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QPainter_.py
@time: 2020/4/15 16:19

打印对象  QPainter
打印图片和文本及文件

这里类似一个文本编辑器
"""

import sys

# from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPageSetupDialog


class Painter(QMainWindow):

    def __init__(self):
        super(Painter, self).__init__()
        self.setWindowTitle('打印机')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(1300, 800)

        # 放一个菜单栏   打印设置窗口
        menu_bar = self.menuBar()
        menu = QMenu('File', self)
        open_file = QAction('Open File', self)
        print_ = QAction('Print Set', self)
        menu.addAction(open_file)
        menu.addAction(print_)
        menu_bar.addMenu(menu)

        # 打印机对象
        self.printer = QPrinter()

        # 工具栏   这个是打印设置
        toolbar = self.addToolBar('Printer')
        tool_action = QAction(QIcon('../images/printer.png'), 'print', self)
        toolbar.addAction(tool_action)

        # 绑定事件
        open_file.triggered.connect(self.open_file)
        print_.triggered.connect(self.set_printer_dialog)
        tool_action.triggered.connect(self.print_dialog)

        # 给一个工具栏打印当前窗口的文本
        self.text_edit = QTextEdit(self)
        self.text_edit.setGeometry(20, 80, self.width()-40, self.height()-100)
        self.text_edit.setFont(QFont('Times New Roman', 15, 10))

    # 打开文件对话框
    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '所有文件 *.*')
        try:
            with open(filename, 'r', encoding='utf-8') as fi:
                self.text_edit.setText(fi.read())
        except UnicodeDecodeError:
            self.text_edit.setHtml("<img src=%s>" % filename)

    # 打印设置对话框
    def set_printer_dialog(self):
        set_dialog = QPageSetupDialog(self.printer, self)
        set_dialog.exec()

    # 打印对话框
    def print_dialog(self):
        print_dialog = QPrintDialog(self.printer, self)
        # 打印对话框点击确认再执行
        if QDialog.Accepted == print_dialog.exec_():
            # 打印的第一种方法直接执行控件的打印方法
            # self.text_edit.print(self.printer)

            # 打印的第二种方法还能画到printer对象里面的方式打印图片
            screen = self.text_edit.grab()   # .QPixmap对象
            painter = QPainter()
            painter.begin(self.printer)
            painter.drawPixmap(0, 0, screen)
            painter.end()

            print('print end')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Painter()
    main_window.show()
    sys.exit(app.exec_())
