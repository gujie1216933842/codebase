'''

python是一门解释型语言,从上往下解释
1.定义
模块:用来从逻辑上组织python代码(变量,函数,类,逻辑:实现一个功能),本质上就是.py文件结尾的python文件(文件名:test.py,对应的模块名:test)

2.导入方法
import
from   import

3.import本质(路径搜索和搜索路径)
导入模块的本质就是把python文件解释一遍


4.包的定义:
  本质就是一个文件夹目录,目录中必须带有一个__init__.py文件
  包是从逻辑上组织模块的,里面放多个模块文件

  导入包的本质:就是解释包下面的__init__.py文件


5.import module
会寻找module.py的路径
寻找顺序  sys.path列表













'''