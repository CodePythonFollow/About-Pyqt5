# Calendar    and   DateTimeEdit

> **注意date、 time、 datetime是clicked函数传入的。在后一章的triggered事件的参数中可能更好理解这一点**

```python
# 日历控件   
calendar = QCalendarWidget(self)
calendar.setGridVisible(True)   # 网格显示
calendar.move(80, 10)
calendar.setFixedSize(600, 400)
data = calendar.selectedDate()

# 显示当前选定的时间
self.label.setText(data.toString('yyyy-MM-dd dddd'))
self.label.move(80, 480)

calendar.clicked.connect(self.show_data)

def show_data(self, data):
    # print(data)
    self.label.setText(data.toString('yyyy-MM-dd dddd'))
```


> **date_time2.setCalendarPopup(True)   这个比较实用   将日期编辑栏结合日历控制**

```python
# QDateTimeEdit   
date_time1 = QDateTimeEdit(QDateTime.currentDateTime())
# 设置一些属性  两种方法
date_time1.setMaximumDate(QDate.currentDate().addDays(365))
date_time1.setMinimumDateTime(QDateTime(1998, 7, 19, 12, 45, 36))

date_time2 = QDateTimeEdit(QDateTime.currentDateTime())

# 将日期编辑栏结合日历控制
date_time2.setCalendarPopup(True)

date_time3 = QDateTimeEdit(QDateTime.currentDateTime())
date_time4 = QDateTimeEdit(QDateTime.currentDateTime())

date_time1.setDisplayFormat("yyyy-MM-dd HH:dd:ss")
date_time2.setDisplayFormat("yyyy/MM/dd HH-dd-ss")
date_time3.setDisplayFormat("yyyy.MM.dd")
date_time4.setDisplayFormat("HH:dd:ss")

# 获取时间编辑栏的属性
button = QPushButton('获取第一行时间')
layout.addWidget(button)
button.clicked.connect(lambda: self.get_time(date_time1))

layout.addWidget(date_time1)
layout.addWidget(date_time2)
layout.addWidget(date_time3)
layout.addWidget(date_time4)

# 有关日期的三个事件
date_time1.timeChanged.connect(self.time_change)
date_time1.dateChanged.connect(self.data_change)
date_time1.dateTimeChanged.connect(self.datetime_change)

# 获取事件编辑栏的事件
@staticmethod
def get_time(date_time):
    print(date_time.dateTime())
    print(date_time.maximumDate())
    print(date_time.minimumDate())

# 获取时间改变
@staticmethod
def time_change(time):
    print(time)

# 获取日期改变
@staticmethod
def data_change(date):
    print(date)

# 获取日期和时间改变
@staticmethod
def datetime_change(datetime):
    print(datetime)
```