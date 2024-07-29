import tkinter
import math
root=tkinter.Tk()
root.title("figure to number")
e1=tkinter.Entry(root, justify="left",width="40")
e1.grid(column=0,row=0)
e2=tkinter.Entry(root, justify="left", width="70")
e2.grid(column=0,row=1, rowspan=2,columnspan=2)


d1={'0':'Zero','1':"One",'2':"Two",'3':"Three",'4':"Four",'5':"Five",'6':"Six",'7':"Seven",'8':"Eight",'9':"Nine"}
ds={'10':"Ten",'11':"Eleven",'12':"Twelve",'13':"Thirteen",'14':"Fourteen",'15':"Fifteen",'16':"Sixtten",'17':"Seventeen",'18':"Eighteen",'19':"Ninteen"}
d2={'2':"Twenty",'3':"Thirty",'4':"Fourty",'5':"Fifty",'6':"Sixty",'7':"Seventy",'8':"Eighty",'9':"Ninty"}
d3={4:"Thousand",6:"Lakh" ,8:"Crore",10:"Arab", 12:"Kharab"}

def one(f1):
    return d1.get(f1)
def two(f2):
    if f2==("00"):
        return ("")
    elif f2[0]==("0"):
        return one(f2[1:])
    else:
        if f2[0]==("1"):
            return ds.get(f2)
        else:
            if (("0") in f2)==True:
                return d2.get(f2[0])
            else:
                return d2.get(f2[0])+d1.get(f2[1])
def three(f3):
    if f3[0]==("0"):
        return two(f3[1:])
    else:
        if f3[1]==("1"):
            return d1.get(f3[0])+"Hundred,"+" "+two(f3[1:])
        else:
            return d1.get(f3[0])+"Hunderd,"+" "+two(f3[1:])
def more(fm):
    if len(fm)/2==math.floor(len(fm)/2): #even
        r=(len(fm)-2)/2-1
        v=0
        w=0
        w=one(fm[0])+d3.get(len(fm))+(" ")
        if len(fm)<=4:
            return w+(" ")+three(fm[-3:])
        else:
            for i in range(0,int(r)):
                if fm[1+(i*2):3+(i*2)]==("00"):
                    v=("")
                else:
                    v=two(fm[1+(i*2):3+(i*2)])+d3.get(len(fm)-(2)*(i+1))+(" ")
                w=w+v
                if i==r-1:
                    w=w+three(fm[-3:])
                    return w
    else:
        r=(len(fm)-3)/2 #odd 
        v=0
        w=("")
        for i in range(0,int(r)):
            if two(fm[0+(i*2):2+(i*2)])=="00":
                v=("")
            else:
                v=two(fm[0+(i*2):2+(i*2)])+d3.get(len(fm)-(i*2)-1)+(" ")
            w=w+v
            if i==r-1:
                w=w+three(fm[-3:])
                return w
                    
def sort():
    e2.delete(0,tkinter.END)
    if len(e1.get())==1:
        e2.insert(tkinter.END,one(e1.get()))
    elif len(e1.get())==2:
        e2.insert(tkinter.END,two(e1.get()))
    elif len(e1.get())==3:
        e2.insert(tkinter.END,three(e1.get()))
    else:
        e2.insert(tkinter.END,more(e1.get()))
        
b1=tkinter.Button(root, text=("conv."), width="20", command=sort)
b1.grid(column=1,row=0)

tkinter.mainloop()
