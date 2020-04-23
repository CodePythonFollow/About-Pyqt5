# About-Pyqt5

###### 				PyQt5介绍，每个文件下是各个控件的介绍和基本使用，核心代码在每个文件下的笔记中都有罗列。

###### 		        代码部分为具体的实现和基本使用，修改日期基本上是我学习做笔记的日期，前面可能很多不太规范，但是所有的导包和逻辑还算清楚。后面没有做过多的修改，很多不懂的在后面慢慢弄懂后都有补充和修改，有的可能在后面进行了补充。    (*^▽^*)

### 一、PyQt5包介绍

+ PyQt5.QtWidgets                         各种控件用来布局       如按钮窗口等

+ PyQt5.QtGui                                 关于展示有关类           如画笔、笔刷、颜色、字体、图片等

+ PyQt5.QtCore                               关于各种工具               如正则工具、日期工具等

  + 这里面有个**Qt**                 里面包含各种常量       如颜色常量、对齐方式、排序常量等

+ PyQt5.QtPrintSupport                与打印有关的所有控件、窗口等

### 二、基本使用（常用的逻辑）    我们以后写的基本都是3、4部分

   1. 创建一个类 继承自PyQt5的基本窗口如**QMainWindow、QWidget**    继承初始化参数（super）

   2. 初始化界面  如设置图标、标题、尺寸

   3. 将有关控件和布局部分写在一个类方法里面并默认执行         **（基本的布局）**  

   4. 将事件作为类方法并绑定到个控件的触发或点击等事件中      **（用来交互）**

   5. 将界面放置到系统、并实例化我们创建的类、调用show方法、系统退出等待界面退出    **（必须）**

      ![images](https://github.com/CodePythonFollow/About-Pyqt5/blob/master/images/%E6%B5%81%E7%A8%8B.png)
      
      

### 三、技巧介绍（很多不仅限于本项目）

+ PyQt5日志pycharm默认不显示 ，按下面这篇文章设置。

  >  https://blog.csdn.net/qq842977873/article/details/82505575

+ 由于Python的原因PyQt5的各种参数控件等都是一个**类**，所以当我们需要用到什么控件可以查看该类的方法等（Ctrl+该类名即可跳转至该函数的源代码）     主要看**类的注释部分**    **如下：**

  ![](https://github.com/CodePythonFollow/About-Pyqt5/blob/master/images/介绍.png)

  

+ 有的时候我们想知道我们写到某些方法时不知道里面的参数**按住ctrl鼠标放在这个函数名上**显示我们需要**写入的参数**   如图：

  ![](https://github.com/CodePythonFollow/About-Pyqt5/blob/master/images/方法.png)
  
  

+ 关于静态方法的使用，简单理解为 类方法里面没用到关键词   **self**    就可以换成**@staticmethod**

  其实如果没用到pycharm也会有波浪线提示   (不用也没关系，一开始没怎么注意，后面基本把有波浪线																				的部分都换了，遵循PEP 8规范 *其实是看着波浪线不舒服*)

  ![](https://github.com/CodePythonFollow/About-Pyqt5/blob/master/images/静态.png)

+ 当我们设置到类似一些需要用到常量的部分可以先按照源码写，当我们想看看其他状态时**点击当前的设置的状态**按住  **ctrl + alt + b**查看引用的位置可查到状态的有关参数。具体值可在看定义位置

  如下面.**setCheckState**方法源码第二个参数写的是Qt.CheckState

  首先我们按照源码**写示例的这个状态**然后我们按住该快捷键**(ctrl + alt + b)**就能t跳到到如下位置   **前面有个※可以点击即可看到该状态的值**
  
  <img src="https://github.com/CodePythonFollow/About-Pyqt5/blob/master/images/State.png" style="zoom:150%;" />
  <video src="https://github.com/CodePythonFollow/About-Pyqt5/blob/master/images/%E7%AE%80%E5%8D%95%E6%8A%80%E5%B7%A7.mp4"></video>
