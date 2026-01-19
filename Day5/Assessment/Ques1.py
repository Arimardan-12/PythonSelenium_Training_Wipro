"""		INHERITANCE
	1. Create a base class Vehicle with a method start()
	2. Create a derived class Car that inherits from Vehicle
	3. Add a class variable to track the number of vehicles created
	4. Demonstrate single inheritance and multilevel inheritance with appropriate classes			"""


# class vehicle with method start
class Vehicle:
    vehicle_count = 0
    def __init__(self):
        Vehicle.vehicle_count += 1
    # Method in base class
    def start(self):
        print("Vehicle is starting")


# Derived class (Single Inheritance)
class Car(Vehicle):
    def start(self):
        print("Car is starting")


# Derived class (Multilevel Inheritance)
class ElectricCar(Car):
    def start(self):
        print("Electric car is starting silently")


# Creating objects
v = Vehicle()
c = Car()
e = ElectricCar()

# Calling start methods
v.start()
c.start()
e.start()

# Display total number of vehicles created
print("Total vehicles created:", Vehicle.vehicle_count)
