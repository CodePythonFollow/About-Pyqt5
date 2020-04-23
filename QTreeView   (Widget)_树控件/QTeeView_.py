#!/user/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Code
@contact: 1284954990@qq.com
@file: QTeeView_.py
@time: 2020/4/22 22:59
"""

import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 文件数据模型
    model = QDirModel()
    tree = QTreeView()
    tree.setModel(model)
    tree.setWindowTitle('QTreeView')
    tree.resize(800, 500)
    tree.show()

    sys.exit(app.exec_())

