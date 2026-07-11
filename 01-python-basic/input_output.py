# print()函数的各种用法
print("默认输出")
print("指定分隔符", end=" | ")
print("下一行")
print("多个参数", "用空格分隔", sep=", ")

# input()函数
name = input("请输入你的名字: ")
print(f"你好, {name}!")

# 类型转换输入
age = int(input("请输入你的年龄: "))
height = float(input("请输入你的身高(米): "))
print(f"你 {age} 岁, 身高 {height} 米")

# 综合练习：简单计算器
print("\n简单计算器")
num1 = float(input("请输入第一个数字: "))
operator = input("请输入运算符(+,-,*,/): ")
num2 = float(input("请输入第二个数字: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "错误: 除数不能为零"
else:
    result = "错误: 无效的运算符"

print(f"结果: {num1} {operator} {num2} = {result}")