'''
@Agenda:    To learn closures in python

@Date:      04 november 2026
'''
'''
--> closures means function inside another function
--> 
'''

# 1
print("start of program")


def outer_function():
    print("\tOuter function entered")
    print("\tDefining inner function")
    def inner_function():
        print("\t\tEntered inner function")
        print("\t\tLeaving inner function")
    print("\tDone defining inner function")
    print("\tCalling inner function")
    inner_function()
    print("\tReturned from inner function")
    print("\tReturned from outer function")


print("Done defining outer function")
print("Calling outer function")
outer_function()
print("Returned from outer function")
print("End of program")

# 2
# Two level nesting 
def f1(n): 
    print(f'n:{n}')
    def f2(x, y): 
        print(f'x:{x}, y:{y}')
    z = 100 
    print(f'z:{z}')
    f2(True, False) 
f1(500)

# 3
# Three level nesting  
def f(): 
    m = 100 
    def g(): 
        n = 200 
        def h(): 
            k = 300 
            print(k) 
        h() 
        print(n) 
    g() 
    print(m)
f() 

# 4
# Module symbol table or global symbol table 

print('globals():', globals())  
print('-----------------------------------------------------------------------') 
gnum = 5000 

print('globals():after gnum = 5000', globals()) 
                                                
print('-----------------------------------------------------------------------')
import math 
import tkinter 

print('globals():after import math and import tkinter:', globals()) 

print('-----------------------------------------------------------------------')
def test_function(): 
    print("1:initial state of local symbol table:locals():", locals())  
    b1 = False 
    print("2:local symbol table after b1 = False:", locals())
    n = 300 
    print("3:local symbol table after n = 300:", locals())
    f = 3.4 
    print("4:local symbol table after f = 3.4:", locals()) 

test_function() 
print('-----------------------------------------------------------------------')


# 5
# Scopes
    # global
    # local
    # class
    # function

L = [10, 20, 30, 40, 50]     # global           
for x in L:                             
    print(x)                            

def my_func_1():         # global                
    D = {'a': 100, 'b': 200, 'c': 300}   # local
    for (key, value) in D.items():         
        if value > 100:                 
            print(key, value)           


def my_func_2():                                 
    L = [100, 200, 300, 400, 500, 600, 700]     
    M = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]     
    result = []                                 
    for p in L:                                 
        for q in M:                             
            T = (p, q):                         
            result.append(T)                    
    print(result)                               

my_func_1()     
my_func_2()      

class Date:      # global
    def __init__(self, init_day, init_month, init_year):    
        self.day = init_day         
        self.month = init_month     
        self.year = init_year        

    def getDay(self):               
        return self.day              

    def setDay(self, newDay):        
        self.day = newDay          


class Test:     # global scope 
    a = 10      
    b = 20      
    def my_method(self):    # local scope of class 
        m = 100     
        n = 200     


# 6
# scopes deep

print("Start of program")
print("This code demonstrates enclosing scope")
def f1():
    L = [10, 20, 30, 40]
    for x in L:
        print(x)
    def f2():
        D = {'p' : True, 'q': False}
        def f3():
            S = {100, 200, 300}
            for x in S:
                print(x**2)

            for x in S:
                if x > 100:
                    y = x + 400
                    z = y ** 2
                    print(z)

        f3()
        for (key, val) in D.items():
            print(key, val)
    f2()
    print(L)
f1()
print("End of program")


# 6
# LHS treatment of variables

m = 100

def f1():
    n = 200

    def f2():
        k = 300

    f2()
f1()


# 7
'''
A variable name can be defined only once in a given scope. 

If you change the scope the variable names created in other 
scopes can be recreated for the changed scope
'''
N = 100 
print('global symbol table:globals():', globals())
def f1(): 
    N = 200 
    print('local symbol table of f1():', locals())
    def f2(): 
        N = 300 
        print('local symbol table of f2():', locals())
        input('Enter any key to continue....')
    f2() 
f1() 


# 8
# LEGB Scope rule

# Code Snippet 1 

N = 100 
print('global():N:', N)
def f(): 
    N = 200 
    print('f():N:', N) 
f() 

#------------------------------------

# Code Snippet 2 

N = 100 
def f(): 
    print("f():N:", N)
f() 

#-------------------------------------

# Code Snippet 3 

N = 100 
def f1(): 
    N = 200 
    def f2(): 
        print("f2():N:", N) 
    f2() 
f1() 

#-----------------------------------------

# Code Snippet 4 

N = 100 
def f1(): 
    print("f1():N:", N)
    def f2(): 
        print("f2():N:", N)
        print(M)
    f2() 
f1() 

# 9
# UnboundLocalError Case 1 
n = 100 
def f(): 
    print(n) 
    n = 200 
f() 

#----------------------------------
# UnboundLocalError Case 2 
n = 100 
def f(): 
    n = n + 1
f()  
#-----------------------------------

# 10
# global statement

N = 100 
def f(): 
    N = 500     
f()


# 11
# BEFORE 

N = 100 
def outer(): 
    N = 200 
    def inner(): 
        print(N)    
    inner() 
outer() 


# AFTER 

N = 100 
def outer(): 
    N = 200 
    def inner(): 
        global N 
        print(N) 
        N = 500 
    inner() 
outer() 

# 12
# non local
def outer():
    N = 100
    def inner():
        N = 500
    inner()
outer()

# 
def outer(): 
    N = 500 
    def inner(): 
        nonlocal N 
        N = 1000 
    print('outer():N before call to inner():', N)
    inner() 
    print('outer():N after call to inner():', N)
outer()


# 13
# Returning function as if it were a data object

def outer(): 
   
    def inner(): 
        print('inner():Function entered')
        print('inner():Function leaving')
    
    print('outer():type(inner):', type(inner))
    print('outer():id(inner):', id(inner))

    return inner

X = outer() 
print('global():type(X):', type(X))
print('global():id(X):', id(X))

print('global():Putting call operator on global variable X')
X()
print('global():End of program')
