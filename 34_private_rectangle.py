class rect:
    def __init__(self,a,b):
        self.l=a
        self.b=b
        self.area_val=None
    def area(self):
        self.area=self.l*self.b
        print("area= ",self.area)
        return self.area
    def __lt__(self,obj):
        if self.area() < obj.area_val():
            print("Rectancgle 1 less than Rectangle 2")
        else:
            print("Rectancgle 2 less than Rectangle 1")
print("Enter rectangle 1 values")
x=int(input("Enter length: "))
y=int(input("Enter breadth: "))
obj1=rect(x,y)
area1=obj1.area()

print("Enter rectangle 2 values")
x=int(input("Enter length: "))
y=int(input("Enter breadth: "))
obj2=rect(x,y)
area2=obj2.area()
obj1 < obj2