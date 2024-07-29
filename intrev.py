d1 ={1:'a',2:'b',3:'c'}
d2 ={1:'d',2:'e',3:'f'}
d3 ={1:'g',2:'h',3:'i'}
d4 ={1:'j',2:'k',3:'l'}
d5 ={1:'m',2:'n',3:'o'}
d6 ={1:'p',2:'q',3:'r',4:'s'}
d7 ={1:'t',2:'u',3:'v'}
d8 ={1:'w',2:'x'}
d9 ={1:'y',2:'z'}
refd={1:d1,2:d2,3:d3,4:d4,5:d5,6:d6,7:d7,8:d8,9:d9}
x=input("XXX")
for i in range(0,int(len(x)/2)):
    n=i*2
    v=refd.get(int(x[n]))
    v.get(n+1)
    print(v.get(n+1))