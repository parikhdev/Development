'''Write this hierarchy:

Vehicle base class — __init__ takes brand and speed. Method describe() returns "Brand: X, Speed: Y km/h"
Car(Vehicle) — adds num_doors in __init__ using super(). Overrides describe() to include door count
ElectricCar(Car) — adds battery_range in __init__. Overrides describe() to include battery range

Then:

Create an ElectricCar object and print describe()
Prove with isinstance() that it's simultaneously an ElectricCar, a Car, and a Vehicle'''

class Vehicle:
    def __init__(self,brand, speed):
        self.brand = brand
        self.speed = speed
    def describe(self):
        return f"Brand is {self.brand} and Speed is {self.speed}km/h"

class Car(Vehicle):
    def __init__(self,brand, speed, num_doors):
        super().__init__(brand,speed)
        self.num = num_doors
    def describe(self):
        return f"Brand is {self.brand}, Speed is {self.speed}km/h and Number of doors are {self.num}"

class ElectricCar(Car):
    def __init__(self, brand, speed, num_doors, battery_range):
        super().__init__(brand, speed, num_doors)
        self.battery = battery_range
    def describe(self):
        return f"Brand is {self.brand}, Speed is {self.speed}km/h , Number of doors are {self.num} and Range of Battery is {self.battery}"
a1 = ElectricCar("Mahindra", 300, 6, 100)
print(a1.describe())

print(isinstance(a1,ElectricCar))
print(isinstance(a1, Car))
print(isinstance(a1, Vehicle))