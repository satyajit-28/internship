'''
@Author:    satyajit 

@Goal:      To implement a command line calculator

@Date:      29th Oct 2026

'''

value1 = float(input("Enter first number: "))
value2 = float(input("Enter second number: "))
operation = input("Enter operation which you want to perform: ")


def operation_type(operation: str) -> float:

    if operation == "+":
        return f"The result is: {value1 + value2}"
    elif operation == "-":
        return f"The result is: {value1 - value2}"
    elif operation == "*":
        return f"The result is: {value1 * value2}"
    elif operation == "/":
        return f"The result is: {value1 / value2}"
    elif operation == "//":
        return f"The result is: {value1 // value2}"
    elif operation == "%":
        return f"The result is: {value1 % value2}"
    elif operation == "**":
        return f"The result is: {value1 ** value2}"
    else:
        return "The current operation is not listed here!"


print(operation_type(operation))