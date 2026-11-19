
class Date:
    def __new__(self):
        print("In __new__()")
        print('id(self) in __new__: ', id(self))
        print('type(self) in __new__: ', type(self))


    def __init__(self):
        print("In __init__()")
        print("id(self) in __init__: ", id(self))
        print("type(self) in __init__: ", type(self))


D = Date()

