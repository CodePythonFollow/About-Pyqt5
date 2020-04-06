#!/user/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: Code
@contact: 1284954990@qq.com
@file: QlineEditMask.py
@time: 2020/4/5 11:59
掩码   (setInputMask)
A    ASCII字母字符是必须输入的(A-Z、a-z)
a    ASCII字母字符是允许输入的,但不是必需的(A-Z、a-z)
N    ASCII字母字符是必须输入的(A-Z、a-z、0-9)
n    ASII字母字符是允许输入的,但不是必需的(A-Z、a-z、0-9)
X    任何字符都是必须输入的
x    任何字符都是允许输入的,但不是必需的
9    ASCII数字字符是必须输入的(0-9)
0    ASCII数字字符是允许输入的,但不是必需的(0-9)
D    ASCII数字字符是必须输入的(1-9)
d    ASCII数字字符是允许输入的,但不是必需的(1-9)
#    ASCI数字字符或加减符号是允许输入的,但不是必需的
H    十六进制格式字符是必须输入的(A-F、a-f、0-9)
h    十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)
B    二进制格式字符是必须输入的(0,1)
b    二进制格式字符是允许输入的,但不是必需的(0,1)
>	所有的字母字符都大写
<    所有的字母字符都小写
!    关闭大小写转换
\    使用"\\"转义上面列出的字符
'''

from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLineEdit
import sys

class InputMask(QWidget):
    def __init__(self):
        super(InputMask, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('掩码')
        formlayout = QFormLayout()

        ipInput = QLineEdit()
        # ;号后面表示为填写显示的符号
        ipInput.setInputMask('000.000.000.000;*')
        formlayout.addRow('&请输入Ip地址：', ipInput)

        # macLineEdit
        macLineEdit = QLineEdit()
        macLineEdit.setInputMask('HH:HH:HH:HH:HH;_')
        formlayout.addRow('请输入字符：',macLineEdit)

        # datatime
        datatimeLine = QLineEdit()
        datatimeLine.setInputMask('0000-00-00;0')
        formlayout.addRow('日期：', datatimeLine)

        # License
        license = QLineEdit()
        license.setInputMask('>AAAA-AAAA-AAAA-AAAA;#')
        formlayout.addRow('认证码：', license)


        self.setLayout(formlayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = InputMask()
    mainwindow.show()
    sys.exit(app.exec_())


