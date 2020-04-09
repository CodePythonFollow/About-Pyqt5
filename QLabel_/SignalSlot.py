#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QLabelevent.py
@time: 2020/4/4 14:19
'''
# Qt的一些常量
from PyQt5.QtCore import Qt
# Qt widgets是各种小部件
from PyQt5.QtWidgets import QVBoxLayout, QMainWindow, QApplication, QLabel, QWidget
# Qt工具如图片、调色板等
from PyQt5.QtGui import QPalette, QPixmap, QIcon
# 导入系统库用于连接app和系统
import sys


class QLabelEvent(QWidget):
    def __init__(self):
        super(QLabelEvent, self).__init__()
        # 默认执行就不需要调用
        self.initUI()

    # 有关Label的控件
    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        # Text支持标签
        label1.setText("<font color=red>这是一个文本标签</font>")
        # 自动填充背景
        label1.setAutoFillBackground(True)
        # 调色板
        patette = QPalette()
        patette.setColor(QPalette.Window, Qt.blue)
        # 对label1进行调色
        label1.setPalette(patette)
        # label1设置居中对齐
        label1.setAlignment(Qt.AlignCenter)

        # 设置一个链接以便后面操作点击和滑过事件
        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        # label3设置一个
        label3.setAlignment(Qt.AlignCenter)
        # 这是提示文本
        label3.setToolTip('这是一个图片标签')
        # 设置一个图片
        label3.setPixmap(QPixmap("../images/python.jpg"))

        # 打开拓展连接     True就会在浏览器打开False就会调用槽
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='http://www.baidu.com'>关注python</a>")


        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个链接')



        # 布局然后放控件
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        # 设置信号槽
        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkActivated)

        # 把布局对象赋给QWidget对象
        self.setLayout(vbox)
        # 设置QWidget的标题
        self.setWindowTitle('这是一个信号槽和QLabel控件的案例')


    # 鼠标滑过事件
    def linkHovered(self):
        print('鼠标从此滑过label2')

    # 鼠标点击事件
    def linkActivated(self):
        print('鼠标点击label4')


if __name__ == '__main__':
    # 创建app对象
    app = QApplication(sys.argv)
    # 创建窗口 (这种是完全空的窗口，而之前都是用的QMainWindow基本窗口创建的)
    mainwindow = QLabelEvent()
    # 显示窗口
    mainwindow.show()
    # 退出程序等待app退出事件
    sys.exit(app.exec_())



