# Hierarchical Inheritance

###############################################################

class A:
    def __init__(self):
        print("A class constructor")

    def m1(self):
        print("A class method 1")

    def m2(self):
        print("A class method 2")
class B(A):
    def __init__(self):
        print("B class constructor ")
    def m1(self):
        print("B class method 1")
class C(A):
    def __init__(self):
       print("C class constructor")
    def m1(self):
        super(C, self).m1()       # call immediate parent class of C.
        print("C class method 1")

obj1 = C()
obj2 = B()
obj1.m1()
obj1.m2()
obj2.m1()