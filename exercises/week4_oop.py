# 题目1: 创建银行账户类
class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        """存款"""
        if amount > 0:
            self.balance += amount
            return f"存入{amount}元，余额{self.balance}元"
        return "存款金额必须大于0"
    
    def withdraw(self, amount):
        """取款"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"取出{amount}元，余额{self.balance}元"
        return "余额不足或金额无效"
    
    def get_balance(self):
        """查询余额"""
        return f"当前余额: {self.balance}元"

# 测试银行账户
account = BankAccount("张三", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())

# 题目2: 创建矩形类
class Rectangle:
    """矩形类"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """计算面积"""
        return self.width * self.height
    
    def perimeter(self):
        """计算周长"""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """判断是否为正方形"""
        return self.width == self.height

rect = Rectangle(5, 3)
print(f"面积: {rect.area()}")
print(f"周长: {rect.perimeter()}")
print(f"是正方形: {rect.is_square()}")

# 题目3: 创建学生管理系统
class StudentManager:
    """学生管理系统"""
    
    def __init__(self):
        self.students = []
    
    def add_student(self, name, grade):
        """添加学生"""
        self.students.append({"name": name, "grade": grade})
        return f"已添加学生: {name}"
    
    def find_student(self, name):
        """查找学生"""
        for student in self.students:
            if student["name"] == name:
                return student
        return None
    
    def get_average_grade(self):
        """计算平均成绩"""
        if not self.students:
            return 0
        total = sum(s["grade"] for s in self.students)
        return total / len(self.students)

manager = StudentManager()
print(manager.add_student("小明", 85))
print(manager.add_student("小红", 92))
print(manager.add_student("小刚", 78))
print(f"平均成绩: {manager.get_average_grade()}")
