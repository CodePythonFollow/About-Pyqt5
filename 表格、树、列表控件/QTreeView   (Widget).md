# QTreeView           QTreeWidget   树控件

###### 							类似 **tabel** 和 **list**

+ 无论父节点和子节点都是  **QTreeWidgetItem**   放在上一个节点里面就是子节点

```python
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
```

+ 节点事件，**注意删除用的是找到父节点删除子节点的方式**

```python
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

....

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
```

