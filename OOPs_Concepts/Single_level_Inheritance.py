
# Single level inheritance

class Parent:
    def __init__(self):
        print("Parent class constructor")

    def m(self):
        print("parent class method 1")
class Child(Parent):
    def __init__(self):

        print("Child class constructor")
    def m1(self):

        print("child class method 1")

obj1 = Child()
obj1.m1()
obj1.m()