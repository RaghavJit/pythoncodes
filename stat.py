import math

def avg(l):
    s=sum(l)
    a=s/len(l)
    return a

def StD(d):
    s=sum(d)
    a=s/len(d)
    v1=0
    for i in d:
        v1=v1+(a-i)**2
    return math.sqrt(v1/len(d))

def CofD(l):
    return StD(l)/a

def CoVa(l, l1):
    x=avg(l)
    y=avg(l1)
    s=0
    for i in range(len(l)):
        s=s+(l[i]-x)*(l1[i]-y)
    return s/len(l)
