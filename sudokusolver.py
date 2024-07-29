import numpy as np
import matx81
mx=matx81.mx
print(mx)
#basic functions
def find(l): #to look for absent elements
    L=[]
    for i in range(1,10):
        if i in l:
            continue
        else:
            L.append(i)
    return L

def identify(l1,l2,l3): #to look for common elements
    masl=[]
    for i in l1:
        if (i in l2)==True:
            if (i in l3)==True:
                masl.append(i)
            else:
                continue
        else:
            continue
    return masl, len(masl)

def box(a,b): #to generate list of elements in the box
    if (a in [0,1,2])==True:
        r= 1
    elif (a in [3,4,5])==True:
        r= 2
    elif (a in [6,7,8])==True:
        r= 3
   
    if (b in [0,1,2])==True:
        c= 1
    elif (b in [3,4,5])==True:
        c= 2
    elif (b in [6,7,8])==True:
        c= 3

    D={(1,1):1,(1,2):2,(1,3):3,(2,1):4,(2,2):5,(2,3):6,(3,1):7,(3,2):8,(3,3):9}

    x=D.get((r,c))

    D2={1:[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        ,2:[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
        ,3:[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]
        ,4:[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]
        ,5:[(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]
        ,6:[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]
        ,7:[(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]
        ,8:[(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]
        ,9:[(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]}

    lb=[]
    for i in D2.get(x):
        r1, c1=i
        lb.append(mx[r1][c1])
    return lb

def fiuq(l): #to find the unique number in a list for filling the place
    l1=[]
    l2=[]
    for i in l:
        if (i in l1)==True:
            if (i in l2)==True:
                pass
            else:
                l2.append(i)
        else:
            l1.append(i)
    l2.sort()
    l1.sort()
    for i in l2:
        if (i in l1)==True:
            l1.remove(i)
        else:
            continue
    return l1
#secondary fuctions    
#fill the primary squares using elemination method
#check if a row can be filled fill if so
#chech if a row can be filled fill of so
#use data form a row or column to fill squares in a box (probably using cache list)


                    
