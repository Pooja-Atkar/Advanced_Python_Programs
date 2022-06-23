
# Inheritance Example
# Method Overriding

class Parent:
    def __init__(self):
        pass
    def m1(self):
        print("I am parent class")

class Child(Parent):
    def m1(self):
        super().m1()                 # To refer parent class method.
        print("I am child class")


obj = Child()
obj.m1()
