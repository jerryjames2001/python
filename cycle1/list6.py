list1=[10,20,30,40,50,60]
list2=[5,10,25,30,40,55]
print("list1 : ",list1)
print("list2 : ",list2)

print("length of list1 = ",len(list1))
print("length of list2 = ",len(list2))
if len(list1) == len(list2):
    print("Lists have same length")
else:
    print("List is of different length")

print("Sum of list1 = ",sum(list1))
print("Sum of list2 = ",sum(list2))
if sum(list1) == sum(list2):
    print("Sum of the lists are same")
else:
    print("Sum of the lists are not same")

check=any(item in list1 for item in list2)
print("Any value occured in both : ",check)