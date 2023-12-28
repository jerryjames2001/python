c = int(input("enter current year\t"))
f = int(input("enter future year\t"))
for i in range(c,f):
    if (i%4==0) and (i%100!=0):
        print("Leap years are -",i)