class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__pin = 1234


Acc = Account('rupesh', 1000)
# print(Acc.__pin)

# OBJ._class_name__private_variable_name
print(Acc._Account__pin)