# menu_toolbar_statusbar 菜单栏—工具栏—状态栏（在QMinWindow下操作会更加美观和简便）

## 一、menu

结构：

​		菜单栏：MenuBar

​				菜单：menu

​						操作：Action  快捷键等操作

> **下面代码是在QMainWindow里面继承的菜单栏  因为self本身就有菜单栏所以只要add即可**

```python
# 这里只是给menuBar起个名字，可以直接用self.menu.add***
bar = self.menuBar()

project = bar.addMenu('文件')
project.addAction('新建文件')

save = QAction('保存文件', self)
save.setShortcut('Ctrl + S')
project.addAction(save)

save.triggered.connect(self.save)

# 这个a是triggered传入的参数所以a是False进入triggered方法里可看到a默认传参False
# sender()就是传入了调用该方法的对象之前的匿名函数也是同理。
def save(self, a):
    print(a)
    print(self.sender())
    print(self.sender().text())
```

## 二、toobar

结构：

​		工具栏：ToolBar

​				工具：Action

> **这里尝试使用QWidget来写一个toobar用QMainWindow和上面菜单栏差不多**

```python
# 由于是是在QWidget写的工具栏没有add方法，所以要采用布局，这里简单的用move实现效果，不加会重叠在一起
# MainWindow写的工具栏会有分隔符还会右键出现工具栏的名称等比较全
file_toolbar = QToolBar('File', self)
file_toolbar.move(0, 0)
new = QAction(QIcon('../images/new.png'), 'new', self)
file_toolbar.addAction(new)

edit_toolbar = QToolBar('Edit', self)
edit_toolbar.move(50, 0)
open_ = QAction(QIcon('../images/open.png'), 'open', self)
edit_toolbar.addAction(open_)
```

```python
# QMainWindow方法
tb1 = self.addToolBar("File")

new = QAction(QIcon('../images/new.png'),"new",self)
tb1.addAction(new)

tb2 = self.addToolBar("Edit")
open__ = QAction(QIcon('../images/new.png'),"open",self)
tb2.addAction(open__)
```

## 三、statusbar

```python
# 菜单时间点击  状态栏显示消息
menu = QMenu('菜单', self)
self.menuBar().addMenu(menu)
action = QAction(QIcon('../images/new.png'), '新建', self)
menu.addAction(action)
menu.triggered.connect(self.status_change)

def status_change(self, action):
    # 创建菜单栏，跟随事件显示消息
    status_bar = QStatusBar()
    self.setStatusBar(self.status_bar)
    if action.text() == '新建':
        ''' showMessage(self, str, msecs: int = 0) 毫秒'''
        status_bar.showMessage('新建一个文件', 5000)
```