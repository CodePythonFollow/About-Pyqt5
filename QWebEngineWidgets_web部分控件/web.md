# PyQt5.QtWebEngineWidgets 

### 一、加载网页

```python
browser = QWebEngineView()
browser.load(QUrl('http://www.baidu.com'))
self.setCentralWidget(browser)
```

### 二、加载本地html

```python
browser = QWebEngineView()
# 得到当前文件目录   由于Qurl不识别相对路径
url = os.getcwd()
print(url)
browser.load(QUrl.fromLocalFile(url + '/测试.html'))
self.setCentralWidget(browser)
```

### 三、直接嵌入html代码

```python
browser = QWebEngineView()
browser.setHtml('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>测试</title>
  <style>
    div {
    width: 500px;
    height: 300px;
    background-color: skyblue;
    margin: 30px auto;
    }
  </style>
  </head>
<body>
  <h1 align="center">PyQt测试本地页面</h1>
  <div></div>
</body>
</html>
''')
self.setCentralWidget(browser)
```

### 三、运行网页js

```python
self.browser = QWebEngineView()
# 得到当前文件目录   由于Qurl不识别相对路径
url = os.getcwd()
# print(url)
self.browser.load(QUrl.fromLocalFile(url + '/测试.html'))
self.layout().addWidget(self.browser)

# button调用js
button = QPushButton('改变颜色')
self.layout().addWidget(button)
button.move(800, 50)
button.clicked.connect(self.get_div)

# 调用js
def get_div(self):
	self.browser.page().runJavaScript('get_p()', self.callback)

# js回调
@staticmethod
def callback(result):
	print(result)
```

​	

