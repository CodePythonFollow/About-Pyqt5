#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTreeWidgetDemo.py
@time: 2020/4/22 11:17

按住  ctrl + alt + b查看引用的位置可查到状态的有关参数。具体值可在看定义位置

class CheckState(int): ...
    Unchecked = ... # type: 'Qt.CheckState'           Unchecked = 0          也可直接写成Qt.Unchecked  下同
    PartiallyChecked = ... # type: 'Qt.CheckState'    PartiallyChecked = 1
    Checked = ... # type: 'Qt.CheckState'             Checked = 2
"""

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class TreeWidget(QMainWindow):
    def __init__(self):
        super(TreeWidget, self).__init__()
        self.setWindowTitle('树控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(500, 300)
        self.unit_ui()

    def unit_ui(self):

        tree_widget = QTreeWidget(self)

        # 设置列数
        tree_widget.setColumnCount(2)

        # 设置成中心控件     注意在QMainWindow才能设置，QWidget不可以。
        self.setCentralWidget(tree_widget)

        # 设置标签
        tree_widget.setHeaderLabels(['介绍', '功能'])
        tree_widget.setHeaderHidden(True)

        # 添加节点两种方式
        root1 = QTreeWidgetItem(tree_widget, ['root1'])
        root1.setIcon(0, QIcon('../images/root.png'))
        root2 = QTreeWidgetItem(tree_widget)
        root2.setText(0, 'root2')      # 指定第几列
        root2.setIcon(0, QIcon('../images/root.png'))
        # QTreeWidgetItem.Type()

        # 添加子节点
        child1 = QTreeWidgetItem(root1, ['child1', 'action'])
        # 设置子节点可选
        child1.setCheckState(0, Qt.CheckState(2))
        child2 = QTreeWidgetItem(root2, ['child2', 'action'])
        # 节点对齐缩进距离
        child2.setTextAlignment(0, 1)
        # 设置节点宽度
        tree_widget.setColumnWidth(0, 300)
        # 让节点全部展开
        tree_widget.expandAll()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TreeWidget()
    main_window.show()
    sys.exit(app.exec_())
