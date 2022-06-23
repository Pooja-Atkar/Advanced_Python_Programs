
# calling parent class without using inheritance concept.

# class Parent:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("parent class method 1")
# class Child:
#     def __init__(self):
#         print("Child class constructor")
#     def m1(self):
#         print("child class method 1")
#
# obj = Parent()
# obj.m1()
# obj1 = Child()
# obj1.m1()

###################################################
# Access Parent class with the help of Child class

# class Parent:
#     def __init__(self):
#         print("Parent class constructor")
#
#     def m1(self):
#         print("parent class method 1")
#
# class Child:
#      def __init__(self):      # self.obj = Parent()------You can give any name rather than obj.---self.a = Parent()
#         self.obj = Parent()   # Access Parent class constructor with the help of Child class statement
#         print("Child class constructor")
#
#      def m1(self):
#         self.obj.m1()         # Access Parent class method with the help of Child class statement
#         print("child class method 1")
#
# No need to call parent class constructor or method with the help of below 2 statements.
# # obj = Parent()
# # obj.m1()
# This 2 statements are required.
# obj1 = Child()
# obj1.m1()


#####################################################

# In above code you can refer parent class constructor and method with the help of below statement.
# self.obj = Parent()------You can give any name rather than obj.---self.a = Parent()--refer constructor.
# self.obj.m1()         # Access Parent class method with the help of this statement
# In this code you can refer child class constructor and method.
# self.obj1 = Child()  # Access Child class constructor with the help of parent class statement
# self.obj1.m1()         # Access child class method with the help of parent class statement

#########################################################

# class Parent:
#     def __init__(self):
#                              # self.obj = Parent()------You can give any name rather than obj.---self.a = Parent()
#         self.obj1 = Child()  # Access child class constructor with the help of parent class statement
#         print("Parent class constructor")
#
#     def m1(self):
#         self.obj1.m1()         # Access child class method with the help of parent class statement
#         print("parent class method 1")
#
# class Child:
#      def __init__(self):
#         print("Child class constructor")
#
#      def m1(self):
#         print("child class method 1")
#
# This 2 statements are required.
# obj = Parent()
# obj.m1()
# No need to call child class constructor or method with the help of below 2 statements.
# # obj1 = Child()
# # obj1.m1()