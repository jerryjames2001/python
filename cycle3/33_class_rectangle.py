class rectangle:
    def __init__(self,l,b):
        self.x=l
        self.y=b
    def area(self):
        self.a = self.x * self.y
    def perimeter(self):
        self.p=4 * (self.x + self.y)
    def disp(self):
        print("Area=", self.a)
        print("Perimeter=", self.p)

l1=int(input("Enter the length of rectangle 1"))
b1=int(input("Enter the breadth of rectangle 1"))

l2=int(input("Enter the length of rectangle 2"))
b2=int(input("Enter the breadth of rectangle 2"))

obj1=rectangle(l1,b1)
obj2=rectangle(l2,b2)
obj1.disp()
obj2.disp()