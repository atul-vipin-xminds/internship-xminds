'''Write a program that prints the price of a sandwich order according to the sandwich filling a customer chooses. First you need to check whether the customer has ordered the item that is in our menu(Sandwich Menu: Chicken = 120, Beef = 150, Veg = 100) then print the price to the console according to his/her order?'''

order = input("Enter sandwich filling: ")

match order:
    case "Chicken":
        print("Price = 120")
    case "Beef":
        print("Price = 150")
    case "Veg":
        print("Price = 100")
    case _:
        print("Item not available in menu")