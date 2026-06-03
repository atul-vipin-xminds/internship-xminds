def restaurant_order(*items_price, **customer):
    delivery_charge = 100
    total_order = sum(items_price)
    final_bill = total_order + delivery_charge

    print("Customer Name :", customer["name"])
    print("Order Value   :", total_order)
    print("Delivery Fee  :", delivery_charge)
    print("Total Bill    :", final_bill)

restaurant_order(250, 180, 120, name="Anu")