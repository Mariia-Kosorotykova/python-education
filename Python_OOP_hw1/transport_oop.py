"""This module provides general description of Transport.

Exercise: - Practice in creating classes from zero and inheritance
from another classes
- Create class Transport, think about attributes and methods,
supplement the class with them
- Think and implement the class - inherited class Transport (min 4),
redefine methods and attributes for each class
- (Additional task) implement multiple inheritance, create one more
parent class, for example Engine
"""


class Transport:
    """This is parent's class that describes Transport"""
    color = "gray"
    weight = 2500
    all_transports = []

    def __init__(self, name):
        self.name = name
        self.speed = None
        self.all_transports.append(self.name)

    def speed_this_car(self, speed):
        """Displays speed of certain type of transport"""
        self.speed = speed
        print(f'Speed {self.name} is {self.speed}')

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print(f"Weight {self.name} is {self.weight} kg")

    def print_color(self):
        """Displays color of certain type of transport"""
        print(f"Color {self.name} is {self.weight}")

class Car(Transport):
    """This class is inherited from Transport and represents Car"""

    def __init__(self, name, fuel_price):
        self.fuel_price = fuel_price
        super().__init__(name)

    def print_benefits(self):
        """Displays benefits of certain type of transport"""
        # print(f'Benefits {self.name} is manufactured in {self.creation_year}')
        print(f'Benefits {self.name} is cheap fuel {self.fuel_price}$')

class Bicycle(Transport):
    """This class is inherited from Transport and represents Car"""
    weight = 4

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print("Bicycle is the lightest weight transport!")
        print(f"Weight {self.name} is {self.weight} kg")

    @staticmethod
    def engine_available():
        """Shows if there is an engine"""
        print("Bicycle hasn't engine")

class Plane(Transport):
    """This class is inherited from Transport and represents Car"""

    def speed_this_car(self, speed):
        """Displays speed of certain type of transport"""
        print("Plane is the fastest type of transport!")
        super().speed_this_car(speed)

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print(f"Weight {self.name} is {self.weight} kg")

class Motorcycle(Transport):
    """This class is inherited from Transport and represents Car"""
    color = "red"

    def print_color(self):
        """Displays color of certain type of transport"""
        print("Motorcycle is the brightest transport!")
        print(f"Color {self.name} is {self.weight}")

    @staticmethod
    def engine_available():
        """Shows if there is an engine"""
        print("Motorcycle has an engine")

class Engine(Bicycle, Motorcycle):
    """This class is inherited from Bicycle, Motorcycle and represents Engine"""

    @staticmethod
    def engine_available():
        """Shows if there is an engine"""
        Motorcycle.engine_available()

if __name__ == "__main__":
    toyota = Transport("toyota")
    toyota.speed_this_car(250)
    toyota.print_weight()

    tesla = Car("Tesla", 5)
    tesla.print_benefits()

    bmx = Bicycle("BMX")
    bmx.print_weight()

    boeing = Plane("Boeing")
    boeing.speed_this_car(700)
    print(Transport.all_transports)

    engine = Engine("motorbike")
    engine.engine_available()
