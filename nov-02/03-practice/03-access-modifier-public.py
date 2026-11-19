class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


C = Customer("rupesh", 'rupesh@gmail.com')
print(C.name)
print(C.email)

C.email = "satyajit@gmail.com"
print(C.email)


