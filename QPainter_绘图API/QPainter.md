# QPainter绘图
流程
1. painter = QPainter()  # 画笔
2. painter.begin()       # 开始
3. painter.draw ...      # 内容（paintEvent）
4. painter.end()         # 结束



##### *绘制的内容必须在painterEvent中进行，此方法会自动调用*





## 绘制文本

```python
# drawText
painter = QPainter(self)        		# 画图对象
painter.begin(self)						# 开始绘图
painter.setPen(QColor(200, 120, 60))    # 用QColor传递颜色， 设置画笔
painter.setFont(QFont('SimSun', 50))	# 设置字体方法

painter.drawText(event.rect(), Qt.AlignCenter, 'Hello World')   # 绘制文本方法
painter.end()
```



## 像素点绘制图形（正弦曲线）

```python
# drawPoint
painter = QPainter(self)
painter.begin(self)
painter.setPen(Qt.blue)             # 用常量设置笔的颜色
painter.setFont(QFont('SimSun', 50))

for i in range(1001):
    x = self.width()/2 - 250 + i / 2     # 定义一千个x
    y = (self.height()/2) + 100 * math.sin(4 * math.pi/1000 * i)  # 0,4 pi取1000个数
    painter.drawPoint(x, y)             
    painter.end()
```





## 画不同类型的线

```python
# drawLine  
# Qpen对象设置笔
# QPen(Union[QBrush, QColor, Qt.GlobalColor, QGradient], float, style: Qt.PenStyle = 
#     Qt.SolidLine, cap: Qt.PenCapStyle = Qt.SquareCap, join: Qt.PenJoinStyle = 
#     Qt.BevelJoin)

""" setDashPattern(self, Iterable[float]) """

'''
SolidLine 实线
DashLine  虚线
DashDotDotLine 虚线双点线
DotLine   点线
CustomDashLine  自定义  配合setDashPattern 四个数字代表线长和空白长度
'''

painter = QPainter(self)   
painter.begin(self)
pen = QPen(Qt.red, 5, Qt.SolidLine)     # 用笔对象单独对笔进行设置   
painter.setPen(pen)						# 传到painter

painter.drawLine(20, 80, 780, 80)       # 直线的两个坐标

pen.setStyle(Qt.DashLine)
painter.setPen(pen)
painter.drawLine(20, 100, 780, 100)

pen.setStyle(Qt.DashDotDotLine)
painter.setPen(pen)
painter.drawLine(20, 120, 780, 120)

pen.setStyle(Qt.DotLine)
painter.setPen(pen)
painter.drawLine(20, 140, 780, 140)

pen.setStyle(Qt.CustomDashLine)
pen.setDashPattern([1, 2, 3, 4])
painter.setPen(pen)
painter.drawLine(20, 160, 780, 160)
```



## 绘制图形（弧形、圆形、椭圆、矩形、多边形、绘制图像）

```python
# drawArc     弧形
# drawChord   带弦的弧形
# drawPie     扇形
# drawEllipse 椭圆
# drawPolygon 多边形(QPolygon多边形对象)
painter = QPainter(self)
painter.begin(self)
painter.setPen(Qt.blue)
painter.setFont(QFont('SimSun', 50))

# 绘制弧形
rect = QRect(0, 10, 800, 800)    # 位置和大小
painter.drawArc(rect, 180*16, 30*16)  # rect 区域，0起始位置，50*16表示50度 1度=16a

# 绘制带弦的弧
painter.drawChord(rect, 90*16, 30*16)

# 绘制扇形
painter.drawPie(10, 240, 100, 100, 12, 120*16)

# 绘制椭圆
painter.drawEllipse(50, 50, 50, 100)

# 绘制多边形(多边形对象)
point1 = QPoint(130, 120)
point2 = QPoint(130, 150)
point3 = QPoint(220, 180)
point4 = QPoint(220, 170)
point5 = QPoint(200, 150)
# 多边形对象
polygon = QPolygon([point1, point2, point3, point4, point5])
painter.drawPolygon(polygon)

# 绘制图片
image = QImage(QPixmap('../images/ajax-loading.gif'))
rect = QRect(100, 100, image.width(), image.height())
painter.drawImage(rect, image)

painter.end()
```



## drawRect   与    QBrush对象

```python
# 关于笔刷的样式 Qt.SolidPattern  (按住Ctrl + alt + B 转到引用可以看到其他的有哪些样式)
brush = QBrush(Qt.SolidPattern)        
painter.setBrush(brush)
painter.drawRect(30, 20, 100, 100)
painter.end()

# 按住Ctrl + alt + B 得到如下内容
SolidPattern = ... # type: 'Qt.BrushStyle'              固定样式
Dense1Pattern = ... # type: 'Qt.BrushStyle'				稠密样式1
Dense2Pattern = ... # type: 'Qt.BrushStyle'				稠密样式2
Dense3Pattern = ... # type: 'Qt.BrushStyle'				稠密样式3
Dense4Pattern = ... # type: 'Qt.BrushStyle'				稠密样式4
Dense5Pattern = ... # type: 'Qt.BrushStyle'				稠密样式5
Dense6Pattern = ... # type: 'Qt.BrushStyle'				稠密样式6
Dense7Pattern = ... # type: 'Qt.BrushStyle'				稠密样式7
HorPattern = ... # type: 'Qt.BrushStyle'				水平线
VerPattern = ... # type: 'Qt.BrushStyle'				垂直线
CrossPattern = ... # type: 'Qt.BrushStyle'				网格线
BDiagPattern = ... # type: 'Qt.BrushStyle'				B对角线(右上左下)
FDiagPattern = ... # type: 'Qt.BrushStyle'				F对角线(左上右下)
DiagCrossPattern = ... # type: 'Qt.BrushStyle'			交叉网格线线
LinearGradientPattern = ... # type: 'Qt.BrushStyle'		线性梯度
RadialGradientPattern = ... # type: 'Qt.BrushStyle'		迳向梯度
ConicalGradientPattern = ... # type: 'Qt.BrushStyle'	锥梯度
TexturePattern = ... # type: 'Qt.BrushStyle'			组织	
```

