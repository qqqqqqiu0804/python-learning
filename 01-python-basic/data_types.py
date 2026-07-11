# 数字类型
integer_num = 100
float_num = 3.14
complex_num = 3 + 4j

print(f"整数: {integer_num}, 类型: {type(integer_num)}")
print(f"浮点数: {float_num}, 类型: {type(float_num)}")
print(f"复数: {complex_num}, 类型: {type(complex_num)}")

# 字符串
str1 = "Hello"
str2 = 'Python'
str3 = """多行
字符串"""
print(f"字符串: {str1} {str2}")
print(f"多行字符串: {str3}")

# 布尔值
is_true = True
is_false = False
print(f"布尔值: {is_true}, {is_false}")

# 类型转换
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
print(f"字符串转整数: {num_int}")
print(f"字符串转浮点数: {num_float}")
