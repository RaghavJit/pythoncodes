import random
l1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
l2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
l3=['0','1','2','3','4','5','6','7','8','9']
l4=['!','@','#','$','%','^','&','*','(',')','[',']']
lm=[l1,l2,l3,l4]
def check(v):
    for i in range(0,len(v)):
        if v[i] in l3:
            pass
        else:
            return False
def gen(x1):
    s=''
    if x1=='Max':
        for i in range(0,8):
            v=random.choice(lm)
            n=random.choice(v)
            s=s+n
        return s
    elif x1=='Med':
        for i in range(0,6):
            v=random.choice(lm)
            n=random.choice(v)
            s=s+n
        return s
    elif x1=='Min':
        for i in range(0,4):
            v=random.choice(lm)
            n=random.choice(v)
            s=s+n
        return s
    elif check(x1)!=False:
        for i in range(0,int(x1)):
            v=random.choice(lm)
            n=random.choice(v)
            s=s+n
        return s
    else:
        return "INVALID INPUT"

while True:
    x=input("Enter Password strength; 'Max', 'Med', 'Min', or NUMBER of characters desired: ")
    print(gen(x))

