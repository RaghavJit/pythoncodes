try:
    y=int(input('enter the number of numbers'))
except:
    print('INVALID INPUT')
    exit()
    
l=[]
l2=[]
try:
    for i in range(0,y):
        x=int(input('enter the number'))
        try:
            l.append(x)
        except:
            print('INVALID INPUT')
    for i in range(0,len(l)):
        l2.append(max(l))
        l.pop(max(l))
    print(l2)
except:
    pass
