import random
#list shuffler
l=[1,2,3]
x=[]#empty list
while True:
    i=random.randint(0,2)
    print(l[i])
    if(int(l[i]) in x)==False:
        x.extend(l[i])
        if len(x)==26:
            print(x)
