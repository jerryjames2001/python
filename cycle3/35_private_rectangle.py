class rect:
    def __init__(self,a,b):
        self.l=a
        self.b=b
    def area(self):
        area1=self.l*self.b
        return area1
    def __lt__(self,obj):
        if(self.area() < obj.area()):
            return "Rectancgle 1 less than Rectangle 2"
        else:
            return "Rectancgle 2 less than Rectangle 1"
print("Enter rectangle 1 values")
x=int(input("Enter length: "))
y=int(input("Enter breadth: "))
obj1=rect(x,y)
print("area is:")
print(obj1.area())

print("Enter rectangle 2 values")
x=int(input("Enter length: "))
y=int(input("Enter breadth: "))
obj2=rect(x,y)
print("area is:")
print(obj2.area())
print(obj1<obj2)
