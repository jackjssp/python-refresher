class BankAccount:
    def __init__(self, balance, name, number):
        self.balance = balance
        self.name = name
        self.number = number

    def withdraw(self, amountToWithdraw):
        self.transaction(-amountToWithdraw)

    def deposit(self, amountToDeposit):
        self.transaction(amountToDeposit)

    def transaction(self, amount):
        if (self.balance + amount < 0):
            print("You cannot withdraw more than you have.")
        else:
            self.balance += amount

    def printBalance(self):
        print(f"The balance of account {self.number} is: {self.balance}")

p1 = BankAccount(10000, "Jack", 293)
p1.deposit(2000)
p1.withdraw(13000)
p1.withdraw(3000)
p1.printBalance()