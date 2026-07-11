# 导入整个模块
import math
print(f"π的值: {math.pi}")
print(f"平方根: {math.sqrt(16)}")

# 导入特定函数
from random import randint, choice
print(f"随机整数: {randint(1, 100)}")
print(f"随机选择: {choice(['苹果', '香蕉', '橙子'])}")

# 导入自定义模块
import my_module
print(f"加法: {my_module.add(5, 3)}")
print(f"乘法: {my_module.multiply(4, 6)}")

# 从模块导入特定内容
from my_module import PI
print(f"PI值: {PI}")

# 导入模块并起别名
import datetime as dt
today = dt.date.today()
print(f"今天日期: {today}")