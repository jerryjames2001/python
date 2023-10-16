# Program :23
# Aim: Generate a list of four digit numbers in a given range with all their digits even and the
# number is a perfect square.
import math
x=int(input("Enter the starting limit"))
y=int(input("Enter the ending limit number"))
for i in range(x,y):
    if i % 2 == 0:
        sq=math.sqrt(i)
        if sq.is_integer():
            print(i,"==",sq)

# a=int(input("Enter the lower bound"))
# b=int(input("Enter the upper bound"))
# result_list = [num for num in range(a,b+1)
#                if all(int(digit) % 2 == 0 for digit in str(num))
#                and int(num**0.5)**2 == num]
# print(result_list)