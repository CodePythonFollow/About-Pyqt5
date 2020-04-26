# QTableView    QTableWidget

###### 一、 QTableView二维表格数据

+ 必须一个model 数据源

+ 解耦合的思想，将界面和数据相分离

+ 每一格数据是一个  **QStandardItem**  对象

  ```python
  # 创建标准model对象  控制几行几列
  model = QStandardItemModel(5, 3)
  # 设置水平表头
  model.setHorizontalHeaderLabels(['id', '姓名', '年龄'])
  # 创建表格
  table_view = QTableView(self)
  table_view.move(20, 50)
  table_view.resize(500, 300)
  # 表格与数据相联系
  table_view.setModel(model)
  # 添加数据
  model.setItem(0, 0, QStandardItem('001'))
  model.setItem(0, 1, QStandardItem('张三'))
  model.setItem(0, 2, QStandardItem('15'))
  ```

  

###### 二、 QTableWidget是QTableView的一个子类

+ 每一格对象是  **QTableWidgetItem**  对象

+ **不需要再用model对象**创建数据

+ 常用操作，一般用到再查这里只运用部分进行演示

+ **setItem**：将文本放到单元格中

+ **setCellWidget**：将控件放到单元格中（多个控制尺寸可能会有冲突）

  ```python
  table_widget = QTableWidget(self)
  table_widget.move(20, 30)
  table_widget.resize(500, 300)
  # 设置行数和列数
  table_widget.setRowCount(4)
  table_widget.setColumnCount(3)
  table_widget.setHorizontalHeaderLabels(['id', 'name', 'old'])
  # 添加数据
  table_widget.setItem(0, 0, QTableWidgetItem('1'))
  table_widget.setItem(0, 1, QTableWidgetItem('张三'))
  table_widget.setItem(0, 2, QTableWidgetItem('15岁'))
  # 禁止编辑
  table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
  # 整行选择
  table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
  # 调整列和行随着内容改变
  table_widget.resizeColumnsToContents()
  table_widget.resizeRowsToContents()
  # 相当于QHeaderView对象设置隐藏不显示 头
  # table_widget.horizontalHeader().setVisible(False)
  # 隐藏网格线
  table_widget.setShowGrid(False)
  # 放下拉框控件进去
  combobox = QComboBox()
  # combobox.resize(100, 20)
  combobox.addItem('01')
  combobox.addItem('02')
  table_widget.setCellWidget(1, 0, combobox)
  ```

+ 查找单元格（根据条件）可设置各种规则，如正则或者自带方法   **自动补全提示**  或者 查源码

+ 单元格设置字体和颜色     更多字体可在网上查询    颜色rgb和rgba可在网上查看有关介绍

  + 宋体 SimSun
  
  + 黑体 SimHei
  
  + 微软雅黑 Microsoft YaHei
  
  + 微软正黑体 Microsoft JhengHei
  
+ 设置文本对齐  **setTextAlignment** 
  
+ 设置行高和列宽    **setRowHeight**   **setColumnWidth**
  
  ```python
  # 设置行高和列宽   第一行的高度和宽度
  table_widget.setRowHeight(0, 80)    
  table_widget.setColumnWidth(0, 100)
  # 添加30 * 3的数据
  for r in range(30):
      for c in range(3):
          table_widget.setItem(r, c, QTableWidgetItem(f"({r}, {c})"))
  # 查找以匹配规则（'(1'）开始的item（单元格数据）
  items = table_widget.findItems('(1', Qt.MatchStartsWith)
  # 对每个item设置一定的样式（字体和颜色）   
  if items:          
      for item in items:
          item.setBackground(QBrush(QPixmap('../images/python.png')))  
          item.setForeground(QBrush(QColor(255, 0, 0)))   # 前景色这里指的是字体颜色
          item.setFont(QFont('SimSun', 15, 10))
          item.setTextAlignment(Qt.AlignRight)
  ```
  
+ 按表格某一列值排序    **sortItems**
  + 列索引            columnIndex
  + 升降序            orderType
  
+ **setSpan（row， col， rowspan， colspan）**

  ```python
  #添加数据
  table_widget.setItem(0, 0, QTableWidgetItem('1'))
  table_widget.setItem(0, 1, QTableWidgetItem('小强'))
  table_widget.setItem(0, 2, QTableWidgetItem('16'))
  table_widget.setItem(1, 0, QTableWidgetItem('2'))
  table_widget.setItem(1, 1, QTableWidgetItem('张三'))
  table_widget.setItem(1, 2, QTableWidgetItem('15'))
  table_widget.setItem(2, 0, QTableWidgetItem('3'))
  table_widget.setItem(2, 1, QTableWidgetItem('小明'))
  table_widget.setItem(2, 2, QTableWidgetItem('14'))
  table_widget.setItem(3, 0, QTableWidgetItem('4'))
  table_widget.setItem(3, 1, QTableWidgetItem('大明'))
  table_widget.setItem(3, 2, QTableWidgetItem('18'))
  # 设置跨行
  table_widget.setSpan(3, 2, 2, 1)
  # 排序
  table_widget.sortItems(0, Qt.DescendingOrder)
  # table_widget.sortItems(0, Qt.AscendingOrder)
  ```
  
+ 防止图片并设置图片大小

  + **QTableWidgetItem(QIcon, str)**
  + **setIconSize(QSize(w, h))**

  ```python
  # 放置图片
  table_widget.setItem(4, 0, QTableWidgetItem(QIcon('../images/python.png'), 'python'))
  # 调整图片大小
  table_widget.setIconSize(QSize(20, 20))
  ```

+ 单元格右键菜单栏

  ```python
  # 这里设置一个右键菜单请求
  table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
  table_widget.customContextMenuRequested.connect(self.get_menu)
  
      # 获得位置但是我们需要得到当前的单元格位置
      def get_menu(self, pos):
          table_widget = self.sender()
          # 得到一个QModelIndex对象   有个列函数和行函数 和data函数也可用.text()返回数据  源码只有几十行
          model_index = table_widget.selectionModel().selection().indexes()
          row = model_index[0].row()
          data = model_index[0].data()
          # 创建菜单
          menu = QMenu()
          menu.addAction('打印当前数据')
          menu.addAction('打印当行数据')
          # 阻塞，类似我们窗口每次退出等待app.exit就是用事件触发才会继续
          # 这里我们exec_()不加参数默认是在pos位置打开菜单，但是QPoint对象默认是针对整个屏幕，也就是绝对坐标
          # 所以我们需要让打开的菜单处在当前打开的位置需要将窗口设置成
          screen_point = table_widget.mapToGlobal(pos)
          action = menu.exec_(screen_point)
          # 由于第一行有空值所以我们不打印第一行的数据空的item没有.text()
          if row > 0:
              if action:
                  if action.text() == '打印当前数据':
                      print(data)
                  else:
                      print('当行数据为：' + table_widget.item(row, 0).text(), 											table_widget.item(row, 1).text(), 											table_widget.item(row, 2).text())
  
  ```

  
