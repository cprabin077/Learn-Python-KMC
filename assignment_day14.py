class Account:
    account_number = 6289780928892
    balance = 1000

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Withdrawn {amount}. Remaining balance: {self.balance}"


class SavingsAmount(Account):
    interest_rate = 5

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        return f"Interest added: {interest}. New balance: {self.balance}"


class PremiumSavingsAmount(SavingsAmount):
    reward_points = 120

    def redeem_points(self):
        if self.reward_points >= 100:
            self.balance += 50
            self.reward_points -= 100
            return f"Redeemed 100 points. Remaining reward points: {self.reward_points}. Balance: {self.balance}"
        else:
            return "Not enough reward points"

acc = PremiumSavingsAmount()
print(f"Account Number: {acc.account_number}") # Account Number: 6289780928892
print(f"Opening Balance: {acc.balance}") # Opening Balance: 1000
print(acc.deposit(500)) # Deposited 500. New balance: 1500
print(acc.withdraw(200)) # Withdrawn 200. Remaining balance: 1300
print(acc.add_interest()) # Interest added: 65.0. New balance: 1365.0
print(acc.redeem_points()) # Redeemed 100 points. Remaining reward points: 20. Balance: 1415.0