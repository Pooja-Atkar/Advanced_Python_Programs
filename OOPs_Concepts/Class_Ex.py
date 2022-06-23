
class first:

    # empty constructor
    def __init__(self):
        pass

    # without argument method
    def method1(self):
        print("It's a first class")

    # with argument method
    def method2(self,x):
        self.x = x
        print("x =",x)

    # with argument method
    def method3(self, p,q,r):
        self.p = p
        self.q = q
        self.r = r
        print("p =", p,"q =",q,"r =",r)

obj = first()
obj.method1()
obj.method2(10)
obj.method3(7,8,9)

