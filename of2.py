import random
def make():
    l=[]
    while len(l)!=4:
        a=random.randint(0,9)
        if a in l:
            pass
        else:
            l.append(a)
    s=''
    for i in range(0,4):
        n=l[i]
        s=s+str(n)
    return s

def check(v1,v2):
    try:
        for i in range(0,4):
            if v1[i] in v2:
                if v1[i]==v2[i]:
                    print(v1[i]+' is at right position')
                else:
                    print(v1[i]+' is incorrectly placed')
            else:
                print(v1[i]+' is wrong entry')
    except:
        return 'INVALID INPUT'
while True:
    ans=make()
    print(ans)
    for i in range(0,3):
        p=input('Enter your guess You have '+str(3-i)+' chances left: ')
        if p==ans:
            print('YOU WON!!')
            break
        else:
            if i==2:
                print('YOU LOST!!')
                print('Number was '+str(ans))
            else:
                print(check(p,ans))
                continue
