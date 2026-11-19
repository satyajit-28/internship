class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} is silent."

class Dog(Animal):
    def speak(self):
        return f"{self.name} says: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says: Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name} says: Quack!"

animals = [Dog("Rupesh"), Cat("Pradyumna"), Duck("Ganesh")]

for animal in animals:
    print(animal.speak())


'''
class Payment:
    def pay(self, amount):
        raise NotImplementedError

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} via Card")

for method in (UPI(), Card()):
    method.pay(500)
'''