class Demo:
    # def __new__(self):
    #     print("In __new__")


    def __init__(self, day, month, year):
        print(self.__dict__)
        self.day = day
        self.month = month
        self.year = year
        print(self.__dict__)
        print("In __init__")


D = Demo(3, 11, 2026)
