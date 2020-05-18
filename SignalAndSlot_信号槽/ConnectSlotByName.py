#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: ConnectSlotByName.py
@time: 2020/5/17 17:49
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore


class ConnectSlotByName(QWidget):

    # noinspection PyArgumentList
    def __init__(self):
        super(ConnectSlotByName, self).__init__()
        self.resize(400, 200)
        button = QPushButton('ok', self)
        button.setObjectName('ok')
        cancel = QPushButton('cancel', self)
        cancel.setObjectName('cancel')
        cancel.move(200, 0)

        # 设置自动连接通过对象名
        QtCore.QMetaObject.connectSlotsByName(self)

    @QtCore.pyqtSlot()
    def on_ok_clicked(self):
        print('ok')

    @QtCore.pyqtSlot()
    def on_cancel_clicked(self):
        print('cancel')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ConnectSlotByName()
    main_window.show()
    sys.exit(app.exec_())
