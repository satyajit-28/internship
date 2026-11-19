'''
@Author:    satyajit 

@Goal:      To implement a unit converter

@Date:      29th Oct 2026

'''


def unit_converter():
    print("-" * 50)
    print("===== UNIT CONVERTER USING PYTHON =====")
    print("-" * 50)
    print("1. Length (meters to kilometers)")
    print("2. Length (kilometers to meters)")
    print("3. Weight (kilograms to grams)")
    print("4. Weight (grams to kilograms)")
    print("5. Temperature (Celsius to Fahrenheit)")
    print("6. Temperature (Fahrenheit to Celsius)")
    print(">" * 50)
    print(">" * 50)


unit_converter()


choice = int(input("Enter conversion you want to do from list [1 to 6]: "))
value = float(input("Enter the value for conversion: "))


def meters_to_kilometers(value:float) -> float:
    result = value / 1000
    return f"{value} meters to {result} kilometers"


def kilometers_to_meters(value:float) -> float:
    result = value * 1000
    return f"{value} Kilometers to {result} meters"


def grams_to_kilograms(value:float) -> float:
    result = value * 1000
    return f"{value} grams to {result} kilograms"

    
def Celsius_to_Fahrenheit(value:float) -> float:
    result = (value * 9 / 5) + 32
    return f"{value} celsius to {result} fahrenheit"


def Fahrenheit_to_Celsius(value:float) -> float: 
    result = (value - 32) * 5 / 9
    return f"{value} fahrenheit to {result} celsius"


if choice == 1:
    print(meters_to_kilometers(value))
elif choice == 2:
    print(kilometers_to_meters(value))
elif choice == 3:
    print(grams_to_kilograms(value))
elif choice == 4:
    print(Celsius_to_Fahrenheit(value))
elif choice == 5:
    print(Fahrenheit_to_Celsius(value))
else:
    print("Your choice is not listed here!!!")


"""
required:>

class madhe lihine
loops want again and again 
use decorators
"""
