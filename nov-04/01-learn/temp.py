
# N = 100
# def f(): 
#     N = 200
#     def g(): 
#         N = 300

#         print('N:', N) 
#         # print(N)
#     g() 
# f() 



N = 100 
def outer(): 
    N = 200 
    def inner(): 
        global N 
        print(N) 
        N = 500 
    inner() 
outer() 