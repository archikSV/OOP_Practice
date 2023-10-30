print("Task 5:\n")

"""
Створіть клас BankAccount з атрибутами balance
та owner, а також методами deposit та withdraw для
здійснення операцій з балансом. Реалізуйте перевірку
на те, що баланс не може стати від'ємним.
"""

# classes
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance set to", self.balance)

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance = 0
            print("Balance cannot be negative! Balance set to 0.")
        else:
            print("Balance set to", self.balance)

# objects
account1 = BankAccount("Jeremy", 100)

# main
account1.deposit(50)
account1.withdraw(20)