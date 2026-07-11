# 条件语句
score = 85
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 70:
    grade = "中等"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"成绩 {score} 分，等级: {grade}")

# for循环
print("\nfor循环示例:")
for i in range(1, 11):
    print(i, end=" ")
print()

# 遍历列表
fruits = ["苹果", "香蕉", "橙子"]
for fruit in fruits:
    print(f"我喜欢吃{fruit}")

# while循环
print("\nwhile循环示例:")
count = 0
while count < 5:
    print(f"计数: {count}")
    count += 1

# break和continue
print("\nbreak示例:")
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

print("continue示例:")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
