import statistics
import math
import time
print("Value of pi=",math.pi)
epoc=time.time()
print("Seconds using epoc",epoc)
current=time.ctime(epoc)
print("Time==",current)
li=[1,2,3,4,2,3,5,6]
avg=statistics.mean(li)
print("Average=",avg)
