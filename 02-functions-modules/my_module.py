"""自定义模块示例"""

def add(a, b):
    """加法函数"""
    return a + b

def subtract(a, b):
    """减法函数"""
    return a - b

def multiply(a, b):
    """乘法函数"""
    return a * b

def divide(a, b):
    """除法函数"""
    if b != 0:
        return a / b
    return "错误: 除数不能为零"

PI = 3.14159