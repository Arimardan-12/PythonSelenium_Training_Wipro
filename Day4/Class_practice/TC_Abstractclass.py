"""
from abc import ABC,abstractmethod

class shape(ABC):
    def display(self):
        print("normal method")
    @abstractmethod
    def area(self):
        pass


class reactangle(shape):
    def area(self):
        print("area method implemented")


r=reactangle()
r.area()
r.display()
"""

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def salary(self):
        pass

class Manager(Employee):
    def salary(self):
        print(self.name,"Salary is 50000")


m=Manager("Ravi")
m.salary()