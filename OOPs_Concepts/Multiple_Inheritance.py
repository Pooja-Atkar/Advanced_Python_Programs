
# Multiple inheritance
# MRO-- Method Resolution Order
# Diamond Shape Problem solve by MRO.
# class C(A,B):
# [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# class C(B,A):
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

###############################################################

class A:
    def __init__(self):
        print("A class constructor")

    def m1(self):
        print("A class method 1")

    def m2(self):
        print("A class method 2")
class B:
    def __init__(self):
        print("Child class B")
    def m1(self):
        print("B class method 1")
class C(B,A):
    def __init__(self):
       print("C class constructor")
    def m1(self):
        print(C.mro())
        super(C, self).m1()       # call immediate parent class of C.
        print("C class method 1")

obj1 = C()
obj1.m1()
obj1.m2()