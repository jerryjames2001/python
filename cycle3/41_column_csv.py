# This code is reading data from a CSV file named "python.csv" and printing the contents in a
# formatted manner.
import csv
with open("cycle3/python.csv",newline='')as csvfile:
    d=csv.reader(csvfile,delimiter=",",quotechar='"')
    # next(d)
    print("Name  -- Email")
    print("------++-------")
    for i in d:
        print(i[0],"\t",i[1])