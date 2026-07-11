import os
from pathlib import Path

# 读取文件
print("读取文件:")
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# 逐行读取
print("\n逐行读取:")
with open("data.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# 写入文件
print("\n写入文件:")
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("这是写入的内容\n")
    file.write("第二行内容\n")

# 使用pathlib
print("\n使用pathlib:")
data_path = Path("data.txt")
print(f"文件存在: {data_path.exists()}")
print(f"文件大小: {data_path.stat().st_size} 字节")
print(f"文件后缀: {data_path.suffix}")

# 列出当前目录
print("\n当前目录文件:")
for item in Path(".").iterdir():
    print(f"{'[目录]' if item.is_dir() else '[文件]'} {item.name}")