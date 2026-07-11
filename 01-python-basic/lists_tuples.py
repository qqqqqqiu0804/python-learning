# 列表操作
fruits = ["苹果", "香蕉", "橙子", "葡萄"]
print(f"列表: {fruits}")
print(f"第一个元素: {fruits[0]}")
print(f"最后一个元素: {fruits[-1]}")
print(f"切片: {fruits[1:3]}")

# 列表方法
fruits.append("西瓜")
print(f"添加后: {fruits}")
fruits.insert(1, "草莓")
print(f"插入后: {fruits}")
fruits.remove("香蕉")
print(f"删除后: {fruits}")
fruits.pop()
print(f"弹出后: {fruits}")

# 列表推导式
squares = [x**2 for x in range(1, 11)]
print(f"平方数: {squares}")

# 元组
colors = ("红", "绿", "蓝")
print(f"元组: {colors}")
print(f"元组长度: {len(colors)}")