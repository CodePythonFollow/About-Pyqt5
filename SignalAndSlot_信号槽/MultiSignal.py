#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: MultiSignal.py
@time: 2020/5/16 17:22
"""

from PyQt5.QtCore import *


class MultiSignal(QObject):

    signal1 = pyqtSignal(int, str)
    signal2 = pyqtSignal(list)
    signal3 = pyqtSignal(dict)

    # 声明一个重载版本信号，也就是
    signal4 = pyqtSignal([int], [int, str])

    def __init__(self):
        super(MultiSignal, self).__init__()
        self.signal1.connect(self.signal_1)
        self.signal1.emit(1, 'one')
        self.signal2.connect(self.signal_2)
        self.signal2.emit([1, 2, 3])
        self.signal3.connect(self.signal_3)
        self.signal3.emit({'name': 'code'})

        # 绑定需要注意要指定那种类型 发送信号也要指定
        self.signal4[int].connect(self.signal_4_1)
        self.signal4[int].emit(4)
        self.signal4[int, str].connect(self.signal_4_2)
        self.signal4[int, str].emit(4, '1')

    @staticmethod
    def signal_1(*args):
        print([i for i in args])

    @staticmethod
    def signal_2(*args):
        print(args)

    @staticmethod
    def signal_3(kwargs):
        print(kwargs)

    @staticmethod
    def signal_4_1(*args):
        print([i for i in args])

    @staticmethod
    def signal_4_2(*args):
        print([i for i in args])


if __name__ == '__main__':
    multi_signal = MultiSignal()
