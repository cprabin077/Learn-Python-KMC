class BankAccount():
    account_holder = "XYZ"
    __balance = 1000

    def deposit(self, amount):
        self.__balance += amount
        return f"Name of Account holder is {self.account_holder}\nThe deposited amount is {amount}\nTotal balance is {self.__balance}"
    
    def withdraw(self, amount):
        self.__balance -= amount
        return f"The fined amount is {amount}"
    
    def showBalance(self):
        return f"The remaining balance is {self.__balance}"
    
class StudentAccount(BankAccount):
    studentId = 101

    def pay_library_fine(self, amount):
        return self.withdraw(amount)
    
obj = StudentAccount()
print(obj.deposit(200))
print(obj.pay_library_fine(100))
print(obj.showBalance())

''' # Output
Name of Account holder is XYZ
The deposited amount is 200
Total balance is 1200
The fined amount is 100
The remaining balance is 1100

'''

        



