try:
    print("In try block")
    s1 = input("Enter first value: ")
    s2 = input("Enter second value: ")
    a = int(s1)
    b = int(s2)
    c = a/b
except ZeroDivisionError:
    print("Dont enter zero for denominator")
except ValueError:
    print("Dont enter symbols and alpha numeric strs")
else:
    print("else block")
    print("val of a:", a)
    print("val of b: ", b)
    print("div: ", c)
finally:
    print("In finally block")