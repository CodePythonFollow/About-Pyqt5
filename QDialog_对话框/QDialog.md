# 对话框 QDialog

###### 一、QMessageBox  显示消息   

+ **通式   这里的icon数字控制和下面五种等效**

  ```python
  QMessageBox(QMessageBox.Icon(1), '您选择了：', index.data()).exec_()
  ```


1. 关于对话框

   ```python
    QMessageBox.about(self, '关于', '这是一个关于对话框')
   ```

2. 错误对话框 

   ```python
   QMessageBox.critical(self, '错误', '这是一个错误对话框', QMessageBox.Yes | 		 
   					QMessageBox.No, QMessageBox.Yes)
   ```

3. 警告对话框(.worning)

   ```python
   QMessageBox.warning(self, '警告', '这是一个警告对话框', QMessageBox.Yes | 
   					QMessageBox.No, QMessageBox.Yes)
   ```

4. 提问对话框(.question)

   ```python
   QMessageBox.question(self, '提问', '这是一个提问对话框', QMessageBox.Yes | 
   					QMessageBox.No, QMessageBox.Yes)
   ```

5. 消息对话框(.information)

   ```python
   QMessageBox.information(self, '消息', '这是一个消息对话框', QMessageBox.Yes 								|QMessageBox.No, QMessageBox.Yes)
   ```

   

###### 二、QColorDialog 显示颜色（这里用到了调色板，QColor对象运用在调色板，并且调色板使用在文本和背景的区别）

```python
# 设置文本颜色     
@staticmethod
def get_color(font_label):
    color = QColorDialog.getColor()
    # 创建调色板并把QColor对象传入调色板
    palette = QPalette()
    palette.setColor(QPalette.WindowText, color)
    font_label.setPalette(palette)

# 设置背景颜色
def set_bgco(self, font_label):
    color = QColorDialog.getColor()
    # 创建调色板并把QColor对象传入调色板
    palette = QPalette()
    palette.setColor(QPalette.Background, color)     # QPalette.Window在这里也可设置背景
    font_label.setAutoFillBackground(True)
    font_label.setPalette(palette)
```



###### 三、QFileDialog  显示文件打开或者保存  （两种方法等效）

```python
def get_image(self, image_label):
    # _ 就是打开文件的限制条件
    filename, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '图像文件 (*.jpg 
                                              *.png)')
    # print(filename)
    image_label.setPixmap(QPixmap(filename))

@staticmethod
def get_file(contents):
	dialog = QFileDialog()
    dialog.setFileMode(QFileDialog.AnyFile)
    dialog.setFilter(QDir.Files)

    if dialog.exec():
        # 返回的是列表
    	file_names = dialog.selectedFiles()
        # print(file_names)
        with open(file_names[0], 'r', encoding='utf-8') as fi:
        	data = fi.read()
            contents.setText(data)
```

###### 四、QFontDialog  设置字体的对话框

1. .getFont会生成一个字体控制面板

   ```python
   font, ok = QFontDialog.getFont(self)
   if ok:
       font_label.setFont(font)
   ```

###### 五、QInputDialog 输入对话框

1. 下拉框

   ```python
   items = ['python', 'c', 'c++', 'php', 'java']
   item, ok = QInputDialog.getItem(self, 'items', '请输入你要选择的语言：', items)
   if ok and item:
       line_edit1.setText(item)
   ```

2. 文本输入框

   ```python
   text, ok = QInputDialog.getText(self, '文本', '请输入文本：')
   if ok and text:
       line_edit2.setText(text)
   ```

3. 整数输入框

   ```python
   num, ok = QInputDialog.getInt(self, '数字', '请选择整数：')
   if ok and num:
       line_edit3.setText(str(num))
   ```

## QDialog类中的常用方法



Qt.NonModal：非模态，可以和程序的其他窗口进行交互

Qt.WindowModal:窗口模态，程序在未处理玩当前对话框时，将阻止和对话框的父窗口进行交互

Qt.ApplicationModal：应用程序模态，阻止和任何其他窗口进行交互