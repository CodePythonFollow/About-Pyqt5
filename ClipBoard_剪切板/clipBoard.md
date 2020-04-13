# clipBoard  剪切板

```python
# 剪切板定义在app上   在别的软件复制的文本也可粘贴到此app    QLabel支持html富文本
self.clip_board = QApplication.clipboard()

def copy_text(self):
    self.clip_board.setText(self.text_label.text())

def paste_text(self):
    self.text_label.setText(self.clip_board.text())

def copy_image(self):
    self.clip_board.setPixmap(QPixmap('../images/python.jpg'))

def paste_image(self):
    self.image_label.setPixmap(self.clip_board.pixmap())

def copy_html(self):
    mime_data = QMimeData()
    mime_data.setHtml('<b>Bold and <font color=red>Red</font></b>')
    self.clip_board.setMimeData(mime_data)
    print(1)

def paste_html(self):
    mime_data = self.clip_board.mimeData()
    if mime_data.hasHtml():
        self.text_label.setText(mime_data.html())
```

