# Multiple Inheritance->  Banking System 
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


class SavingsAmount:
    def __init__(self, interest_rate=5):
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        return f"Interest added: {interest}. New balance: {self.balance}"


class PremiumSavingsAmount(Account, SavingsAmount):
    def __init__(self, account_number, balance=0, interest_rate=5, reward_points=0):
        Account.__init__(self, account_number, balance)
        SavingsAmount.__init__(self, interest_rate)
        self.reward_points = reward_points

    def redeem_points(self):
        if self.reward_points >= 100:
            self.balance += 50
            self.reward_points -= 100
            return f"Redeemed 100 points. Bonus added. Remaining reward Points: {self.reward_points}. Balance: {self.balance}"
        else:
            return "Not enough reward points"


# Testing
acc = PremiumSavingsAmount(6289780928892, 1000, 5, 120)
print(f"Account Number: {acc.account_number}")
print(f"Opening Balance: {acc.balance}")
print(acc.deposit(500))
print(acc.withdraw(200))
print(acc.add_interest())
print(acc.redeem_points())