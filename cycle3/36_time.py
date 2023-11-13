class time:
    def __init__(self,a,b,c):
        self.h=a
        self.m=b
        self.s=c
    def __add__(self, x):
        sum_h=self.h + x.h
        sum_m=self.m + x.m
        sum_s=self.s + x.s
        if sum_s >= 60:
            sum_s-=60
            sum_m +1
        if sum_m >=60:
            sum_m-=60
            sum_h +1
        print("Sum time=",sum_h," : ",sum_m," : ",sum_s)

print("Time1:")
h1=int(input("Enter the hour"))
m1=int(input("Enter minutes"))
s1=int(input("Enter seconds"))
obj1=time(h1,m1,s1)

print("Time2:")
h2=int(input("Enter the hour"))
m2=int(input("Enter minutes"))
s2=int(input("Enter seconds"))
obj2=time(h2,m2,s2)
print("Sum of times are ==:")
obj1+obj2
