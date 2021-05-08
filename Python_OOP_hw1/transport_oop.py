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

    @abstractmethod
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
    weight = 2500
    all_transports = []
    material = "aluminum"
    braking_dist = 0

    def __init__(self, name):
        self.name = name
        self.speed = None
        self.manufactured_in = None
        self.all_transports.append(self.name)

    def __len__(self):
        return len(self.all_transports)

    @classmethod
    def braking_distances(cls):
        """This method describes braking distances"""
        print(f"Braking distance for this transport - {cls.braking_dist}m.")

    def manufacture_year(self, manufactured_in):
        """Displays manufacturing year of select transport"""
        self.manufactured_in = manufactured_in
        print(f"This transport manufactured in {manufactured_in} year.")

    def speed_this_transport(self, speed):
        """Displays speed of certain type of transport"""
        self.speed = speed
        print(f'Speed {self.name} is {self.speed}!')

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print(f"Weight {self.name} is {self.weight} kg.")

    @staticmethod
    def print_color(color):
        """Displays color of certain type of transport"""
        print(f"This type of transport has {color} color!")

    def print_material(self):
        """Displays material of certain type of transport"""
        print(f"Material {self.name} is {self.material}.")

    def move(self):
        """This method describes transport movement"""
        print(f"Transport {self.name} can move")

class Car(Transport, Engine):
    """Inherited from Transport,Engine and represents Car"""
    type_engine = "electric"
    braking_dist = 2

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
    def __gt__(self, other):
        return self.speed > other.speed

    def __lt__(self, other):
        return self.speed < other.speed

    def speed_this_transport(self, speed):
        """Displays speed of certain type of transport"""
        print("Plane is the fastest type of transport!")
        super().speed_this_transport(speed)

    def print_weight(self):
        """Displays weight of certain type of transport"""
        print(f"Weight {self.name} is {self.weight} kg")

class Motorcycle(Transport, Engine):
    """Inherited from Transport,Engine and represents Motorcycle"""


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

    def __init__(self, name, price):
        self._price = price
        super().__init__(name)

    def __mul__(self, other):
        """Converting dollars into the required currency"""
        print("Please, enter, exchange rate:")
        if isinstance(other, int):
            print("In your currency it cost - ", end=" ")
            print(self._price * other)
        else:
            print("Please, enter a exchange rate")

    def move(self):
        """This method describes transport movement"""
        super().move()

    @property
    def price(self):
        """This function displays price"""
        print(f"Catamaran {self.name} price is {self._price} $")

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, int):
            self._price = new_price
        else:
            print("Please, enter a valid price")

    @price.deleter
    def price(self):
        del self._price

if __name__ == "__main__":

    tesla = Car("Tesla", 5)
    tesla.print_benefits()
    tesla.engine_info(362)
    tesla.braking_distances()

    bmx = Bicycle("BMX")
    bmx.print_weight()

    boeing = Plane("Boeing")
    boeing.speed_this_transport(943)
    boeing.engine_info(735)
    boeing.manufacture_year(2020)

    atp = Plane("ATP")
    atp.speed_this_transport(496)
    print(atp.name, 'faster than', boeing.name, '-', atp > boeing)
    print(boeing.name, 'faster than', atp.name, '-', atp < boeing)

    yamaha = Motorcycle("Yamaha")
    yamaha.print_color("red")
    yamaha.manufacture_year(1990)

    riverday = Boat("Riverday")
    riverday.print_material()

    aurora = Catamaran("Aurora", 9000)
    aurora.move()
    aurora.price = 78.99
    # aurora * 28

    print(Transport.all_transports)
    print(f"Quantity of available transport - {len(atp)}")
