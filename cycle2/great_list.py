list1=["hello","world","programming","python","datastructure"]
print(list1)
a=0
for i in list1:
    if len(i)>a:
        a=len(i)
print(a)