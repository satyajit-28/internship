# # eg 1
# def fun():
#     return 10
#     return 10
# ret1 = fun()
# ret2 = fun()


# # eg 2
# def fun():
#     x = 10
#     y = 20
#     yield x
#     yield y

# def run():
#     return 30

# gen = fun()
# norm = run()
# print(type(fun))
# print(type(run))
# print(type(gen))
# print(type(norm))


# # eg 3
# def fun():
#     x = 10
#     print(x)
#     x = x + 1
#     print(x)

# fun()
# fun()
# fun()


# # eg 4
# def fun():
#     print("start fun")
#     yield 10
#     yield 20
#     yield 30
#     print("End fun")
# gen = fun()
# for i in gen:
#     print(i)


# # eg 5
def fun():
    print("Start fun")
    yield 10
    yield 20
    yield 30
    print("End fun")
ret = fun()
print(next(ret))
print(next(ret))
print(next(ret))
print(next(ret))