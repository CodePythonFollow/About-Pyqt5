# 拖拽事件

a: 让a控件支持拖拽 a.setDragEnabled(True)


b: 让b控件支持被拖拽 b.setAcceptDrops(True)还需要两个事件
1. dragEnterEvent   将A拖到B触发
2. dropEvent        在B的区域放下A时触发



```python
"""
有三个对象：
QtGui.QDragEnterEvent
QtCore.QMimeData
QtCore.QDropEvent

方法是对象的方法，课点击（ctrl + dragEnterEvent可看到原始代码，这里只是重写了该方法。）

"""


# 下拉框接收拖拽
class Drag(QComboBox):
    def __init__(self):
        super(Drag, self).__init__()
        self.setAcceptDrops(True)   # 设置下拉框接收拖拽

    def dragEnterEvent(self, e):    # e: QtGui.QDragEnterEvent
        print(e)
        print(e.mimeData())			# e: QtCore.QMimeData
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):                 # e: QtCore.QDropEvent
        self.addItem(e.mimeData().text())   # e: QtCore.QMimeData


# 主界面下拉框并设置拖拽事件
class ComboBox(QWidget):
    def __init__(self):
        super(ComboBox, self).__init__()
        self.setWindowTitle('拖拽事件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 400)

        layout = QFormLayout()
        self.setLayout(layout)

        # 设置下拉框
        combobox = Drag()

        line_edit = QLineEdit()
        line_edit.setDragEnabled(True)

        layout.addRow(line_edit, combobox)
```