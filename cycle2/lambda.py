# Write lambda functions to find area of square, rectangle and triangle.
l=int(input("Enter the length for rectangle"))
b=int(input("Enter the breadth for rectangle"))
c=lambda l,b : l*b
print("Area of rectangle="+str(c(l,b)))

s=int(input("Enter the side of square"))
c=lambda x : x*x
print("Area of square=",str(c(s)))

base=int(input("Enter th base of triangle"))
h=int(input("Enter the height of triangle"))
c=lambda b,h :0.5*b*h
print("Area of triangle="+str(c(base,h)))
