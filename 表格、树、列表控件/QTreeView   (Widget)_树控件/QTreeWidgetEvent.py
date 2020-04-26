#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTreeWidgetEvent.py
@time: 2020/4/22 17:20
"""

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class TreeWidgetEvent(QWidget):
    def __init__(self):
        super(TreeWidgetEvent, self).__init__()
        self.tree_widget = QTreeWidget()
        self.root1 = QTreeWidgetItem(self.tree_widget, ['root1'])
        self.setWindowTitle('树控件节点事件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(500, 300)
        self.unit_ui()

    def unit_ui(self):

        # 先设置一个垂直布局    注意QMainWindow有自己的布局所以如果用QMainWindow直接addLayout即可
        v_layout = QVBoxLayout()
        self.setLayout(v_layout)

        # 设置一个水平布局放三个按钮
        h_layout = QHBoxLayout()
        # 水平布局放入整体的处置布局
        v_layout.addLayout(h_layout)

        # 水平布局放三个按钮
        add_button = QPushButton('添加节点')
        update_button = QPushButton('更新节点')
        delete_button = QPushButton('删除节点')

        h_layout.addWidget(add_button)
        h_layout.addWidget(update_button)
        h_layout.addWidget(delete_button)

        # 创建树控件
        v_layout.addWidget(self.tree_widget)

        # 设置列数
        self.tree_widget.setColumnCount(2)

        # 设置成中心控件     注意在QMainWindow才能设置，QWidget不可以。
        # self.setCentralWidget(self.tree_widget)

        # 设置标签
        self.tree_widget.setHeaderLabels(['介绍', '功能'])
        self.tree_widget.setHeaderHidden(True)

        # 添加节点两种方式
        self.root1.setIcon(0, QIcon('../images/root.png'))
        root2 = QTreeWidgetItem(self.tree_widget)
        root2.setText(0, 'root2')      # 指定第几列
        root2.setIcon(0, QIcon('../images/root.png'))
        # QTreeWidgetItem.Type()

        # 添加子节点
        child1 = QTreeWidgetItem(self.root1, ['child1', 'action'])
        # 设置子节点可选
        child1.setCheckState(0, Qt.CheckState(2))
        child2 = QTreeWidgetItem(root2, ['child2', 'action'])
        # 节点对齐缩进距离
        child2.setTextAlignment(0, 1)
        # 设置节点宽度
        self.tree_widget.setColumnWidth(0, 300)
        # 让节点全部展开
        self.tree_widget.expandAll()

        # 绑定事件
        add_button.clicked.connect(self.add_node)
        update_button.clicked.connect(self.update_node)
        delete_button.clicked.connect(self.delete_node)

    # 添加节点
    def add_node(self):
        item = self.tree_widget.currentItem()
        # 如果未选中就在父节点添加
        if item:
            new_item = QTreeWidgetItem(item, ['新加的项', '新建的值'])
        else:
            new_item = QTreeWidgetItem(self.tree_widget, ['新加的root', '新建root的值'])
        return new_item

    # 修改节点
    def update_node(self):
        item = self.tree_widget.currentItem()
        if item:
            item.setText(0, '修改的值')
        else:
            self.root1.setText(0, '已修改root')

    # 删除节点   注意root默认没有父节点, 因为我们的方法是通过父节点删除子节点进行删除
    def delete_node(self):
        item = self.tree_widget.currentItem()
        if item:
            # 设置root的父节点
            root_parent = self.tree_widget.invisibleRootItem()
            print(root_parent)
            # 得到父节点
            parent = item.parent()
            (parent or root_parent).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = TreeWidgetEvent()
    main_window.show()
    sys.exit(app.exec_())
