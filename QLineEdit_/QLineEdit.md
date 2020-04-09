# QLineEdit

### 一、QLineEconMode  （回显模式）

1: normal 正常显示
		2: noEchol 不显示
		3: password 密码不可见
		4: passwordEchoOnEditLineEdit  密码可见



### 二、Validator 验证器



#### PyQt5.QtGui

IntValidator   整数验证器

DoubleValidator   浮点数（双精型）

RegExp   正则验证器    需要用到    **PyQt5.QtCore import QRegExp  工具里面的正则表达式**



### 三、用掩码限制QLineEdit控件的输入

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

\#    ASCI数字字符或加减符号是允许输入的,但不是必需的

H    十六进制格式字符是必须输入的(A-F、a-f、0-9)
		h    十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)
		B    二进制格式字符是必须输入的(0,1)
		b    二进制格式字符是允许输入的,但不是必需的(0,1)

\>	所有的字母字符都大写
		<    所有的字母字符都小写
		!    关闭大小写转换
		\    使用"\\"转义上面列出的字符