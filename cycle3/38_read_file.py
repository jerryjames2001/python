def read(fname):
    with open(fname) as f:
        c=f.readlines()
    print(c)
read("demo.txt")
