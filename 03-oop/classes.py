# 基本类定义
class Dog:
    """狗类"""
    
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age
    
    def bark(self):
        """叫的方法"""
        return f"{self.name}说: 汪汪!"
    
    def get_info(self):
        """获取信息"""
        return f"名字: {self.name}, 年龄: {self.age}岁"

# 创建对象
my_dog = Dog("旺财", 3)
print(my_dog.bark())
print(my_dog.get_info())

# 类属性和实例属性
class Student:
    """学生类"""
    school = "Python学校"  # 类属性
    
    def __init__(self, name, grade):
        self.name = name  # 实例属性
        self.grade = grade
    
    def introduce(self):
        return f"我是{self.name}, 在{self.school}上{self.grade}年级"

student1 = Student("小明", 3)
print(student1.introduce())
