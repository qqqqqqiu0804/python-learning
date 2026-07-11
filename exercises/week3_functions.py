# 题目1: 计算阶乘
def factorial(n):
    """计算阶乘"""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"5的阶乘: {factorial(5)}")

# 题目2: 判断回文字符串
def is_palindrome(s):
    """判断回文字符串"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"'level'是回文: {is_palindrome('level')}")
print(f"'hello'是回文: {is_palindrome('hello')}")

# 题目3: 生成斐波那契数列
def fibonacci(n):
    """生成斐波那契数列"""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

print(f"前10个斐波那契数: {fibonacci(10)}")

# 题目4: 函数装饰器
def timer_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"函数 {func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    return wrapper

@timer_decorator
def slow_function():
    """慢函数"""
    import time
    time.sleep(0.1)
    return "完成"

print(slow_function())

# 题目5: 闭包示例
def outer_func(x):
    """外层函数"""
    def inner_func(y):
        """内层函数"""
        return x + y
    return inner_func

add5 = outer_func(5)
print(f"add5(3) = {add5(3)}")
