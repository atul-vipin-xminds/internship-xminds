class BankManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.account_list = []
        return cls._instance

    def add_account(self, acc_no):
        self.account_list.append(acc_no)

    def show_accounts(self):
        print(self.account_list)


manager1 = BankManager()
manager2 = BankManager()

manager1.add_account(101)
manager2.add_account(102)

manager1.show_accounts()

print(manager1 is manager2)