'''
@Author:    satyajit 

@Goal:      To implement a command line calculator with proper error handling

@Date:      03rd November 2026

'''
def read_number(check_value):
    while True:
        try:
            value = float(input(check_value))
        except ValueError:
            print("Please check type of values")
            continue
        return value


def operation_type(value1:float, value2:float, operation: str) -> float:

    if operation == "+":
        return f"The result is: {value1 + value2}"
    elif operation == "-":
        return f"The result is: {value1 - value2}"
    elif operation == "*":
        return f"The result is: {value1 * value2}"
    elif operation in ("/", "//", "%"):
        if value2 == 0:
            raise ZeroDivisionError("Denominator should not be 0...!")
        if operation == "/":
            return f"The result is: {value1 / value2}"
        elif operation == "//":
            return f"The result is: {value1 // value2}"
        return f"The result is: {value1 % value2}"
    elif operation == "**":
        if value1 == 0 and value2 < 0:
            raise ZeroDivisionError("0 cannot be raised to a negative power...!")
        elif value2 > 1000:
            raise OverflowError("Power is too much...!")
        return f"The result is: {value1 ** value2}"
    else:
        return "The current operation is not listed here!"


try:
    value1 = read_number("Enter first number: ")
    value2 = read_number("Enter second number: ")
    operation = input("Enter operation which you want to perform: ")
    print(operation_type(value1, value2, operation))
except ZeroDivisionError:
    print("Not applicable")
except OverflowError:
    print("Result is too large to calculate")
except ValueError as v:
    print(f"Error: {v}")
except (KeyboardInterrupt):
    print("\nCancelled by user")
    

   
# print(operation_type(operation))