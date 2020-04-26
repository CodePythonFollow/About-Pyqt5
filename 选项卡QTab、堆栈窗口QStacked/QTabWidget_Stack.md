# QTabWidget     选项卡控件

### 类似网页上的翻页效果点击切换一页

###### 每个选项卡都是一个页面，将每个页面写成一个函数结果更清晰

```python
# 创建一个选项卡控件
# 创建三个窗口
self.tab1 = QWidget()
self.addTab(self.tab1, '基本详细')
self.tab2 = QWidget()
self.addTab(self.tab2, '详细信息')
self.tab3 = QWidget()
self.addTab(self.tab3, '确认')

# 默认执行选项卡界面函数，否则不显示，我本来想着点击，但是没看到这个方法
self.tab1_show()
self.tab2_show()
self.tab3_show()

def tab1_show(self):
    layout = QFormLayout()
    self.tab1.setLayout(layout)
    layout.addRow('姓名：', QLineEdit())
    sex = QHBoxLayout()
    sex.addWidget(QRadioButton('男'))
    sex.addWidget(QRadioButton('女'))
    layout.addRow('性别：', sex)

def tab2_show(self):
    layout = QFormLayout()
    self.tab2.setLayout(layout)
    combobox = QComboBox()
    for i in range(16, 60):
        combobox.addItem(str(i) + '岁')

    layout.addRow('年龄', combobox)
    layout.addRow('地址', QLineEdit())

def tab3_show(self):
    button = QPushButton(self.tab3)
    button.move(120, 120)
    button.setText('确认')
```
# QStackedWidget   堆栈窗口

### 	 		自定义分页方式（用listwidget控件控制）

##### 										**原理是通过list行号作为stack_widget的索引**

```python
def __init__(self):
    super(StackedWidget, self).__init__()
    self.setWindowTitle('堆栈窗口控件')
    self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
    self.resize(600, 300)
    self.layout = QHBoxLayout()
    self.setLayout(self.layout)
    self.unit_ui()

def unit_ui(self):
    # 创建列表控件用来作为分页事件
    list_widget = QListWidget()
    list_widget.addItems(['基本信息', '详细信息', '确认'])
    self.layout.addWidget(list_widget)

    # 创建一个堆栈窗口用来放三个窗口
    self.stacked_widget = QStackedWidget()
    self.layout.addWidget(self.stacked_widget)

    # 创建三个窗口并放进堆栈窗口
    self.tab1 = QWidget()
    self.stacked_widget.addWidget(self.tab1)
    self.tab2 = QWidget()
    self.stacked_widget.addWidget(self.tab2)
    self.tab3 = QWidget()
    self.stacked_widget.addWidget(self.tab3)

    # 切换选项卡事件（原理是通过list行号作为stack_widget的索引）
    list_widget.currentRowChanged.connect(self.display)

    # 默认执行选项卡界面函数
    self.tab1_show()
    self.tab2_show()
    self.tab3_show()

def tab1_show(self):
    layout = QFormLayout()
    self.tab1.setLayout(layout)
    layout.addRow('姓名：', QLineEdit())
    sex = QHBoxLayout()
    sex.addWidget(QRadioButton('男'))
    sex.addWidget(QRadioButton('女'))
    layout.addRow('性别：', sex)

def tab2_show(self):
    layout = QFormLayout()
    self.tab2.setLayout(layout)
    combobox = QComboBox()
    for i in range(16, 60):
        combobox.addItem(str(i) + '岁')

    layout.addRow('年龄', combobox)
    layout.addRow('地址', QLineEdit())

def tab3_show(self):
    button = QPushButton(self.tab3)
    button.move(120, 120)
    button.setText('确认')

def display(self, index):
    self.stacked_widget.setCurrentIndex(index)
```

