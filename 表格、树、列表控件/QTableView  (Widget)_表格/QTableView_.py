#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTableView_.py
@time: 2020/4/17 21:30

（解耦合的思想）
QTableView 二维表数据    负责显示表格
model      数据源       负责数据

"""
# 导包
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys


# 创建一个类包含界面所有有关的显示  继承的是QWidget初始界面
class TableView(QWidget):
    def __init__(self):
        # 继承PyQt5写好的 QWidget初始参数
        super(TableView, self).__init__()
        # 初始化我们的界面
        self.setWindowTitle('二维表数据')    # 标题
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))   # 图标
        self.resize(800, 500)              # 大小
        # 将有关空间布局的部分默认执行
        self.unit_ui()

    # 所有有关布局的部分放置在一个类方法中
    def unit_ui(self):
        # 创建标准model对象  控制几行几列
        model = QStandardItemModel(5, 3)
        # 设置水平表头
        model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])
        # 创建表格
        table_view = QTableView(self)
        table_view.move(20, 50)
        table_view.resize(500, 300)
        # 表格与数据相联系
        table_view.setModel(model)
        # 添加数据
        model.setItem(0, 0, QStandardItem('001'))
        model.setItem(0, 1, QStandardItem('张三'))
        model.setItem(0, 2, QStandardItem('15'))

    # 这是一个事件函数当控件触发某种操作时进行调用  如：putton.clicked.connect(self.event)
    def event(self):
        print('测试')


if __name__ == '__main__':
    # 创建一个应用   与系统绑定
    app = QApplication(sys.argv)
    # 实例化我们创建的类并show() 显示
    main_window = TableView()
    main_window.show()
    # 系统退出等待应用退出
    sys.exit(app.exec_())
