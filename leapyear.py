c = int(input("enter current year"))
f = int(input("enter future year"))
for i in range(c,f):
    if (i%4==0) and (i%100!=0):
        print(i)