# class Abc:
#     def __init__(self):
#         print("I am parent class constructor")
#     def xyz(self):
#         print("I am parent class method1")
#     def mnr(self):
#         print("I am parent class method2")
#
# class Pqr(Abc):
#     def __init__(self):
#         super().__init__()      # call parent class constructor
#         print("I am child class constructor")
#     def abc(self):
#         print("I am child class method1")
#     def xyz(self):               # method overriding
#         super().xyz()            # call parent class method
#         print("I am child class method2")
#
# a=Pqr()
# a.xyz()
# a.mnr()
# a.abc()



############################################################################

# class Abc:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#         print("x:",self.x)
#         print("y:",self.y)
#         print("I am parent class constructor")
#     def xyz(self):
#         print("I am parent class method1")
#     def mnr(self):
#         print("I am parent class method2")
#
# class Pqr(Abc):
#     def __init__(self,z):
#         self.z = z
#         print("z:",self.z)
#         super().__init__(10,20)      # call parent class constructor
#         print("I am child class constructor")
#     def abc(self):
#         print("I am child class method1")
#     def xyz(self):               # method overriding
#         super().xyz()            # call parent class method
#         print("I am child class method2")
#
# a=Pqr(30)
# a.xyz()
# a.mnr()
# a.abc()