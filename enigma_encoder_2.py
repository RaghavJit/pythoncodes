import tkinter
from tkinter import messagebox

#added window
root=tkinter.Tk()
root.eval("tk::PlaceWindow %s center" % root.winfo_toplevel())
root.title("ENIGMA ENCODER-DECODER")
#title label
L=tkinter.Label(root,text="ENIGMA MACHINE", bg="grey", fg="black")
L.grid(row=0,column=0,columnspan=3)

window=tkinter.Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.withdraw()
#================================================================================USER INTERFACE===================================================================================================
#roller number entry
e1=tkinter.Entry(root, justify="center", borderwidth=5, font=("small fonts", "15", "bold"), bg="grey", fg="light blue", width="4")
e2=tkinter.Entry(root, justify="center", borderwidth=5, font=("small fonts", "15", "bold"), bg="grey", fg="light blue", width="4")
e3=tkinter.Entry(root, justify="center", borderwidth=5, font=("small fonts", "15", "bold"), bg="grey", fg="light blue", width="4")
#rolloer starter number entry
e4=tkinter.Entry(root, justify="center", borderwidth=5, font=("small fonts", "15", "bold"), bg="black", fg="cyan", width="4")
e5=tkinter.Entry(root, justify="center", borderwidth=5, font=("small fonts", "15", "bold"), bg="black", fg="cyan", width="4")
e6=tkinter.Entry(root, justify="center", borderwidth=5, font=("small fonts", "15", "bold"), bg="black", fg="cyan", width="4")
#placements
e1.grid(row=1,column=0)
e2.grid(row=1,column=1)
e3.grid(row=1,column=2)
e4.grid(row=2,column=0)
e5.grid(row=2,column=1)
e6.grid(row=2,column=2)
#guiding labels
l1=tkinter.Label(root, text="INPUT", width=8).grid(row=3,column=0)
l2=tkinter.Label(root, text="OUTPUT",width=8).grid(row=4,column=0)
#input output entry boxes
E1=tkinter.Entry(root, justify="left", width="20")
E2=tkinter.Entry(root, justify="left", width="20")

E1.grid(row=3,column=1,columnspan=2)
E2.grid(row=4,column=1,columnspan=2)

#bead board
l3=tkinter.Label(root, text=("------SET 1------"),width=40)
l3.grid(row=5,column=0,columnspan=5)
#set1
b0=tkinter.Entry(root, justify="center",width="8")
b1=tkinter.Entry(root, justify="center",width="8")
b2=tkinter.Entry(root, justify="center",width="8")
b3=tkinter.Entry(root, justify="center",width="8")
b4=tkinter.Entry(root, justify="center",width="8")
b5=tkinter.Entry(root, justify="center",width="8")
b6=tkinter.Entry(root, justify="center",width="8")
b7=tkinter.Entry(root, justify="center",width="8")
b8=tkinter.Entry(root, justify="center",width="8")
b9=tkinter.Entry(root, justify="center",width="8")
b0.grid(row=6,column=0)
b1.grid(row=7,column=0)
b2.grid(row=6,column=1)
b3.grid(row=7,column=1)
b28.grid(row=9,column=4)
b4.grid(row=6,column=2)
b5.grid(row=7,column=2)
b6.grid(row=6,column=3)
b7.grid(row=7,column=3)
b8.grid(row=6,column=4)
b9.grid(row=7,column=4)

#set2
l4=tkinter.Label(root, text=("------SET 2------"),width=40)
l4.grid(row=8,column=0,columnspan=5)
b20=tkinter.Entry(root, justify="center",width="8")
b21=tkinter.Entry(root, justify="center",width="8")
b22=tkinter.Entry(root, justify="center",width="8")
b23=tkinter.Entry(root, justify="center",width="8")
b24=tkinter.Entry(root, justify="center",width="8")
b25=tkinter.Entry(root, justify="center",width="8")
b26=tkinter.Entry(root, justify="center",width="8")
b27=tkinter.Entry(root, justify="center",width="8")
b28=tkinter.Entry(root, justify="center",width="8")
b29=tkinter.Entry(root, justify="center",width="8")
b20.grid(row=9,column=0)
b21.grid(row=10,column=0)
b22.grid(row=9,column=1)
b23.grid(row=10,column=1)
b24.grid(row=9,column=2)
b25.grid(row=10,column=2)
b26.grid(row=9,column=3)
b27.grid(row=10,column=3)
b28.grid(row=9,column=4)
b29.grid(row=10,column=4)
#=====================================================================================SYSTEM=======================================================================================================
#alphabet dict.
D1={0:"a", 1:"b", 2:"c", 3:"d", 4:"e", 5:'f', 6:'g', 7:'h', 8:'i', 9:'j', 10:'k', 11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y',
    25:'z'}
D2={'a':0,'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24,
    'z':25}

#rotters
l1=[25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 26, 7, 19, 8, 12, 22]
l2=[5, 1, 13, 16, 9, 8, 21, 20, 6, 11, 26, 2, 4, 22, 24, 14, 18, 21, 25, 17, 3, 12, 23, 7, 19, 15]
l3=[4, 13, 22, 1, 5, 10, 16, 2, 16, 23, 18, 7, 12, 24, 21, 19, 3, 8, 17, 6, 14, 11, 20, 15, 9, 25]
l4=[10, 3, 26, 1, 21, 11, 8, 15, 14, 17, 4, 19, 2, 23, 12, 24, 6, 9, 25, 13, 5, 7, 20, 22, 16, 18]
l5=[13, 1, 17, 22, 7, 14, 4, 20, 10, 15, 4, 5, 19, 26, 12, 11, 2, 21, 16, 8, 25, 9, 23, 6, 18, 23]

def reset():
    e1.delete(0,tkinter.END)
    e2.delete(0,tkinter.END)
    e3.delete(0,tkinter.END)
    e4.delete(0,tkinter.END)
    e5.delete(0,tkinter.END)
    e6.delete(0,tkinter.END)
btimp=tkinter.Button(root, text=(" RESET "), bg="grey", fg="yellow", padx=11, pady=20, command=reset)
btimp.grid(row=0, column=3, rowspan=2)#debug of incorrect execution of statements

#encoding 
def encode():
    #clearing outputbox
    E2.delete(0,tkinter.END)
    
    #check rootters
    if (int(e1.get()) in [1,2,3,4,5])==True:
        pass
    else:
        e1.delete(0,tkinter.END)
        tkinter.messagebox.showerror("ERROR", "Choose rotters: 1,2,3,4,5")
    window.quit()

    if (int(e2.get()) in [1,2,3,4,5])==True:
        pass
    else:
        e2.delete(0,tkinter.END)
        tkinter.messagebox.showerror("ERROR", "Choose rotters: 1,2,3,4,5")
    window.quit()

    if (int(e3.get()) in [1,2,3,4,5])==True:
        pass
    else:
        e3.delete(0,tkinter.END)
        tkinter.messagebox.showerror("ERROR", "Choose rotters: 1,2,3,4,5")
    window.quit()

    #check numbers
    if (int(e4.get()) in [25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 26, 7, 19, 8, 12, 22])==True:
        pass
    else:
        e4.delete(0,tkinter.END)
        tkinter.messagebox.showerror("ERROR", "Choose numbers: 1 to 26")
    window.quit()

    if (int(e5.get()) in [25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 26, 7, 19, 8, 12, 22])==True:
        pass
    else:
        e5.delete(0,tkinter.END)
        tkinter.messagebox.showerror("ERROR", "Choose numbers: 1 to 26")
    window.quit()

    if (int(e6.get()) in [25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 26, 7, 19, 8, 12, 22])==True:
        pass
    else:
        e6.delete(0,tkinter.END)
        tkinter.messagebox.showerror("ERROR", "Choose numbers: 1 to 26")
    window.quit()
    #check ended

    #creating useful list
    ref_dict={"l1":l1,"l2":l2,"l3":l3,"l4":l4,"l5":l5}
    x=str("l")+e1.get()
    y=str("l")+e2.get()
    z=str("l")+e3.get()
    X=ref_dict.get(str(x))
    Y=ref_dict.get(str(y))
    Z=ref_dict.get(str(z)) #input lists
    
    #adding starter number choosal
    a=X.index(int(e4.get()))
    X0=X[a:]+X[:a]

    b=Y.index(int(e5.get()))
    Y0=Y[b:]+Y[:b]

    c=Z.index(int(e6.get()))
    Z0=Z[c:]+Z[:c]
    Fl=X0+Y0+Z0 #final list created 

    #processing letters of input with rotters
    for i in range(0,len(str(E1.get()))):
        if str(E1.get())[i]==(" "):
            E2.insert(tkinter.END," ")
        else:
            V=E1.get()[i]
            V1=(D2.get(V)+Fl[i])%26
            V2=D1.get(V1)
            #replacing letters from final string
            if V2==(b0.get()):
                E2.insert(tkinter.END,b1.get())
            elif V2==(b2.get()):
                E2.insert(tkinter.END,b3.get())
            elif V2==(b4.get()):
                E2.insert(tkinter.END,b5.get())
            elif V2==(b6.get()):
                E2.insert(tkinter.END,b7.get())
            elif V2==(b8.get()):
                E2.insert(tkinter.END,b9.get())
            elif V2==(b20.get()):
                E2.insert(tkinter.END,b21.get())
            elif V2==(b22.get()):
                E2.insert(tkinter.END,b23.get())
            elif V2==(b24.get()):
                E2.insert(tkinter.END,b25.get())
            elif V2==(b26.get()):
                E2.insert(tkinter.END,b27.get())
            elif V2==(b28.get()):
                E2.insert(tkinter.END,b29.get())
            elif V2==(b1.get()):#swipe2
                E2.insert(tkinter.END,b0.get())
            elif V2==(b3.get()):
                E2.insert(tkinter.END,b2.get())
            elif V2==(b5.get()):
                E2.insert(tkinter.END,b4.get())
            elif V2==(b7.get()):
                E2.insert(tkinter.END,b6.get())
            elif V2==(b9.get()):
                E2.insert(tkinter.END,b8.get())
            elif V2==(b21.get()):
                E2.insert(tkinter.END,b20.get())
            elif V2==(b23.get()):
                E2.insert(tkinter.END,b22.get())
            elif V2==(b25.get()):
                E2.insert(tkinter.END,b24.get())
            elif V2==(b27.get()):
                E2.insert(tkinter.END,b26.get())
            elif V2==(b29.get()):
                E2.insert(tkinter.END,b28.get())    
            else:
                E2.insert(tkinter.END,V2)
        

btenc=tkinter.Button(root, text=("encode"), bg="grey", fg="yellow", padx=10, pady=10, command=encode)
btenc.grid(row=2, column=3)

#decoding
def decode():
    #recreating useful list
    ref_dict={"l1":l1,"l2":l2,"l3":l3,"l4":l4,"l5":l5}
    x=str("l")+e1.get()
    y=str("l")+e2.get()
    z=str("l")+e3.get()
    X=ref_dict.get(str(x))
    Y=ref_dict.get(str(y))
    Z=ref_dict.get(str(z)) #input lists
    
    #adding starter number choosal
    a=X.index(int(e4.get()))
    X0=X[a:]+X[:a]

    b=Y.index(int(e5.get()))
    Y0=Y[b:]+Y[:b]

    c=Z.index(int(e6.get()))
    Z0=Z[c:]+Z[:c]
    Fl=X0+Y0+Z0 #final list created 

    for i in range(len(str(E1.get()))):
        if E1.get()[i]==(" "):
            E2.insert(tkinter.END," ")

        elif E1.get()[i]==str(b1.get()):
            v0a=((D2.get(b0.get())+26)-Fl[i])-26
            if (v0a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v0a))
            else:
                v0b=(D2.get(b0.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v0b))

        elif E1.get()[i]==str(b3.get()):
            v1a=((D2.get(b2.get())+26)-Fl[i])-26
            if (v1a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v1a))
            else:
                v1b=(D2.get(b2.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v1b))

        elif E1.get()[i]==str(b5.get()):
            v2a=((D2.get(b4.get())+26)-Fl[i])-26
            if (v2a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v2a))
            else:
                v2b=(D2.get(b4.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v2b))

        elif E1.get()[i]==str(b7.get()):
            v3a=((D2.get(b6.get())+26)-Fl[i])-26
            if (v3a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
               E2.insert(tkinter.END,D1.get(v3a)) 
            else:
                v3b=(D2.get(b6.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v3b))

        elif E1.get()[i]==str(b9.get()):
            v4a=((D2.get(b8.get())+26)-Fl[i])-26
            if (v4a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v4a))
            else:
                v4b=(D2.get(b8.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v4b))

        elif E1.get()[i]==str(b21.get()):
            v5a=((D2.get(b20.get())+26)-Fl[i])-26
            if (v5a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v5a))
            else:
                v5a=(D2.get(b20.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v5a))

        elif E1.get()[i]==str(b23.get()):
            v6a=((D2.get(b22.get())+26)-Fl[i])-26
            if (v6a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v6a))
            else:
                v6a=(D2.get(b22.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v6a))

        elif E1.get()[i]==str(b25.get()):
            v7a=((D2.get(b24.get())+26)-Fl[i])-26
            if (v7a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v7a))
            else:
                v7b=(D2.get(b24.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v7b))

        elif E1.get()[i]==str(b27.get()):
            v8a=((D2.get(b26.get())+26)-Fl[i])-26
            if (v8a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v8a))
            else:
                v8b=(D2.get(b26.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v8b))

        elif E1.get()[i]==str(b29.get()):
            v9a=((D2.get(b28.get())+26)-Fl[i])-26
            if (v9a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v9a))
            else:
                v9b=(D2.get(b28.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v9b))

        elif E1.get()[i]==str(b0.get()):#upswipe2
            v0a=((D2.get(b1.get())+26)-Fl[i])-26
            if (v0a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v0a))
            else:
                v0b=(D2.get(b1.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v0b))

        elif E1.get()[i]==str(b2.get()):
            v1a=((D2.get(b3.get())+26)-Fl[i])-26
            if (v1a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v1a))
                print(v1a)
            else:
                v1b=(D2.get(b3.get())+26)-Fl[i]
                print(b2.get(),v1b)
                E2.insert(tkinter.END,D1.get(v1b))

        elif E1.get()[i]==str(b4.get()):
            v2a=((D2.get(b5.get())+26)-Fl[i])-26
            if (v2a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v2a))
            else:
                v2b=(D2.get(b5.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v2b))

        elif E1.get()[i]==str(b6.get()):
            v3a=((D2.get(b7.get())+26)-Fl[i])-26
            if (v3a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
               E2.insert(tkinter.END,D1.get(v3a)) 
            else:
                v3b=(D2.get(b7.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v3b))

        elif E1.get()[i]==str(b8.get()):
            v4a=((D2.get(b9.get())+26)-Fl[i])-26
            if (v4a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v4a))
            else:
                v4b=(D2.get(b9.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v4b))

        elif E1.get()[i]==str(b20.get()):
            v5a=((D2.get(b21.get())+26)-Fl[i])-26
            if (v5a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v5a))
            else:
                v5a=(D2.get(b21.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v5a))

        elif E1.get()[i]==str(b22.get()):
            v6a=((D2.get(b23.get())+26)-Fl[i])-26
            if (v6a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v6a))
            else:
                v6a=(D2.get(b23.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v6a))

        elif E1.get()[i]==str(b24.get()):
            v7a=((D2.get(b25.get())+26)-Fl[i])-26
            if (v7a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v7a))
            else:
                v7b=(D2.get(b25.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v7b))

        elif E1.get()[i]==str(b26.get()):
            v8a=((D2.get(b27.get())+26)-Fl[i])-26
            if (v8a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v8a))
            else:
                v8b=(D2.get(b27.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v8b))

        elif E1.get()[i]==str(b28.get()):
            v9a=((D2.get(b29.get())+26)-Fl[i])-26
            if (v9a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v9a))
            else:
                v9b=(D2.get(b29.get())+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v9b))        
                
        else:
            v10a=((D2.get(E1.get()[i])+26)-Fl[i])-26
            if (v10a in [0, 25, 21, 13, 15 ,24, 2, 3, 17, 18, 23, 5, 20, 9, 11, 1, 14, 6, 10, 16, 4, 7, 19, 8, 12, 22])==True:
                E2.insert(tkinter.END,D1.get(v10a))
            else:
                v10b=(D2.get(E1.get()[i])+26)-Fl[i]
                E2.insert(tkinter.END,D1.get(v10b))

btdec=tkinter.Button(root, text=("decode"), bg="grey", fg="yellow", padx=10, pady=10, command=decode)
btdec.grid(row=3, column=3, rowspan=2)

def clear():
    E1.delete(0,tkinter.END)
    E2.delete(0,tkinter.END)
btclear=tkinter.Button(root, text=(" C "), bg="white", fg="black", padx=15, pady=65, command=clear)
btclear.grid(row=0, column=4, rowspan=5)



tkinter.mainloop()




