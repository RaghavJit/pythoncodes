l1=['a','b','c']
l2=['d','e','f']
l3=['g','h','i']
l4=['j','k','l']
l5=['m','n','o']
l6=['p','q','r','s']
l7=['t','u','v']
l8=['w','x']
l9=['y','z']
s=''
x=input()
for i in range(len(x)):
    if x[i] in l1:
        v='1'+str(int(l1.index(x[i])+1))
    if x[i] in l2:
        v='2'+str(int(l2.index(x[i])+1))
    if x[i] in l3:
        v='3'+str(int(l3.index(x[i])+1))
    if x[i] in l4:
        v='4'+str(int(l4.index(x[i])+1))
    if x[i] in l5:
        v='5'+str(int(l5.index(x[i])+1))
    if x[i] in l6:
        v='6'+str(int(l6.index(x[i])+1))
    if x[i] in l7:
        v='7'+str(int(l7.index(x[i])+1))
    if x[i] in l8:
        v='8'+str(int(l8.index(x[i])+1))
    if x[i] in l9:
        v='9'+str(int(l9.index(x[i])+1))
    s=s+v
print(s)
