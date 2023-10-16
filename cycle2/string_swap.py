a=input("Enter string 1: ")
b=input("Enter string 2: ")
#print(a.replace(a[0],b[0])," ",b.replace(b[0],a[0]))      mistake in seniours
sum = b[0]+a[1:]+" "+a[0]+b[1:]
print(sum)