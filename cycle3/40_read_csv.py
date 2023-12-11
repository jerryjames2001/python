# This code is reading a CSV file named "python.csv" and printing its contents.
import csv
with open("cycle3\python.csv",newline='')as csvfile:
    d=csv.reader(csvfile,delimiter=' ',quotechar='"')
    for i in d:
        print(','.join(i))