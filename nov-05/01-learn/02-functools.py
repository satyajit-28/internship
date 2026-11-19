'''
is a library which provides high order function to use directly
'''
'''
Most used pieces
>> wraps:   fix decorators
            When you wrap a function, 
            the wrapper replaces its name and docstring. 
            wraps copies that metadata back.
'''
from functools import wraps

def log_calls(func):
    @wraps(func)                      # preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def greet(name):
    """Say hello."""
    return f"Hello, {name}"

print(greet.__name__)   # 'greet' (without @wraps it would be 'wrapper')


from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))   # 25
print(cube(2))     # 8