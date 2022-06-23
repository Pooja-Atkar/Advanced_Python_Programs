# Duck Typing in python.

class A:
    def __init__(self):
        pass
    def m1(self):
        print("A class method 1")
class B:
    def __init__(self):
        pass
    def m1(self):

        print("B class method 1")

def func(obj):
        obj.m1()

# If you want to access A class method then write following statements.
# a = A()
# func(a)

# If you want to access B class method then write following statements.
# b = B()
# func(b)

# Otherwise you want to access both class method at a time then used following statements.
# lst = [A(),B()]
# for x in lst:
#     func(x)

# Also you can write following statement to call A and B class method.

# for i in A(),B():
#     i.m1()

# Duck type check the object at runtime.
# if object of class A is created at runtime then execute A class method.
# if object of class B is created at runtime then execute B class method.
# if method name are different in both the classes then duck typing does not work.
# Method name of both the classes should be same.otherwise it's not work.
# Which instance is pass is decided at run time.
