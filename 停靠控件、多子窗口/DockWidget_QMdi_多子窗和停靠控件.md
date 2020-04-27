# QDockWidget    停靠控件

### 		相当于一个容器、容器让入控件

```python
# 首先放一个主控件在窗口
list_widget = QListWidget()
list_widget.addItems(['第一行', '第二行', '第三行'])

# 设置Label成主控件
self.setCentralWidget(QLabel())

# 设置一个停靠的控件
dock_widget = QDockWidget('停靠控件', self)
dock_widget.setWidget(list_widget)
# 默认停靠状态   这里设置为初始浮动
dock_widget.setFloating(True)

# 默认左上方停靠  界面设置停靠控件(这里设置在顶部)   
self.addDockWidget(Qt.TopDockWidgetArea, dock_widget)
```
# QMdiArea   容器控件

### 用来放子容器

# QMdiSubWindow   子窗口容器

### 用来放各种窗口 

##### 单独的窗口所以要调用  show()  方法

+ 默认显示
+ 重叠显示    **cascadeSubWindows()**
+ 平铺显示    **tileSubWindows()**

~~~python
self.setWindowTitle('多子窗口控件')
self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
self.resize(600, 500)
self.unit_ui()
self.count = 0

def unit_ui(self):
    # 设置容器
    self.mdi_area = QMdiArea()
    self.setCentralWidget(self.mdi_area)

    # 设置菜单栏7
    menu = QMenu('文件', self)
    self.menuBar().addMenu(menu)
    menu.addActions([QAction('新建', self), QAction('折叠', self), 							QAction('平铺', self)])

    # 三种状态触发事件
    menu.triggered.connect(self.event_)

def event_(self, action):

    if action.text() == '新建':
        # 子窗口
        sub_window_num = self.count + 1
        # 创建子窗口
        sub_window = QMdiSubWindow()
        # 子窗口设置空间
        sub_window.setWidget(QTextEdit())
        # 设置子窗口标题
        sub_window.setWindowTitle('子窗口' + str(sub_window_num))
        # 将子窗口加入到容器
        self.mdi_area.addSubWindow(sub_window)
        # 显示子窗口
        sub_window.show()

    elif action.text() == '折叠':
        # 重叠方法(级联)
        self.mdi_area.cascadeSubWindows()

    else:
    	self.mdi_area.tileSubWindows()
~~~

