# 基本函数
def greet(name):
    """问候函数"""
    return f"你好, {name}!"

print(greet("Python"))

# 默认参数
def power(base, exponent=2):
    """幂运算函数"""
    return base ** exponent

print(f"2的平方: {power(2)}")
print(f"2的立方: {power(2, 3)}")

# 可变参数
def calculate_sum(*numbers):
    """求和函数"""
    return sum(numbers)

print(f"求和: {calculate_sum(1, 2, 3, 4, 5)}")

# 关键字参数
def print_info(**kwargs):
    """打印信息函数"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="张三", age=25, city="北京")

# lambda函数
square = lambda x: x ** 2
print(f"lambda平方: {square(5)}")

# 函数作为参数
def apply_function(func, value):
    """应用函数"""
    return func(value)

print(f"应用lambda: {apply_function(lambda x: x * 2, 5)}")
