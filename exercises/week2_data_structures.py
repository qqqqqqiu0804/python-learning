# 题目1: 找出列表中的最大值和最小值
numbers = [23, 45, 12, 67, 89, 34, 56]
print(f"列表: {numbers}")
print(f"最大值: {max(numbers)}")
print(f"最小值: {min(numbers)}")

# 题目2: 列表去重
original_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique_list = list(set(original_list))
print(f"去重前: {original_list}")
print(f"去重后: {unique_list}")

# 题目3: 字典合并
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(f"合并后: {merged_dict}")

# 题目4: 统计字符出现次数
text = "hello world"
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(f"字符统计: {char_count}")

# 题目5: 列表排序
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = sorted(unsorted_list)
print(f"排序前: {unsorted_list}")
print(f"排序后: {sorted_list}")
