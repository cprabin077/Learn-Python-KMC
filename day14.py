# # Example-1: Single Inheritance
# class Parent():
#     a = 100
#     b = 45
#     def a1(self):
#         return self.a, self.b

# class Child(Parent):
#     b = "Prabin Chy"
#     d = 657
#     def a2(self):
#         return self.b, self.d

# obj = Child()
# print(obj.a)
# print(obj.b)
# print(obj.a1())
# print(obj.a2())

# print("------"*20)
# # Example-2: Single Inheritance
# class Parent():
#     a = 100
#     b = 45
#     def add(self):
#         return self.a + self.b

# class Child(Parent):
#     c = "Prabin Chy"
#     d = 657
    
#     def display(self):
#         return self.add()
    
#     def final(self):
#         return self.add() + self.d

# obj = Child()
# print(obj.a) # 100
# print(obj.b)    # 45
# print(obj.d)    # 657
# print(obj.add()) # 145
# print(obj.display()) # 145
# print(obj.final()) # 145 + 657 = 802

# print("------"*20)
# # Example-3 -> Inheritance with constructor
# class TestParent():
#     def __init__(self):
#         print("Parent Class")

# class TestChild(TestParent):
#     def __init__(self):
#         print("Child Class")
#         # TestParent.__init__(self)
#         super().__init__() # Preferable

# obj = TestChild()  

# print("------"*20)
# # Example-3 -> Single Inheritance with constructor
# class TestParent():
#     def __init__(self,x):
#         print("Parent Class")

# class TestChild(TestParent):
#     def __init__(self,a,b,c,d):
#         print("Child Class")
#         self.b = b
#         super().__init__(a) # Preferable

#     def test(self):
#         return self.b # 2

# obj = TestChild(1,2,3,4) 
# print(obj.test()) # 2


# print("------"*20)
# # Example-4 -> Multi-level Inheritance with constructor
# class TestParent():
#     def __init__(self,x):
#         print("Parent Class")

# class TestChild(TestParent):
#     def __init__(self,a,b,c,d):
#         print("Child Class")
#         self.b = b
#         super().__init__(a) # Preferable

#     def test(self):
#         return self.b # 2
    
# class Child(TestChild):
#     pass

# obj = TestChild(1,2,3,4) 


# Class Work -> Banking Management System
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn {amount}. Remaining balance: {self.balance}"


class SavingsAmount(Account):
    def __init__(self, account_number, balance=0, interest_rate=5):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        return f"Interest added: {interest}. New balance: {self.balance}"


class PremiumSavingsAmount(SavingsAmount):
    def __init__(self, account_number, balance=0, interest_rate=5, reward_points=0):
        super().__init__(account_number, balance, interest_rate)
        self.reward_points = reward_points

    def redeem_points(self):
        if self.reward_points >= 100:
            self.balance += 50
            self.reward_points -= 100
            return f"Redeemed 100 points. Bonus added. Balance: {self.balance}"
        else:
            return "Not enough reward points"


acc = PremiumSavingsAmount(6289780928892, 1000)

print(acc.deposit(500)) # Deposited 500. New balance: 1500
print(acc.withdraw(200)) # Withdrawn 200. Remaining balance: 1300
print(acc.add_interest()) # Interest added: 65.0. New balance: 1365.0

acc.reward_points = 120
print(acc.redeem_points()) # Redeemed 100 points. Bonus added. Balance: 1415.0