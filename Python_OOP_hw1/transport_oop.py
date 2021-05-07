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

from abc import ABC, abstractmethod

class Engine(ABC):
    """This is parent's class that describes Engine"""
    type_engine = "petrol"

    def __init__(self):
        self.engine_power = None
        self.manufactured_in = None

    @abstractmethod
    def manufacture_year(self, manufactured_in):
        """Displays manufacturing year of select engine"""
        self.manufactured_in = manufactured_in
        print(f"This engine manufactured in {manufactured_in} year.")

    def engine_info(self, engine_power):
        """Provides info about engine"""
        self.engine_power = engine_power
        print(f"This transport has {self.type_engine} type of engine"
              f" and power - {self.engine_power}.")

class Transport:
    """This is parent's class that describes Transport"""
    color = "gray"
    weight = 2500
    all_transports = []
    material = "aluminum"

    def __init__(self, name):
        self.name = name
        self.speed = None
        self.manufactured_in = None
        self.all_transports.append(self.name)

    def manufacture_year(self, manufactured_in):
        """Displays manufacturing year of select transport"""
        self.manufactured_in = manufactured_in
        print(f"This transport manufactured in {manufactured_in} year.")

    def speed_this_car(self, speed):
        """Displays speed of certain type of transport"""
        self.speed = speed
        print(f'Speed {self.name} is {self.speed}!')

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print(f"Weight {self.name} is {self.weight} kg.")

    def print_color(self):
        """Displays color of certain type of transport"""
        print(f"Color {self.name} is {self.weight}.")

    def print_material(self):
        """Displays material of certain type of transport"""
        print(f"Material {self.name} is {self.material}.")

    def move(self):
        """This method describes transport movement"""
        print(f"Transport {self.name} can move")

class Car(Transport, Engine):
    """Inherited from Transport,Engine and represents Car"""
    type_engine = "electric"

    def __init__(self, name, fuel_price):
        self.fuel_price = fuel_price
        super().__init__(name)

    def print_benefits(self):
        """Displays benefits of certain type of transport"""
        print(f'Benefits {self.name} is cheap fuel {self.fuel_price}$')

class Bicycle(Transport):
    """This class is inherited from Transport and represents Bicycle"""
    weight = 4

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print("Bicycle is the lightest weight transport!")
        print(f"Weight {self.name} is {self.weight} kg")

    def move(self):
        """This method describes transport movement"""
        print(f"Transport {self.name} moves by land")
        super().move()

class Plane(Transport, Engine):
    """Inherited from Transport,Engine and represents Plane"""

    def speed_this_car(self, speed):
        """Displays speed of certain type of transport"""
        print("Plane is the fastest type of transport!")
        super().speed_this_car(speed)

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print(f"Weight {self.name} is {self.weight} kg")

class Motorcycle(Transport, Engine):
    """Inherited from Transport,Engine and represents Motorcycle"""
    color = "red"

    def print_color(self):
        """Displays color of certain type of transport"""
        print("Motorcycle is the brightest transport!")
        print(f"Color {self.name} is {self.color}.")

    def manufacture_year(self, manufactured_in):
        """Displays manufacturing year of select engine"""
        Engine.manufacture_year(self, manufactured_in)

class Boat(Transport):
    """This class is inherited from Transport and represents Boat"""
    material = "plastic"

    def print_material(self):
        """Displays material of certain type of transport"""
        print(f"{self.material} boats are very popular.")
        super().print_material()

    def move(self):
        """This method describes transport movement"""
        print(f"This transport {self.name} moves on water")
        super().move()


class Catamaran(Bicycle, Boat):
    """Inherited from Bicycle, Boat and represents Catamaran"""

    def move(self):
        """This method describes transport movement"""
        super(Boat, self).move()


if __name__ == "__main__":
    toyota = Transport("toyota")
    toyota.speed_this_car(230)
    toyota.print_weight()

    tesla = Car("Tesla", 5)
    tesla.print_benefits()
    tesla.engine_info(362)

    bmx = Bicycle("BMX")
    bmx.print_weight()

    boeing = Plane("Boeing")
    boeing.speed_this_car(943)
    boeing.engine_info(735)
    boeing.manufacture_year(2020)

    yamaha = Motorcycle("Yamaha")
    yamaha.print_color()
    yamaha.manufacture_year(1990)

    riverday = Boat("Riverday")
    riverday.print_material()

    aurora = Catamaran("Aurora")
    aurora.move()

    print(Transport.all_transports)
