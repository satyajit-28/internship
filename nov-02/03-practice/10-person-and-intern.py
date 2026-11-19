"""
Inheritance — Person and intern
Question: Create an Intern class that inherits from a Person class.
Requirements:
Person stores name and age.
Person.introduce() prints the name and age.
Intern adds a technology attribute.
Use super().__init__() to initialize the inherited attributes.
Intern.show_training() prints the technology being learned.
"""

'''
@Date:  02 november 2026

@Aim:   To implement inheritance
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def introduce(self):
        print(f"Person Name: {self.name}")
        print(f"Person Age: {self.age}")


class Intern(Person):
    def __init__(self, name:str, age:int, technology:str):
        if type(name) != str or type(age) != int or type(technology) != str:
            raise TypeError("check your data once!")
        print(self.__dict__)
        super().__init__(name, age)
        self.technology = technology
        print(self.__dict__)


    def show_training(self):
        print(self.technology)

I = Intern(3, 90, "Python")
# I = Intern("Rupesh", "Omkar", "python")
# I = Intern("Rupesh", 100, 100)
# I = Intern(10, 90, "Python")
I.introduce()
I.show_training()







        
              
