#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QDataTimeEdit_.py
@time: 2020/4/14 0:24

QDataTimeEdit  设置不同的风格的日期和时间
"""
import sys

from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class DataTimeEdit(QWidget):
    def __init__(self):
        super(DataTimeEdit, self).__init__()
        self.label = QLabel(self)
        self.unit_ui()

    def unit_ui(self):
        self.setWindowTitle('不同风格的时间格式')
        self.setWindowIcon(QIcon(QPixmap('../images/python.png')))
        self.resize(800, 500)

        layout = QVBoxLayout()
        self.setLayout(layout)
        date_time1 = QDateTimeEdit(QDateTime.currentDateTime())

        # 设置一些属性
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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = DataTimeEdit()
    main_window.show()
    sys.exit(app.exec_())

