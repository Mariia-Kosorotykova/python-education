"""This module describes restaurant system.

Exercise: Create program that describes Restaurant with
food delivery. It should consists of 10 classes and follows
OOP principles (Inheritance and Encapsulation). Access
modifiers and static methods are required.
"""


class Restaurant:
    """Describe Restaurant and its status at certain moment"""
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.status_restaurant = True

    def show_status(self):
        """This method shows open/closed restaurant status"""
        print("Restaurant is open" if self.status_restaurant else
              "Restaurant is closed")

class Employee:
    """This is parent's class that describes Employee"""
    _id_counter = 1
    all_employee = {}

    def __init__(self, name, position):
        self._name = name
        self.position = position
        self.all_employee[self._id_counter] = name + "-" + position
        self.name_id = Employee._id_counter
        Employee._id_counter += 1

    def show_id_employee(self):
        """This method displays employee id"""
        print(f"{self._name} has {self.name_id}")

    def show_all_employee(self):
        """This method displays list of all employees"""
        print(self.all_employee)

    def show_salary(self):
        """Displays salary according to position"""
        if self.position == "hostess":
            print(f"Salary {self._name} is 200 $")
        elif self.position == "waiter":
            print(f"Salary {self._name} is 400 $")
        elif self.position == "cook":
            print(f"Salary {self._name} is 500 $")
        else:
            print(f"Salary {self._name} is 300 $")

class Hostess(Employee):
    """Inherited from Employee and represents Hostess"""
    def __init__(self, name, restaurant_obj):
        self.name = name
        super().__init__(name, position="Hostess")
        self.free_table = list(range(0, restaurant_obj.capacity + 1))

    def display_capacity(self):
        """Displays all available tables"""
        print(self.free_table)

    def book_tables(self, client_obj):
        """Books available table and reject unavailable"""
        if client_obj.selected_table in self.free_table:
            print("Good news, this table is free!")
            self.free_table.remove(client_obj.selected_table)
        else:
            print("Sorry, this table is booked. Please, choose another...")

    def restore_table(self, client_obj):
        """Makes table available after client leave"""
        self.free_table.append(client_obj.selected_table)

class Waiter(Employee):
    """Inherited from Employee and represents Waiter"""
    def __init__(self, name):
        self.name = name
        super().__init__(name, position="Waiter")

    @staticmethod
    def recieve_order(order_obj):
        """This method change order status to 'Order accepted'"""
        order_obj.status_order = "Order accepted"
        print(f"Status of your order is: '{order_obj.status_order}'")
        print("Order in progress...")

    @staticmethod
    def recieve_payment(order_obj):
        """This method change order status to 'Order closed'"""
        order_obj.status_order = "Order closed"
        print(f"Status of this order is: '{order_obj.status_order}'")

class ClientInside:
    """This class describes ClientInside"""
    _id_counter = 1

    def __init__(self, client_name, selected_table):
        self.__client_name = client_name
        self.selected_table = selected_table
        self.another_table = None
        self._id_client_inside = ClientInside._id_counter
        self.client_order = Order()
        ClientInside._id_counter += 1

    def change_table(self, another_table):
        """This method allowed change table to desired"""
        self.selected_table = another_table
        print(f"Now your desired table is {self.selected_table}.")

    @staticmethod
    def see_menu():
        """This method shows menu"""
        Menu.show_menu()

    def make_order(self, *args):
        """This method creates list with desired dishes"""
        self.client_order.status_order = "Formed"
        for i in args:
            self.client_order.order_list.append(i)
        print(f"Your order consists of: {self.client_order.order_list}")
        print(f"Status of your order is: '{self.client_order.status_order}'")

    def receive_payment(self):
        """This method change order status to 'Order paid'"""
        self.client_order.status_order = "Order paid"
        print(f"Status of this order is: '{self.client_order.status_order}'")

class Chief(Employee):
    """Inherited from Employee and represents Chief"""
    def __init__(self, name):
        self.name = name
        super().__init__(name, position="Chief")

    @staticmethod
    def cook_order(order_obj):
        """This method change order status to 'Ready'"""
        order_obj.status_order = "Ready"
        print(f"Status of your order is: '{order_obj.status_order}'")

class Administrator(Employee):
    """Inherited from Employee and represents Administrator"""
    def __init__(self, name):
        self.name = name
        super().__init__(name, position="Administrator")

    @staticmethod
    def close_restaurant(restaurant_obj):
        """Change restaurant status to False(closed)"""
        if not restaurant_obj.status_restaurant:
            print("Restaurant is AlREADY closed")
        else:
            restaurant_obj.status_restaurant = False
            print("This restaurant is closed")

    @staticmethod
    def open_restaurant(restaurant_obj):
        """Change restaurant status to True(opened)"""
        if restaurant_obj.status_restaurant:
            print("Restaurant is AlREADY opened")
        else:
            restaurant_obj.status_restaurant = True
            print("This restaurant is opened")

class Menu:
    """This class describes Restaurant Menu"""
    list_dishes = {
        "Pizza": 100,
        "Soup": 50,
        "Pasta": 80,
        "Rolls": 120,
        "Borscht": 50,
        "Cake": 60,
        "Salad": 70
    }

    @staticmethod
    def show_menu():
        """This method displays restaurant menu"""
        for i, j in Menu.list_dishes.items():
            print(f" ~ Dish '{i}' costs {j} $")

class ClientOutside:
    """This class describes ClientOutside"""
    _id_counter = 1

    def __init__(self, client_name, telephone, address):
        self.__client_name = client_name
        self._telephone = telephone
        self._address = address
        self.name_id = ClientOutside._id_counter
        self.client_order = Order()
        ClientOutside._id_counter += 1

    def make_order(self, *args):
        """This method creates list with desired dishes"""
        self.client_order.status_order = "Formed"
        for i in args:
            self.client_order.order_list.append(i)
        print(f"Your order consists of: {self.client_order.order_list}")
        print(f"Status of your order is: '{self.client_order.status_order}'")

    def receive_payment(self):
        """This method change order status to 'Order paid'"""
        self.client_order.status_order = "Order paid"
        print(f"Status of this order is: '{self.client_order.status_order}'")

class Courier(Employee):
    """Inherited from Employee and represents Courier"""

    def __init__(self, name):
        self.name = name
        super().__init__(name, position="Courier")

    @staticmethod
    def receive_order(order_obj):
        """This method change order status to 'Order accepted'"""
        order_obj.status_order = "Order accepted"
        print(f"Status of your order is: '{order_obj.status_order}'")
        print("Order in progress...")

    @staticmethod
    def receive_payment(order_obj):
        """This method change order status to 'Order closed'"""
        order_obj.status_order = "Order closed"
        print(f"Status of this order is: '{order_obj.status_order}'")

class Order:
    """This class describes Order"""
    _id_counter = 1

    def __init__(self):
        self.status_order = None
        self._name_id_order = Order._id_counter
        Order._id_counter += 1
        self.order_list = []

    @staticmethod
    def total_price(client_obj):
        """This method calculates the order amount"""
        order_amount = 0
        for i in client_obj.client_order.order_list:
            order_amount += Menu.list_dishes.get(i)
        print(f"sum your order - {order_amount} $")

if __name__ == '__main__':
    sveta = Employee("Sveta", "hostess")
    sveta.show_salary()
    vasia = Employee("Vasia", "cook")
    vasia.show_salary()
    dima = Employee("Dima", "courier")
    dima.show_salary()
    vasia.show_all_employee()

    mafia = Restaurant("Mafia", 30)
    mafia.show_status()

    liza = Administrator("Liza")
    liza.close_restaurant(mafia)
    liza.close_restaurant(mafia)
    mafia.show_status()
    liza.show_all_employee()

    k = Menu()
    k.show_menu()

    kate = ClientInside('Kate', 7)
    mari = Hostess("Mari", mafia)
    mari.book_tables(kate)
    vlad = ClientInside("Vlad", 7)
    mari.book_tables(vlad)
    vlad.change_table(8)
    mari.book_tables(vlad)
    vlad.see_menu()
    vlad.make_order("Pizza", "Cake")
