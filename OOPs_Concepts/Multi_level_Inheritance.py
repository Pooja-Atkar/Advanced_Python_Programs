
# Multi level inheritance

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
        super(B, self).m1()
        print("B class method 1")
class C(B):
    def __init__(self):
       print("C class constructor")
    def m1(self):
        # super(B, self).m1()
        super(C, self).m1()       # call immediate parent class of C.
        print("C class method 1")

obj1 = C()
obj1.m1()
obj1.m2() 