class BankAccount:
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, amountToWithdraw):
        self.balance -= amountToWithdraw
    def deposit(self, amountToDeposit):
        self.balance += amountToDeposit
    def printBalance(self):
        print(f"Your balance is: {self.balance}")

p1 = BankAccount(10000, "Jack", 293)
p1.deposit(2000)
p1.withdraw(3000)
p1.printBalance()