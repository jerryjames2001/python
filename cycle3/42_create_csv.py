import csv
fields=['id','name','gender']
data=[{'id':'1','name':'jerry','gender':'male'},
      {'id':'2','name':'jerin','gender':'male'},
      {'id':'3','name':'jeril','gender':'male'},
      {'id':'4','name':'jaison','gender':'male'},
      {'id':'5','name':'jacob','gender':'male'},
      {'id':'6','name':'indulekha','gender':'female'},
      ]
with open("cycle3/42_create.csv",'w')as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=fields)
    write.writeheader()
    write.writerows(data)
with open("cycle3/42_create.csv",newline="")as csvfile:
    d=csv.reader(csvfile,delimiter=',',quotechar='"')
    for i in d:
        print("-".join(i))