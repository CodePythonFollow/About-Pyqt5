# QScrollBar     滚动条控件

```python
layout = QHBoxLayout()
self.setLayout(layout)
# 创建一个label
self.label = QLabel('测试文本', self)
layout.addWidget(self.label)

# 创建一个滚动条
scroll = QScrollBar(self)
scroll.setMaximum(100)
scroll.setMinimum(10)
layout.addWidget(scroll)

scroll.sliderMoved.connect(self.move)

def move(self, int_value):
    print(int_value)
    self.label.setFont(QFont('Arial', int_value))
```