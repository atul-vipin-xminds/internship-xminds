class InsufficientBalanceError(Exception):
    pass


balance = 10000

try:
    withdrawal_amount = float(input("Enter amount to withdraw: "))

    if withdrawal_amount > balance:
        raise InsufficientBalanceError("Not enough balance in your account.")

    balance = balance - withdrawal_amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except InsufficientBalanceError:
    print("Insufficient balance!")
    print("Available balance:", balance)