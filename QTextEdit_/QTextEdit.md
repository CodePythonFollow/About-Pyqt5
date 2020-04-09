# QTextEdit多行文本编辑

```python
self.text = QTextEdit()

buttontext = QPushButton('显示文本')
buttontext.clicked.connect(self.Buttontext)

buttonhtml = QPushButton('显示HTML')
buttonhtml.clicked.connect(self.Buttonhtml)

buttonTotext = QPushButton('打印文本')
buttonTotext.clicked.connect(self.ButtonTotext)

buttonTohtml = QPushButton('打印HTML')
buttonTohtml.clicked.connect(self.ButtonTohtml)

# 显示文本
def Buttontext(self):
 	self.text.setText('Hello Python')

# 显示Html
def Buttonhtml(self):
	self.text.setHtml('<font color="red" size="20">Hello Word</font>')

# 打印文本
def ButtonTotext(self):
	print(self.text.toPlainText())

# 打印Html
def ButtonTohtml(self):
	print(self.text.toHtml())
```

