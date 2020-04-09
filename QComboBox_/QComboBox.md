# QComboBox

### 下拉框

```python
self.comboBox1 = QComboBox()
self.comboBox1.addItem('c++')
self.comboBox1.addItems(['python', 'java', 'php'])

# 事件
def selectionChange(self, index):
        self.label.setText(self.comboBox1.currentText())
        # 根据内容自适应大小
        self.label.adjustSize()
        print('current index is ' + str(index), 'current text is ' + 				  				str(self.comboBox1.currentText()))
```

