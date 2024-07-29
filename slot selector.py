#slot checker
S1=[('02:00 am', '04:00 am'),('08:00 am', '10:00 am'),('04:00 pm', '06:00 pm')]
S2=[('03:00 am', '05:00 am'),('07:00 am', '09:00 am'),('03:00 pm', '05:00 pm'),('08:00 pm', '10:00 pm')] 

def btw(a,b):
    v1, v2=b
    if a>v1:
        c2=True
        if a<v2:
            c1=True
            if (c1 and c2)==True:
                return [a, v2]
    elif a<v1:
        c12=True
        if a>v2:
            c11=True
            if (c11 and c12)==True:
                return [v1, a]

c=-1
for i in S1:
    c=c+1
    t1, t2=i
    for j in [t1, t2]:
        if btw(j,S2[c]) != None:
            print(btw(j,S2[c]))
