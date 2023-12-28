a = open("./cycle3/demo.txt", "r")
b = open("cycle3/t", "w")
c = a.readlines()
d = len(c)
for i in range(0, d):
 if i % 2 == 0:
     b.write(c[i])
 else:
     pass
b.close()
b = open("cycle3/t", "r")
e = b.read()
print(e)
a.close()
b.close()