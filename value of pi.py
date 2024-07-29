import math
import time
x=1/1
s=0
t1=time.time()
for x in range(1,10000000):
    s=s+(1/x**2)
    x=x+1
print(s)

inmd=s*6
pi=math.sqrt(inmd)
print(pi)
t2=time.time()

print("time",t2-t1)

input("CLOSE")
