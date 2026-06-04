class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self._holder_name = holder_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def check_balance(self):
        print("Balance:", self.__balance)


acc = BankAccount(101, "John", 5000)

acc.deposit(1000)
acc.withdraw(2000)
acc.check_balance()