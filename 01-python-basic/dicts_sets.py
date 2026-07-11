# 字典操作
student = {
    "name": "张三",
    "age": 20,
    "major": "计算机科学",
    "grades": [85, 92, 78]
}
print(f"字典: {student}")
print(f"姓名: {student['name']}")
print(f"年龄: {student.get('age', 0)}")

# 字典方法
student["gender"] = "男"
print(f"添加后: {student}")
del student["grades"]
print(f"删除后: {student}")
print(f"所有键: {list(student.keys())}")
print(f"所有值: {list(student.values())}")

# 字典推导式
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"平方字典: {squares_dict}")

# 集合
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"集合1: {set1}")
print(f"集合2: {set2}")
print(f"交集: {set1 & set2}")
print(f"并集: {set1 | set2}")
print(f"差集: {set1 - set2}")
