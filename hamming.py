import numpy as np
import math

global am, ar
ar = np.full([4,4], np.nan)
am = np.full([4,4], np.nan)
Dc={1:(0,3) ,2:(1,1) ,3:(1,2) ,4:(1,3) ,5:(2,1) ,6:(2,2) ,7:(2,3) ,8:(3,0) ,9:(3,1) ,10:(3,2) ,11:(3,3)}

while True:
    x = int(input())
    if x >= 2047:
        print('enter number smaller than or equal to 2047')
        continue
    else:
        y = bin(x)
        y1=str(y)[2:]
        print(y1)
        break
    
def genpe(n):
    c1 = 0
    for i in range(len(str(n))):
        if str(n)[i] == '1':
            c1=c1+1
    if c1%2 == 0:
        return 0
    else:
        return 1

def change(X, a, b):
    x, y = b
    l = list(X[x])
    l.pop(y)
    l.insert(y, a)
    a = np.array([l])
    X = np.concatenate((X[:x], a, X[x+1:]), axis=0)
    return X

def com(s):
    return '0'*(4-len(s)) + str(s)

def com1(s):
    return '0'*(11-len(s)) + str(s)

for i in range(1,12):
    am=change(am, com1(y1)[i-1], Dc.get(i))

def hamming():
    global am, ar
    D = {}
    for i in range(4):
        for j in range(4):
            n = ((i)*4)+j
            d = str(bin(n))[2:]
            D.update({(i,j):com(d)})
            ar = change(ar, com(d), (i,j))

    p1 = ''
    p2 = ''
    p3 = ''
    p4 = ''
    mp = ''

    for i in range(4):
        for j in range(4):
            if str(ar[i,j])[3] == '1':
                if str(am[i,j]) == '1':
                    p1 = p1+'1'
    am = change(am, genpe(p1), (0, 1))

    for i in range(4):
        for j in range(4):
            if str(ar[i,j])[2] == '1':
                if str(am[i,j]) == '1':
                    p2 = p2 +'1'
    am = change(am, genpe(p2), (0, 2))

    for i in range(4):
        for j in range(4):
            if str(ar[i,j])[1] == '1':
                if str(am[i,j]) == '1':
                    p3 = p3 +'1'
    am = change(am, genpe(p3), (1, 0))

    for i in range(4):
        for j in range(4):
            if str(ar[i,j])[0] == '1':
                if str(am[i,j]) == '1':
                    p4 = p4+'1'
    am = change(am, genpe(p4), (2,0))

    for i in range(4):
        for j in range(4):
            if am[i,j] in ['0', '1']:
                mp =  mp + str(am[i,j])
    am = change(am, genpe(mp), (0,0))
    return am

def hammingdec():
    pl1 = []
    pl2 = []
    pl3 = []
    pl4 = []
    
    for i in range(4):
        for j in range(4):
            if am[i,j] in ['0', '1']:
                mp =  mp + str(am[i,j])
    if genpe(mp) != am[0,0]:
        print('Error in Matrix')

    for i in range(4):
        for j in range(4):
            if (i ,j) != (2, 0):
                if str(ar[i,j])[0] == '1':
                    pl4.append((i, j))
                    if str(am[i,j]) == '1':
                        p4 = p4+'1'
    if genpe(p4) != am[2,0]:









