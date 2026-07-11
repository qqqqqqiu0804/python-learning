# 题目1: 交换两个变量的值
a = 5
b = 10
print(f"交换前: a={a}, b={b}")
a, b = b, a
print(f"交换后: a={a}, b={b}")

# 题目2: 判断奇偶数
num = 7
if num % 2 == 0:
    print(f"{num}是偶数")
else:
    print(f"{num}是奇数")

# 题目3: 判断闰年
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")

# 题目4: 计算绝对值
num = -15
if num >= 0:
    abs_num = num
else:
    abs_num = -num
print(f"{num}的绝对值是: {abs_num}")

# 题目5: 十进制转二进制
num = 42
print(f"{num}的二进制表示: {bin(num)}")
