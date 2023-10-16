list1="Web programming"
newlist=[i for i in list1.casefold()]
dictt={}.fromkeys(newlist, 0)
for i in list1.casefold():
    if i in dictt:
        dictt[i]=dictt[i]+1
print(list1)
print(dictt)