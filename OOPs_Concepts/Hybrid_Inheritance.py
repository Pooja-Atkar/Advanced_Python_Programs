
# How to define public,private,protected variable
# Public variable = x
# Protected variable = _x
# Private variable = __x

# Hybrid inheritance

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
        print("Child class B")
    def m1(self):
        print("B class method 1")
class C(A):
    def __init__(self):
       print("C class constructor")
    def m1(self):
        print(C.mro())
        super(C, self).m1()       # call immediate parent class of C.
        print("C class method 1")

class D(B,C):
    def __init__(self):
       print("D class constructor")
    def m1(self):
        print(C.mro())
        super(D, self).m1()       # call immediate parent class of C.
        print("D class method 1")

obj1 = D()
obj1.m1()
obj1.m2()