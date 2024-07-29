import time
import math
t1=time.time()
x=1
s=0
for x in range(10000000,9000000):
    s=s+(1/x**2)
    x=x+1
#print("DONE",s)

x1=1
s1=0
for x1 in range(8000000,9000000):
    s1=s1+(1/x1**2)
    x1=x1+1
#print("DONE",s1)

x2=1
s2=0
for x2 in range(7000000,8000000):
    s2=s2+(1/x2**2)
    x2=x2+1
#print("DONE",s2)

x3=1
s3=0
for x3 in range(6000000,7000000):
    s3=s3+(1/x3**2)
    x3=x3+1
#print("DONE",s3)

x4=1
s4=0
for x4 in range(5000000,6000000):
    s4=s4+(1/x4**2)
    x4=x4+1
#print("DONE",s4)

x5=1
s5=0
for x5 in range(4000000,5000000):
    s5=s5+(1/x5**2)
    x5=x5+1
#print("DONE",s5)

x6=1
s6=0
for x6 in range(3000000,4000000):
    s6=s6+(1/x6**2)
    x6=x1+1
#print("DONE",s6)

x7=1
s7=0
for x7 in range(2000000,3000000):
    s7=s7+(1/x7**2)
    x7=x7+1
#print("DONE",s7)

x8=1
s8=0
for x8 in range(1000000,2000000):
    s8=s8+(1/x8**2)
    x8=x8+1
#print("DONE",s8)

x9=1
s9=0
for x9 in range(1,1000000):
    s9=s9+(1/x9**2)
    x9=x9+1
#print("DONE",s9)


print(s+s1+s2+s3+s4+s5+s6+s7+s8+s9)
t2=time.time()
y=6*(s+s1+s2+s3+s4+s5+s6+s7+s8+s9)
pi=math.sqrt(y)
print("time",t2-t1)
print(pi)
input("CLOSE")
