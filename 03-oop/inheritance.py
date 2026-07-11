# 基类
class Animal:
    """动物类"""
    
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def speak(self):
        return f"{self.name}说: {self.sound}!"
    
    def __str__(self):
        return f"Animal({self.name})"

# 派生类
class Dog(Animal):
    """狗类，继承自Animal"""
    
    def __init__(self, name, breed):
        super().__init__(name, "汪汪")
        self.breed = breed
    
    def fetch(self):
        return f"{self.name}去捡球了!"

class Cat(Animal):
    """猫类，继承自Animal"""
    
    def __init__(self, name, color):
        super().__init__(name, "喵喵")
        self.color = color
    
    def climb(self):
        return f"{self.name}去爬树了!"

# 使用继承
dog = Dog("旺财", "金毛")
cat = Cat("咪咪", "白色")

print(dog.speak())
print(dog.fetch())
print(cat.speak())
print(cat.climb())
print(isinstance(dog, Animal))  # True
