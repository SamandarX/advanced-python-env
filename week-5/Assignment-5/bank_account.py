class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner 
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Not enough balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def get_balance(self):
        return self.__balance

account = BankAccount("Sam", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

print("Current balance:", account.get_balance())
