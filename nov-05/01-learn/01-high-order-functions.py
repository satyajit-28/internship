#  Passing a function as an argument:

def apply(func, x):
   return func(x)

def square(n):
   return n * n

print(apply(square, 5)) # Output: 25


# Returning a function:

def multiplier(n):
   return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(5)) # Output: 10
print(triple(5)) # Output: 15