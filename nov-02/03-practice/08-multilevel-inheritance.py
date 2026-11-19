class Vehicle:
    def move(self):
        print("Moving")


class Car(Vehicle):
    def fuel(self):
        print("Petrol")


class ElecricCar(Car):
    def charge(self):
        print("Charging")


E = ElecricCar()
E.move()
E.fuel()
E.charge()
