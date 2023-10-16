a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))

if a>b and a>c:
    print(a," is the greatest")
elif b>c and b>a:
    print(b," is the greatest")
else:
    print(c," is the greatest")
