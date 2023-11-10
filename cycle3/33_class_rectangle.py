class rectangle:
    def __init__(self,l,b):
        self.x=l
        self.y=b
    def area(self):
        self.a = self.x * self.y
    def perimeter(self):
        self.p=4 * (self.x + self.y)
    def disp(self):
        print("Area=",self.a," \tPerimeter=",self.p)
    def comp(self,obj2):
        if self.a > obj2.a:
            print("Area of Rectangle 1 is greater than rectangle 2");
        elif self.a == obj2.a:
            print("Area of Rectangle 1 is same of rectangle 2");
        else:
            print("Area of Rectangle 2 is greater than rectangle 1");

l1=int(input("Enter the length of rectangle 1"))
b1=int(input("Enter the breadth of rectangle 1"))

l2=int(input("Enter the length of rectangle 2"))
b2=int(input("Enter the breadth of rectangle 2"))

obj1=rectangle(l1,b1)
print("Rectangle 1:")
obj1.area()
obj1.perimeter()
obj1.disp()

print("Rectangle 2:")
obj2=rectangle(l2,b2)
obj2.area()
obj2.perimeter()
obj2.disp()

print("\nComparing area of rectangle \n")
obj1.comp(obj2);