'''Input a number check if the number is positive or negative or zero and display an appropriate message use nested if statement?'''

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")