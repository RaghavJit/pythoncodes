import random

def union(L):
    l=[]
    for i in L:
        if i not in l:
            l.append(i)
    return l  

def inter(L1,L2):
    l=[]
    for i in L1:
        if i in L2:
            l.append(i)
    return l

#m=[e5]
#c=[e1, e3, e7, e9]
#s=[e2, e4, e6, e8]

def pref(L):
    l=[]
    for i in m:
        if i in L:
            return e5
        
    for i in c:
        if i in L:
            l.append()
    return random.choice(l)

    for i in s:
        if i in L:
            l.append()
    return random.choice(l)

def minus(L,l):
    for i in l:
        if i in L:
            L.remove(i)
    return L
    
