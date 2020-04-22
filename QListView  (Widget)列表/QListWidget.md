# QListView     QListWidget

###### 		与QTableView类似     下面用到消息对话框的两种写法（注意exec_()）

### 一、QListView

```python
# 列表视图
list_view = QListView(self)
# 列表数据
model = QStringListModel()
model.setStringList(['row1', 'row2', 'row3'])
# 绑定
list_view.setModel(model)

# 可以按住ctrl发现clicked里面有个QModelIndex对象
list_view.clicked.connect(self.get_index)

@staticmethod
def get_index(index):
    # 可看到是QModelIndex对象我们可以进入写一个这个对象来查看它的方法
    # print(index)
    # a = QModelIndex()   可以看到有关方法
    # 弹出消息对话框  并阻塞
    QMessageBox(QMessageBox.Icon(4), '您选择了：', index.data(),
    			QMessageBox.Yes | QMessageBox.No).exec_()
```

### 二、 QListWidget

```python
list_widget = QListWidget(self)
list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单一'))
list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单二'))
list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单三'))
list_widget.addItem(QListWidgetItem(QIcon('../images/python.png'), '菜单四'))

# 绑定事件
list_widget.clicked.connect(self.get_index)

def get_index(self, index):
        QMessageBox.information(self, '菜单', f'您选择的是{index.data()}', 											QMessageBox.Yes | QMessageBox.No)
```

