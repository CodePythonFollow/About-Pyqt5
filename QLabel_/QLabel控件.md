# QLabel

1. setAlignment   设置文本的对齐方式 （如：Qt.AlignCenter）

2. setIndex            设置文本缩进（如：）

3. text                     获取文本内容 

4. setBuddy           设置伙伴关系   （文本和输入框）    表单布局addrow比较方便，不需手动生成伙伴关系     

   ​                                                                                         和label提示

5. setText               设置文本内容   （支持富文本  html文本）

6. selectedText      返回所选择的字符

7. setWordWrap    设置是否允许换行

   ## Qlabel常用的信号（事件）

   1. 当鼠标滑过QLabel控件时触发：linkHovered
   
2. 当鼠标点击QLabel控件时触发：linkActivated
   
      # 设置信号槽
      ```python
          label2.linkHovered.connect(self.linkHovered)
          label4.linkActivated.connect(self.linkActivated)
          
          # 鼠标滑过事件
          def linkHovered(self):
              print('鼠标从此滑过label2')
      
          # 鼠标点击事件
          def linkActivated(self):
              print('鼠标点击label4')
      ```
   
   

