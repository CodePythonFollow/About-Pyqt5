#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTableWidget_.py
@time: 2020/4/17 22:46
"""
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class TableWidget(QWidget):
    def __init__(self):
        super(TableWidget, self).__init__()
        self.setWindowTitle('二维表数据')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 500)
        self.unit_ui()

    def unit_ui(self):
        table_widget = QTableWidget(self)
        table_widget.move(20, 30)
        table_widget.resize(500, 300)
        # 设置行数和列数
        table_widget.setRowCount(5)
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels(['id', 'name', 'old'])
        # 添加数据
        table_widget.setItem(0, 0, QTableWidgetItem('1'))
        table_widget.setItem(0, 1, QTableWidgetItem('小强'))
        table_widget.setItem(0, 2, QTableWidgetItem('16'))
        table_widget.setItem(1, 0, QTableWidgetItem('2'))
        table_widget.setItem(1, 1, QTableWidgetItem('张三'))
        table_widget.setItem(1, 2, QTableWidgetItem('15'))
        table_widget.setItem(2, 0, QTableWidgetItem('3'))
        table_widget.setItem(2, 1, QTableWidgetItem('小明'))
        table_widget.setItem(2, 2, QTableWidgetItem('14'))
        table_widget.setItem(3, 0, QTableWidgetItem('4'))
        table_widget.setItem(3, 1, QTableWidgetItem('大明'))
        table_widget.setItem(3, 2, QTableWidgetItem('18'))
        # 设置跨行
        table_widget.setSpan(3, 2, 2, 1)
        # 放置图片
        table_widget.setItem(4, 0, QTableWidgetItem(QIcon('../images/python.png'), 'python'))
        # 调整图片大小zzz
        table_widget.setIconSize(QSize(20, 20))
        # 排序
        table_widget.sortItems(0, Qt.DescendingOrder)
        # table_widget.sortItems(0, Qt.AscendingOrder)
        # 禁止编辑
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 整行选择
        # table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 调整列和行随着内容改变
        # table_widget.resizeColumnsToContents()
        # table_widget.resizeRowsToContents()
        # 相当于QHeaderView对象设置隐藏不显示 头
        # table_widget.horizontalHeader().setVisible(False)
        # 隐藏网格线
        # table_widget.setShowGrid(False)
        # 放控件进去
        # combobox = QComboBox()
        # combobox.resize(100, 20)
        # combobox.addItem('01')
        # combobox.addItem('02')
        # table_widget.setCellWidget(1, 0, combobox)

        # 这里设置一个右键菜单请求
        table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        table_widget.customContextMenuRequested.connect(self.get_menu)

    # 获得位置但是我们需要得到当前的单元格位置
    def get_menu(self, pos):
        table_widget = self.sender()
        # 得到一个QModelIndex对象   有个列函数和行函数 和data函数也可用.text()返回数据  源码只有几十行
        model_index = table_widget.selectionModel().selection().indexes()
        row = model_index[0].row()
        data = model_index[0].data()
        # 创建菜单
        menu = QMenu()
        menu.addAction('打印当前数据')
        menu.addAction('打印当行数据')
        # 阻塞，类似我们窗口每次退出等待app.exit就是用事件触发才会继续
        # 这里我们exec_()不加参数默认是在pos位置打开菜单，但是QPoint对象默认是针对整个屏幕，也就是绝对坐标
        # 所以我们需要让打开的菜单处在当前打开的位置需要将窗口设置成
        screen_point = table_widget.mapToGlobal(pos)
        action = menu.exec_(screen_point)
        # 由于第一行有空值所以我们不打印第一行的数据空的item没有.text()
        if row > 0:
            if action:
                if action.text() == '打印当前数据':
                    print(data)
                else:
                    print('当行数据为：' + table_widget.item(row, 0).text(), table_widget.item(row, 1).text(), table_widget.item(row, 2).text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TableWidget()
    main_window.show()
    sys.exit(app.exec_())
