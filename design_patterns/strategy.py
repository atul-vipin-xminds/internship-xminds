class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class NetBanking:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount):
        self.payment_strategy.pay(amount)


payment_type = input("Enter payment method (credit/upi/netbanking): ")
payment_amount = float(input("Enter amount: "))

if payment_type == "credit":
    strategy = CreditCard()
elif payment_type == "upi":
    strategy = UPI()
elif payment_type == "netbanking":
    strategy = NetBanking()
else:
    strategy = None

if strategy:
    payment = PaymentContext(strategy)
    payment.make_payment(payment_amount)
else:
    print("Invalid payment method")