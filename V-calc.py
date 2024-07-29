import tkinter

root=tkinter.Tk()
root.title("V-Calc")

#display box========================================================================================================================================================================================
d=tkinter.Entry(root,width=15,font=("ariel","15","bold"),bg="white",justify="right",fg="black",borderwidth=10)
d.grid(row=0,column=0,columnspan=3)
#numeric buttons====================================================================================================================================================================================
#func.numeric
def press(number):
    d.insert(tkinter.END,number)
    
bt1 = tkinter.Button(root,text="1",padx=23,pady=20,bg="black",fg="white",command=lambda:press(1))
bt2 = tkinter.Button(root,text="2",padx=23,pady=20,bg="black",fg="white",command=lambda:press(2))
bt3 = tkinter.Button(root,text="3",padx=23,pady=20,bg="black",fg="white",command=lambda:press(3))
bt4 = tkinter.Button(root,text="4",padx=23,pady=20,bg="black",fg="white",command=lambda:press(4))
bt5 = tkinter.Button(root,text="5",padx=23,pady=20,bg="black",fg="white",command=lambda:press(5))
bt6 = tkinter.Button(root,text="6",padx=23,pady=20,bg="black",fg="white",command=lambda:press(6))
bt7 = tkinter.Button(root,text="7",padx=23,pady=20,bg="black",fg="white",command=lambda:press(7))
bt8 = tkinter.Button(root,text="8",padx=23,pady=20,bg="black",fg="white",command=lambda:press(8))
bt9 = tkinter.Button(root,text="9",padx=23,pady=20,bg="black",fg="white",command=lambda:press(9))
bt0 = tkinter.Button(root,text="0",padx=88,pady=20,bg="black",fg="white",command=lambda:press(0))
#placement
bt1.grid(row=3,column=0)
bt2.grid(row=3,column=1)
bt3.grid(row=3,column=2)
bt4.grid(row=2,column=0)
bt5.grid(row=2,column=1)
bt6.grid(row=2,column=2)
bt7.grid(row=1,column=0)
bt8.grid(row=1,column=1)
bt9.grid(row=1,column=2)
bt0.grid(row=4,column=0,columnspan=3)

#opr butttons=====================================================================================================================================================================================
#func operational
def add():
    a=d.get()[-1]
    if a == ("+"):
        pass
    elif a == ("-"):
        pass
    elif a == ("*"):
        pass
    elif a == ("/"):
        pass
    else:
        d.insert(tkinter.END,"+")
        
btadd=tkinter.Button(root,text=(" + "),bg="grey",fg="yellow",pady=20,padx=40,command=add)
def sub():
    b=d.get()[-1]
    if b == ("+"):
        pass
    elif b == ("-"):
        pass
    elif b == ("*"):
        pass
    elif b == ("/"):
        pass
    else:
        d.insert(tkinter.END,"-")

btsub=tkinter.Button(root,text=(" - "),bg="grey",fg="yellow",pady=20,padx=40,command=sub)
def dev():
    c=d.get()[-1]
    if c == ("+"):
        pass
    elif c == ("-"):
        pass
    elif c == ("*"):
        pass
    elif c == ("/"):
        pass
    else:
        d.insert(tkinter.END,"/")

btdev=tkinter.Button(root,text=(" / "),bg="grey",fg="yellow",pady=20,padx=40,command=dev)
def mul():
    D=d.get()[-1]
    if D == ("+"):
        pass
    elif D == ("-"):
        pass
    elif D == ("*"):
        pass
    elif D == ("/"):
        pass
    else:
        d.insert(tkinter.END,"*")

btmul=tkinter.Button(root,text=(" * "),bg="grey",fg="yellow",pady=20,padx=40,command=mul)

#placement
btadd.grid(row=1,column=3,columnspan=2)
btsub.grid(row=2,column=3,columnspan=2)
btdev.grid(row=3,column=3,columnspan=2)
btmul.grid(row=4,column=3,columnspan=2)

#other buttons======================================================================================================================================================================================
def equals():
    if "+" in d.get():
        na1=d.get()[0:d.get().find("+")]
        na2=d.get()[d.get().find("+")-len(d.get()):]
        rsum=float(na1)+float(na2)
        d.delete(0,tkinter.END)
        d.insert(tkinter.END,rsum)

    if "-" in d.get():
        ns1=d.get()[0:d.get().find("-")]
        ns2=d.get()[d.get().find("-")-len(d.get()):]
        rsub=float(ns1)+float(ns2)
        d.delete(0,tkinter.END)
        d.insert(tkinter.END,rsub)

    if "/" in d.get():
        nd1=d.get()[0:d.get().find("/")]
        nd2=d.get()[1+d.get().find("/")-len(d.get()):]
        rdev=float(nd1)/float(nd2)
        d.delete(0,tkinter.END)
        d.insert(tkinter.END,rdev)

    if "*" in d.get():
        nm1=d.get()[0:d.get().find("*")]
        nm2=d.get()[1+d.get().find("*")-len(d.get()):]
        rmul=float(nm1)*float(nm2)
        d.delete(0,tkinter.END)
        d.insert(tkinter.END,rmul)

    else:
        pass
bteq=tkinter.Button(root,text=("="),padx=18,pady=20,command=equals).grid(row=0,column=3,columnspan=1)

def clear():
    d.delete(0,tkinter.END)
btC=tkinter.Button(root,text=("C"),padx=18,pady=20,command=clear).grid(row=0,column=4,columnspan=1)




