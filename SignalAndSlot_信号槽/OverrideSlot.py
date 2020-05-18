#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: OverrideSlot.py
@time: 2020/5/18 0:20
"""
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Override(QWidget):
    def __init__(self):
        super(Override, self).__init__()
        self.setWindowTitle('override')

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == Qt.Key_Escape:
            self.close()

        else:
            self.setWindowTitle(f'点击了 {str(QKeyEvent.text())}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = Override()
    main_window.show()
    sys.exit(app.exec_())
