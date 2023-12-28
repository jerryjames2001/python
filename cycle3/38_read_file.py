def read(fname):
    with open(fname) as f:
        c=f.readlines()
    print(c)
read("./cycle3/demo.txt")