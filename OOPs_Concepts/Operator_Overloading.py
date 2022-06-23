
# Operator Overloading
class Poly:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        print(self.x + self.y)

        str1 = input("Enter 1st String:")
        str2 = input("Enter 2nd String:")
        print(str1 + str2)

obj=Poly(10,20)
