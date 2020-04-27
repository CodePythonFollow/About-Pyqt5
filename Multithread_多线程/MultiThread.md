# 计时器   QTimer
### timer  是一个线程对象

##### 			timer.timeout是绑定的线程事件

### start开始线程，每隔1000毫秒执行

### end  结束线程

```python
# 计时器控件
self.timer = QTimer()
# 显示时间
self.timer.timeout.connect(self.showtime)

# 放置显示时间的label
self.label = QLabel('等待开始')
self.label.setFont(QFont('Arial', 20))
layout.addWidget(self.label, 0, 0, 1, 3)

# 起始和终止按钮
self.start_button = QPushButton('开始')
self.end_button = QPushButton('结束')
self.delay_start = QPushButton('5秒后开始')
layout.addWidget(self.start_button, 1, 0)
layout.addWidget(self.end_button, 1, 1)
layout.addWidget(self.delay_start, 1, 2)

# 点击事件
self.start_button.clicked.connect(self.start_event)
self.end_button.clicked.connect(self.end_event)
self.delay_start.clicked.connect(self.single_shot)

# 每个线程事件    
def showtime(self):
    # 也可写'yyyy-MM-dd ··· 'ctrl+alt+b查看自带的样式self.label.setText(time)        	
    time = QDateTime.currentDateTime().toString(Qt.DateFormat(5))
    self.label.setText(time)

# 开始线程，设置每次运行事件1000毫秒
def start_event(self):
    self.timer.start(1000)
    # 将开始按钮设置不可点击防止多开
    self.start_button.setEnabled(False)
    self.end_button.setEnabled(True)

def end_event(self):
    self.timer.stop()
    self.start_button.setEnabled(True)
    self.end_button.setEnabled(False)

# 5秒后执行一次一般用于退出，这里只是介绍方法
def single_shot(self):
    self.timer.singleShot(5000, self.start_event)
```



# QThread   线程类编写计数器

######   这里用到信号槽的知识。

### 写两个信号:

#####         第一个是线程执行完发送的信号  就是每次事件执行完计数加一

#####         第二个是结束信号，结束时执行的操作，这里是显示消息对话框

###### 实例：用来计数10秒。循环执行玩一次秒数加1、设置在10秒时发送 结束信号

```python
# 创建线程
class WorkThread(QThread):
    timer = pyqtSignal()   # 每隔1秒发送一次信号
    end = pyqtSignal()     # 计数完成后发送一次信号

    def run(self):
        global sec
        while True:
            self.sleep(1)  # 休眠1秒
            if sec == 10:
                self.end.emit()   # 发送end信号
                break
            self.timer.emit()   # 发送timer信号
            
  
# 界面显示部分
class Thread(QWidget):

    def __init__(self, parent=None):
        super(Thread, self).__init__(parent)
        self.setWindowTitle('计时器控件')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(600, 500)

        layout = QVBoxLayout()

        # 显示屏控件
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        layout.addWidget(button)

        # 调用线程
        self.workThread = WorkThread()

        # 收到timer信号进行的事件
        self.workThread.timer.connect(self.count_time)
        # 收到end信号进行的事件
        self.workThread.end.connect(self.end)
        button.clicked.connect(self.work)

        self.setLayout(layout)

    # 计数事件
    def count_time(self):
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        QMessageBox.information(self, '消息', '计数结束', QMessageBox.Ok)

    # 线程调用start方法开始进行
    def work(self):
        self.workThread.start()
```

