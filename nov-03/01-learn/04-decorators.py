# # First example
# def fun():
#     return "Hello"
# ret = fun()
# print(ret)  


# # second example
# def outer():
#     print("In outer")
#     def inner():
#         print("In inner")
#     inner()
# outer()


# # Third example
# def outer():
#     print("In outer")
#     def inner():
#         print("In inner")
#     return inner

# retfun = outer()
# retfun()


# # Fouth example
# def outerfunc():
#     print("In outer function")
#     def innerfunc1():
#         print("In innerfunc1 function")
#     def innerfunc2():
#         print("In innerfunc2 function")
#     innerfunc1()
#     innerfunc2()
# outerfunc()

# # Fifth example
# def run():
#     print("In run")
# def fun(x):
#     print("In fun")
# fun(run)


# # Sixth example
# def run():
#     print("In run")
# def fun(x):
#     print("In fun")
#     x()
# fun(run)


# # Seventh example
# def gun():
#     print("In gun")
# def run(y):
#     print("In run")
#     y()
# def fun(x):
#     print("In fun")
#     x()
# fun(run(gun))


# # Eighth example
# def decorfun(func):
#     def wrapper():
#         print("Start wrapper")
#         func()
#         print("End wrapper")
#     return wrapper

# def normalfun():
#     print("Hello in normal fun")

# ret = decorfun(normalfun)
# ret()

# # Nonth example
# def decorfun(func):
#     def wrapper():
#         print("Start wrapper")
#         func()
#         print("End wrapper")
#     return wrapper

# @decorfun
# def normalfun():
#     print("Hello in normal fun")

# # normalfun = decorfun(normalfun)
# normalfun()


