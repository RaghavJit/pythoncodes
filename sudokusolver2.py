import numpy as np
import matx81

# Data and variables
dl=[1,2,3,4,5,6,7,8,9]
mx = matx81.mx
D = {1:[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        ,2:[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
        ,3:[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]
        ,4:[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]
        ,5:[(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]
        ,6:[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]
        ,7:[(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]
        ,8:[(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]
        ,9:[(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]}

# Functions
def check():
    l = []
    for i in range(0,9):
        l.extend(mx[i])

    for i in l:
        if np.isnan(i) == True:
            return True

def clean(L):
    l = []
    for i in L:
        if not np.isnan(i):
            l.append(i)
    return l

def unique(l):
    L = []
    for i in dl:
        for j in l:
            if i in j:
                L.append(j)
        if len(L) == 1:
            return i, L[0]
        else:
            L = []        
            
def union(L):
    l = []
    for i in L:
        if i not in l:
            l.append(i)
    return l  

def inter(L1,L2):
    l = []
    for i in L1:
        if i in L2:
            l.append(i)
    return l

def minus(L,l):
    for i in l:
        if i in L:
            L.remove(i)
    return L

def box(a, b):
    if a in [0,1,2]:
        ax = [1,4,7]
    elif a in [3,4,5]:
        ax = [2,5,8]
    elif a in [3,6,9]:
        ax = [3,6,9]

    if b in [0,1,2]:
        bx = [1,2,3]
    elif b in [4,5,6]:
        bx = [2,5,8]
    elif b in [3,6,9]:
        bx = [7,8,9]

    return list(D.get(inter(ax, bx)[0]))

def change(a, b):
    x, y = b
    l = list(mx[x])
    l.pop(y)
    l.insert(y, a)
    a = np.array([l])
    return np.concatenate((a, mx[x+1:]), axis=0)


# Solver
while check():
    Lch = []
    Dch={}
    i=0
    while True:
        i=i+1
        if i == 9:
            break
        else:
            for j in D.get(i):
                if np.isnan(j):
                    r, c = j
                    n=minus(dl, union(clean(mx[r])+clean(mx[c])+box(j)))
                    Lch.append(n)
                    Dch.update(n:j)
            if unique(Lch) != None:
                a, b = unique(Lch)
                change(a, Dch.get(b))
                i=
            
            
