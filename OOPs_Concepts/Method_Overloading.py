
# Method Overloading not possible in python.
# Because python consider latest argument value.but there are alternative way.

# class Overloading:
#     def __init__(self):
#         pass
#
#     def m1(self):
#         print("method m1")
#
#     def m1(self,x):
#         print("method m2")
#
#     def m1(self,x,y):
#         print("method m3",x,y)
#
# obj = Overloading()
# # obj.m1()
# # obj.m1(10)
# obj.m1(20,30)


# Overcome method overloading Problem.(Using Variable Length).
# class Overloading:
#     def __init__(self):
#         pass
#
#     def m1(self,*x):
#         print("method m1",x)
#
# obj = Overloading()
# obj.m1()
# obj.m1(10)
# obj.m1(20,30)
# obj.m1("Pooja")


# Default Arguments
# class Overloading:
#     def __init__(self):
#         pass
#
#     def m1(self,a=10,b=20):
#         print("method m1",a+b)
#
# obj = Overloading()
# obj.m1()
# obj.m1(40)
# obj.m1(20,30)

