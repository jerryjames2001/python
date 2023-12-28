file=input("Enter file name with extension")
text=file.split(".")
print("file name is : ",text[0])
print("file extension is : ",text[-1])