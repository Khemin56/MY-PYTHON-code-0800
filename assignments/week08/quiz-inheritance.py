""" 
Create a class hierarchy:

    Base class Vehicle with attributes: brand, model, year
    Derived class Car with additional attribute: number_of_doors
    Implement a method get_info() in both classes

"""
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_info(self):
            return f"Brand: {self.brand},Model:{self.model},Year:{self.year}"
    
class Car(Vehicle):
    def __init__(self, brand, model, year,number_of_doors):
super().__inif__(brand, model, year)
self.number_of_doors = number_of_doors

def get_info(self):
     return f"Brand: {self.brand},Model:{self.model},Year:{self.year},Number of doors:{self.number_of_doors}"
vehicle = Vehicle("Toyota","Yaris","2025")
print(vehicle.get_info())
class Car(Vehicle):
     def get_info(self):
          return f"Brand: {self.brand},Model:{self.model},Year:{self.year},Number of doors:{self.number_of_doors}"
     vehicle = Vehicle("Toyota","Yaris","2025")
     print(vehicle.get_info())
     car = Car("Toyota","Yaris","2025","5")
     print(car.get_info())