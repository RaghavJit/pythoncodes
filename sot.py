x=0
l1=[]
l2=[]

while x!='ok':
    x=input()
    if x=='ok':
        print(l1)
        print(len(l1))
    else:
        l1.append(int(x))
l=len(l1)

for i in range(0,len(l1)):
    l2.append(min(l1))
    l1.remove(min(l1))
    if len(l2)==l:
        print(l2)
        
q=input("END")
