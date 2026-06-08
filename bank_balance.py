class InsufficientBalanceError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


balance = 10000

try:
    withdrawal_amount = float(input("Enter amount to withdraw: "))

    if withdrawal_amount > balance:
        raise InsufficientBalanceError("Not enough balance in your account.")

    balance = balance - withdrawal_amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except InsufficientBalanceError as e:
    print(e.message)
    print("Available balance:", balance)