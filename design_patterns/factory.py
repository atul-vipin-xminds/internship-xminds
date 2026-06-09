class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class NetBanking:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


class PaymentFactory:
    @staticmethod
    def get_payment(payment_type):
        if payment_type == "credit":
            return CreditCard()
        elif payment_type == "upi":
            return UPI()
        elif payment_type == "netbanking":
            return NetBanking()
        else:
            return None



payment_type = input("Enter payment method (credit/upi/netbanking): ")
payment_amount = float(input("Enter amount: "))

payment_method = PaymentFactory.get_payment(payment_type)

if payment_method:
    payment_method.pay(payment_amount)
else:
    print("Invalid payment method")