# QSlider 滑块控件

### QSlider滑块的基本使用

```python
slider = QSlider(Qt.Horizontal)   # 水平滑块
slider.setMaximum(100)
slider.setMinimum(10)
slider.setSingleStep(3)   # 步长
slider.setValue(18)   # 当前值
slider.setTickPosition(QSlider.TicksBelow)  # 刻度在下方
slider.setTickInterval(6)  # 设置刻度间隔
slider.valueChanged.connect(lambda: self.getvalue(slider))

def getvalue(self, slider):
        print('当前大小：' + str(slider.value()))

        self.label.setFont(QFont('Arial', slider.value()))
```

