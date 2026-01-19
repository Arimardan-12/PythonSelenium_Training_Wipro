"""Question –
1. Create a class Calculator that demonstrates method overriding
2. Create another class AdvancedCalculator that overrides a method from Calculator
3. Implement operator overloading by overloading the + operator to add two objects of a custom class
4. Demonstrate polymorphism using the same method name with different behaviors"""


     #a class Calculator that demonstrates method overriding & another Advcalculator class that overrides
class Calculator:
    def add(self, a, b):
        print("Calculator Add:", a + b)


# Derived class overriding a method from Calculator
class AdvancedCalculator(Calculator):
    def multiply(self, a, b):
        print("Advanced Calculator Add:", round(a+b))

calc = Calculator()
adv_calc = AdvancedCalculator()

calc.add(4, 2)
adv_calc.multiply(4, 2)


         #operator overloading by overloading the + operator to add two objects of a custom class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Create two Point objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Use the overloaded + operator
p3 = p1 + p2  # This calls p1.__add__(p2)

# Print the result
print(p3)  # This calls p3.__str__()



    #Demonstrate polymorphism using the same method name with different behaviors

class animal:
    def sound(self):
        print("animal sound")
class dog(animal):
    def sound(self):
        print("Dog Barks");

class cat(animal):
    def sound(self):
        print("cat meows")
obj=[dog(),cat()]

for a in obj:
    a.sound()


