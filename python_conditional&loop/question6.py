'''Input a number check if the number is positive or negative or zero and display an appropriate message use nested if statement?'''

num = int(input("Enter a number: "))

match (num > 0, num < 0):
    case (True, False):
        print("Positive")
    case (False, True):
        print("Negative")
    case (False, False):
        print("Zero")