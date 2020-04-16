# QPrinter   打印对象

## QtPrintSupport  是所有有关打印的父类()

>  有关类的介绍引用自  https://www.cnblogs.com/findumars/p/6152822.html

> | QAbstractPrintDialog | base implementation for print dialogs used to configure printers |
| -------------------- | ------------------------------------------------------------ |
| QPageSetupDialog     | configuration dialog for the page-related options on a printer |
| QPrintDialog         | Dialog for specifying the printer's configuration            |
| QPrintEngine         | Defines an interface for how QPrinter interacts with a given printing subsystem |
| QPrintPreviewDialog  | Dialog for previewing and configuring page layouts for printer output |
| QPrintPreviewWidget  | Widget for previewing page layouts for printer output        |
| QPrinter             | Paint device that paints on a printer                        |
| QPrinterInfo         | Gives access to information about existing printers          |

> - 抽象文档打印对话框类，提供配置打印机的打印对话框基本实现；
> - 页面设置对话框类，和打印页面相关参数的配置对话框；
> - 打印对话框类，指定打印机配置的对话框；
> - 打印引擎类，定义了Q Printer类如何与打印子系统交互的接口；
> - 打印预览对话框类，用来预览和配置页面布局的对话框；
> - 打印预览控件类，预览页面布局的控件；
> - 打印机类，指示打印机如何工作。
> - 打印机信息类 有关打印机的信息



**小提示**：*可以在 Typora 设置里面的偏好设置取消自动检查拼写否则会出现很多波浪号（如果强迫症的话）*



```python
'''
介绍：
	比较综合的一个案例：
	
		一、用到三个action：
			1、 Open File   打开文件对话框
			2、 Print_set   打印设置对话框
			3、 print       打印对话框
			
		二、用到打印的两种方法
			1、 控件的print方法
			2、 控件的grab方法得到QPixmap对象 再用 QPainter 对象  *绘制*  到 QPrinter 对象
											 （ 很     像     别     看     错  ）
'''

# 放一个菜单栏   打印设置窗口
menu_bar = self.menuBar()				 # 菜单栏
menu = QMenu('File', self)        		 # 文件菜单
open_file = QAction('Open File', self)   # 打开文件用到文件对话框（考虑了多种图片和文本文件）
print_ = QAction('Print Set', self)      # 打印设置对话框
menu.addAction(open_file)				 
menu.addAction(print_)
menu_bar.addMenu(menu)

# 打印机对象
self.printer = QPrinter()			

# 工具栏   这个是打开 ： 打印对话框    
toolbar = self.addToolBar('Printer')    
tool_action = QAction(QIcon('../images/printer.png'), 'print', self)
toolbar.addAction(tool_action)

# 绑定事件  
open_file.triggered.connect(self.open_file)
print_.triggered.connect(self.set_printer_dialog)
tool_action.triggered.connect(self.print_dialog)

# 给一个工具栏打印当前窗口的文本
self.text_edit = QTextEdit(self)
self.text_edit.setGeometry(20, 80, self.width()-40, self.height()-100)
self.text_edit.setFont(QFont('Times New Roman', 15, 10))

# 打开文件对话框
def open_file(self):
    filename, _ = QFileDialog.getOpenFileName(self, '打开文件', '.', '所有文件 *.*')
    try:
        with open(filename, 'r', encoding='utf-8') as fi:
            self.text_edit.setText(fi.read())
    except UnicodeDecodeError:
        self.text_edit.setHtml("<img src=%s>" % filename)

# 打印设置对话框
def set_printer_dialog(self):
    set_dialog = QPageSetupDialog(self.printer, self)
    set_dialog.exec()

# 打印对话框
def print_dialog(self):
    print_dialog = QPrintDialog(self.printer, self)
    # 打印对话框点击确认再执行
    if QDialog.Accepted == print_dialog.exec_():
        # 打印的第一种方法直接执行控件的打印方法
        # self.text_edit.print(self.printer)

        # 打印的第二种方法还能画到printer对象里面的方式打印图片
        screen = self.text_edit.grab()   # .QPixmap对象
        painter = QPainter()
        painter.begin(self.printer)
        painter.drawPixmap(0, 0, screen)
        painter.end()

        print('print end')
```