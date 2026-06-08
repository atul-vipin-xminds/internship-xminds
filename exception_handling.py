#question1

try:
    a = 12
    s = "hello"
    print(a + s)
except TypeError:
    print("Cannot add an integer and a string.")

#question2

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ValueError:
    print("Invalid input. Please enter numeric values.")

except ZeroDivisionError:
    print("Division by zero is not allowed.")

#question3

def format_name(name):
    try:
        return name.capitalize()
    except AttributeError:
        raise TypeError("Argument must be a string")


try:
    print(format_name("abhishek"))
    print(format_name(123))
except TypeError as e:
    print("Error:", e)

#question4

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index number: "))
    print("Element at index", index, "is", numbers[index])

except ValueError:
    print("Error: Please enter a valid numeric index.")

except IndexError:
    print("Error: Index is out of range.")
