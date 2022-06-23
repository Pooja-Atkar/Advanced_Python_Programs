
# Constructor overloading
# Constructor overloading not possible.
# Because python refer latest arguments.

# class Consruct:
#     def __init__(self):
#         print("No argument Constructor")
#     def __int__(self,x):
#         print("1 argument constructor")
#
#     def __init__(self,x,y):
#         print("2 argument constructor")
#
# obj = Consruct()
# obj = Consruct(10)
# obj = Consruct(20,30)

# Default Arguments
# class Consruct:
#
#     def __init__(self,x=10,y=20):
#         print(x + y)
#
# obj = Consruct()
# obj = Consruct(50)
# obj = Consruct(60,30)

# Another way to perform constructor overloading. (Using Variable Length).
# class Consruct:
#
#     def __init__(self,*x):
#         print(sum(x))
#
# obj = Consruct()
# obj = Consruct(50)
# obj = Consruct(60,30)