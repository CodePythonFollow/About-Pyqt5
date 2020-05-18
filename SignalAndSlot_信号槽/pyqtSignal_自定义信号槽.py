#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: pyqtSignal_自定义信号槽.py
@time: 2020/5/13 23:04
"""

from PyQt5.QtCore import pyqtSignal, QObject


# 定义信号
class Signal(QObject):
    signal = pyqtSignal(str, int)

    # 发送信号指令
    def run(self, arg=('参数', 1)):
        self.signal.emit(*arg)


# 定义槽函数
def get_signal(arg, i):
    print('收到' + arg + str(i))


if __name__ == '__main__':
    # 实例化
    signal = Signal()
    # 绑定
    signal.signal.connect(get_signal)
    # 发送信号
    signal.run()
