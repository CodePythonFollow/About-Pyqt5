# 计数器控件(QSpinBox)



```python
spinBox = QSpinBox()
spinBox.setMinimum(10)
spinBox.setMaximum(100)
spinBox.setValue(18)
layout.addWidget(spinBox)
spinBox.valueChanged.connect(lambda: self.get_value(spinBox))

def get_value(self, spinbox):
    print(spinbox.value())
    self.label.setFont(QFont('Arial', spinbox.value()))
```