import random
import tkinter as tk
from tkinter import messagebox


#Window 
root=tk.Tk()
root.title("TIC-TAC-TOE")
root.eval("tk::PlaceWindow %s center" % root.winfo_toplevel())

#Title label
l0=tk.Label(root, text=("TIC-TAC-TOE"),  font=('Constantia', '15', 'bold'), width=28)
l0.grid(row=0, column=0, rowspan=None, columnspan=4)

#Display game status
l1=tk.Label(root, text=("COMPUTER :"), font=('Arial', '15')) 
l1.grid(row=3, column=0, rowspan=None, columnspan=None)

e0=tk.Entry(root, font=('Arial', '15'), width= 33)
e0.grid(row=3, column=1, rowspan=None, columnspan=3)

#Mode choice multi or solo (PLAYER 1, PLAYER 2)
global pc
pc=tk.IntVar()
def choice1():
    if pc.get()==1:
        e0.delete(0,tk.END)
        e0.insert(tk.END,'1 PLAYER>  ')
        r3['state']='active'
        r4['state']='active'
        reset() #resetting the board

    elif pc.get()==2: #disables symbol choosal when playing multiplayer
        e0.delete(0,tk.END)
        e0.insert(tk.END,'2 PLAYER  ')
        r3['state']='disable'
        r4['state']='disable'
        reset() #resetting the board
        
r1=tk.Radiobutton(root, variable=pc, value=1, text=('1 PLAYER'), font=('Arial', '15'), command=choice1) #button to choose single player mode
r1.grid(row=1, column=0, rowspan=None, columnspan=2) 
r2=tk.Radiobutton(root, variable=pc, value=2, text=('2 PLAYER'),  font=('Arial', '15'), command=choice1) #button to choose multiplayer mode
r2.grid(row=1, column=2, rowspan=None, columnspan=2)

#Symbol choice (X or O)
global ps
ps=tk.StringVar()
def choice2():
    if pc.get()==1:
        e0.delete(9,tk.END)
        e0.insert(tk.END,'  YOU HAVE CHOSEN : ' + str(ps.get()))
        reset() #resetting the board
    elif pc.get()==2:
        e0.delete(9,tk.END)
        e0.insert(tk.END,'  YOU HAVE CHOSEN : ' + str(ps.get()))
        reset() #resetting the board

r3=tk.Radiobutton(root, variable=ps, value='X', text=('X'), font=('Arial', '15'), command=choice2) #button to choose 'X' as playing symbol
r3.grid(row=2, column=0, rowspan=None, columnspan=2)
r4=tk.Radiobutton(root, variable=ps, value='O', text=('O'), font=('Arial', '15'), command=choice2) #button to choose 'O' as playing symbol
r4.grid(row=2, column=2, rowspan=None, columnspan=2)

#Board
#Boxes for tic tac toe
e1=tk.Entry(root, borderwidth=6, font=('Constantia', '55', 'bold'), width=3, justify='center')
e1.grid(row=4, column=0, rowspan=None, columnspan=None)
e2=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e2.grid(row=4, column=1, rowspan=None, columnspan=None)
e3=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e3.grid(row=4, column=2, rowspan=None, columnspan=None)
e4=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e4.grid(row=5, column=0, rowspan=None, columnspan=None)
e5=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e5.grid(row=5, column=1, rowspan=None, columnspan=None)
e6=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e6.grid(row=5, column=2, rowspan=None, columnspan=None)
e7=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e7.grid(row=6, column=0, rowspan=None, columnspan=None)
e8=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e8.grid(row=6, column=1, rowspan=None, columnspan=None)
e9=tk.Entry(root, borderwidth=5, font=('Constantia', '55', 'bold'), width=3, justify='center')
e9.grid(row=6, column=2, rowspan=None, columnspan=None)

#Display result and warnings
e10=tk.Entry(root, borderwidth=10, width=36, justify="center", font=('Arial','15'))
e10.grid(row=8,column=0,rowspan=None, columnspan=3)

#Data and variables
li1=[e1,e2,e3,e4,e5,e6,e7,e8,e9]
li2=[e1,e2,e3,e4,e5,e5,e5,e5,e6,e7,e8,e9]
q1=[e1, e2, e3]
q2=[e4, e5, e6]
q3=[e7, e8, e9]
q4=[e1, e4, e7]
q5=[e2, e5, e8]
q6=[e3, e6, e9]
q7=[e1, e5, e9]
q8=[e3, e5, e7]
lq=[q1, q2, q3, q4, q5, q6, q7, q8]
D={e1:[q1 ,q4 ,q7], e2:[q1 ,q5], e3:[q1, q3, q8], e4:[q2, q4], e5:[q2, q5, q7, q8], e6:[q2, q6], e7:[q4, q3, q8], e8:[q3, q5], e9:[q3, q6, q8]}
m=[e5]
c=[e1, e3, e7, e9]
s=[e2, e4, e6, e8]
global co, Sch
co=0
Sch=''
Dch={}

#Action / turn confirmation
def press():
    global co
    global Sch
    a, b = finder() #calling finder for f2
    L1=[]
    L2=[]
    
    # If 1 player  ###################################################################################################################################################################
    if pc.get()==1:

        #CHECKS
        #check for invalid entries (c1)
        c1=True
        if ps.get()=='':
            tk.messagebox.showerror("ERROR", "CHOOSE A PLAYING SYMBOL FIRST!")
            reset()
            c1=False
        else:
            for i in li1:
                if i.get() in ['X', 'O', '']:
                    pass
                else:
                    tk.messagebox.showerror("ERROR", "INVALID ENTRY: ONLY " +str(ps.get())+ " ALLOWED!")
                    i.delete(0,tk.END)
                    c1=False
                
        #check for extra entries / turn taken (c2)
        c2=True
        if c1==True:
            co=co+1
            for i in li1:
                if i.get()!='':
                    if i not in Dch:
                        Dch.update({i:i.get()})
                        Sch=Sch+i.get()

            if ('OO' in Sch) or ('XX' in Sch):
                tk.messagebox.showerror("ERROR", "CANNOT TAKE TWO TURNS AT ONCE!")
                reset() #resetting the board
                c2=False

            if len(Sch)>co:
                tk.messagebox.showerror("ERROR", "CANNOT TAKE TWO TURNS AT ONCE!")
                reset() #resetting the board
                c2=False
            elif co>len(Sch): 
                co=co-1
                if all([e1.get()=='',e2.get()=='',e3.get()=='',e4.get()=='',e5.get()=='',e6.get()=='',e7.get()=='',e8.get()=='',e9.get()=='']):
                    c2=True
                else:
                    c2=False
                
        else:
            c2=False

        if c2==True:
            if all([e1.get()!='', e2.get()!='', e3.get()!='', e4.get()!='', e5.get()!='', e6.get()!='', e7.get()!='', e8.get()!='', e9.get()!='']):
                if e10.get()=='':
                    e10.insert(tk.END, "THIS GAME IS A TIE")
                    res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                    c2=False
                    if res==False:
                        quit()
                    else:
                        reset()
                        
        #COMPUTER TAKES TURN
        if c2== True:
            #randomly fill a box if board is empty' (f1)
            if all([e1.get()=='',e2.get()=='',e3.get()=='',e4.get()=='',e5.get()=='',e6.get()=='',e7.get()=='',e8.get()=='',e9.get()=='']):
                e=random.choice(li2)
                e.insert(tk.END, inv())          
                #updating counter and cache 
                co=co+1
                Dch.update({e:inv()})
                Sch=Sch+inv()

            #fill _XX, X_X, XX_ (f2)
            elif a:
                b.insert(tk.END, inv())
                #updating counter and cache
                co=co+1
                Dch.update({b:inv()})
                Sch=Sch+inv()
        
            #turn function (f3)        
            else:
                for i in li1:
                    if i.get()==ps.get():
                        L1.extend(D.get(i))
                    elif i.get()==inv():
                        L2.extend(D.get(i))

                if L2==[]: #letting user take first turn
                    for i in li1:
                        if i.get()==ps.get():
                            L=pref(union(join(D.get(i))))
                    e=random.choice(L)              
                    if e.get()=='':
                            e.insert(tk.END, inv())
                            #updating counter and cache
                            co=co+1
                            Dch.update({e:inv()})
                            Sch=Sch+inv()

                else:
                    I= inter(union(L1), union(L2))   
                    print(I)
                    C=minus(union(L1), I)
                    P=minus(union(L2), I)

                    L=inter(union(join(C)), union(join(P)))
                    print(L)
                    Lch=[]
                    for i in L:
                        if i.get()=='':
                            Lch.append(i)
                    print(Lch)
                            
                    if  len(pref(Lch)) >1:
                        print(Lch)
                        d=random.choice(pref(Lch))
                        d.insert(tk.END, inv())
                        #updating counter and cache
                        co=co+1
                        Dch.update({d:inv()})
                        Sch=Sch+inv()

                    elif len(pref(Lch)) ==1:
                        print(Lch)
                        d=Lch[0]
                        d.insert(tk.END, inv())
                        #updating counter and cache
                        co=co+1
                        Dch.update({d:inv()})
                        Sch=Sch+inv()

                    elif len(pref(Lch)) == 0:
                        e10.insert(tk.END, "THIS GAME IS A TIE")
                        res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                        c2=False
                        if res==False:
                            quit()
                        else:
                            reset()
                        
                    
        #END OF GAME
        #check for completion
        if c2==True:                                       
            cl1=[] #counter list 1
            cl2=[] #counter list 2
            for i in lq:
                for j in i:
                    if j.get()==ps.get():
                        cl1.append(True)
                    elif j.get()==inv():
                        cl2.append(False)
                    else:
                        cl1.clear()
                        cl2.clear()
                        
                if (len(cl1)==3) or (len(cl2)==3):
                    if cl1==[True, True, True]:
                        e10.insert(tk.END, "PLAYER " +ps.get()+ " HAS WON THE GAME")
                        res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                        if res==False:
                            quit()
                        else:
                            reset()
                            
                    elif cl2==[False, False, False]:
                        e10.insert(tk.END, "PLAYER " + inv()+ " HAS WON THE GAME")
                        res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                        if res==False:
                            quit()
                        else:
                            reset()
                            
                else:
                    cl1.clear()
                    cl2.clear()

        
    #elif 2 player ##################################################################################################################################################################
    elif pc.get()==2:

        #CHECKS
        #check for invalid entries (c1)
        c1=True
        for i in li1:
            if i.get() in ['X', 'O', '']:
                pass
            else:
                i.delete(0,tk.END)
                tk.messagebox.showerror("ERROR", "INVALID ENTRY: ONLY 'X' or 'O' ALLOWED!")
                c1=False
                
        #check for extra entries / turn taken (c2)
        c2=True
        if c1==True: 
            co=co+1 
            for i in li1: 
                if i.get()!='':
                    if i not in Dch:
                        Dch.update({i:i.get()})
                        Sch=Sch+i.get() 

            if any(['OO' in Sch, 'XX' in Sch])==True:
                tk.messagebox.showerror("ERROR", "CANNOT TAKE TWO TURNS AT ONCE!")
                reset() #resetting the board
                
            if co<len(Sch): 
                tk.messagebox.showerror("ERROR", "CANNOT TAKE TWO TURNS AT ONCE!")
                reset() 
                c2=False 
            elif co>len(Sch):
                co=co-1
        else:
             c2=False

        #END OF GAME
        #check for completion 
        if c2==True:                                       
            cl1=[] #counter list 1
            cl2=[] #counter list 2
            for i in lq:
                for j in i:
                    if j.get()=='X':
                        cl1.append(True)
                    elif j.get()=='O':
                        cl2.append(False)
                    else:
                        cl1.clear()
                        cl2.clear()
                        
                if (len(cl1)==3) or (len(cl2)==3):
                    if cl1==[True, True, True]:
                        e10.insert(tk.END, "PLAYER 'X' HAS WON THE GAME")
                        res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                        if res==False:
                            quit()
                        else:
                            reset()
                            
                    elif cl2==[False, False, False]:
                        e10.insert(tk.END, "PLAYER 'O' HAS WON THE GAME")
                        res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                        if res==False:
                            quit()
                        else:
                            reset()
                            
                else:
                    cl1.clear()
                    cl2.clear()

        if c2==True:
            if all([e1.get()!='', e2.get()!='', e3.get()!='', e4.get()!='', e5.get()!='', e6.get()!='', e7.get()!='', e8.get()!='', e9.get()!='']):
                if e10.get()=='':
                    e10.insert(tk.END, "THIS GAME IS A TIE")
                    res=tk.messagebox.askyesno("GAME ENDED", "DO YOU WANT TO PLAY AGAIN")
                    if res==False:
                        quit()
                    else:
                        reset()
                        
b1=tk.Button(root, text=('CONFIRM'), command=press, padx=180, pady=12)
b1.grid(row=7,column=0,rowspan=None, columnspan=3)

#Imortant functions
def reset():
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)
    e3.delete(0,tk.END)
    e4.delete(0,tk.END)
    e5.delete(0,tk.END)
    e6.delete(0,tk.END)
    e7.delete(0,tk.END)
    e8.delete(0,tk.END)
    e9.delete(0,tk.END)
    e10.delete(0,tk.END)
    global co, Sch
    co=0
    Sch=''
    Dch.clear()

def inv(): #to access the opposite sign to the player
    if ps.get()=='X':
        return 'O'
    elif ps.get()=='O':
        return 'X'

def finder(): #return if we have a = one move win and b = return the corrusponding entry box
    Lch=[]
    a=False
    b=None
    for i in lq:
        for j in i:
            Lch.append(j.get())
        if any([[ps.get(), ps.get(),''] == Lch, [ps.get(), '', ps.get()] == Lch, ['', ps.get(), ps.get()] == Lch ]):
            a= True
            b=i[Lch.index('')]
            break
        elif any([[inv(), inv(), ''] == Lch, [inv(), '',  inv()] == Lch, ['', inv(), inv()] == Lch ]):
            a= True
            b=i[Lch.index('')]
            break
        else:
            Lch=[]
            continue
        
    return (a, b)

            
def union(L):
    l=[]
    for i in L:
        if i not in l:
            l.append(i)
    return l  

def inter(L1,L2):       
    l=[]
    for i in L1:
        if i in L2:
            l.append(i)
    return l

def minus(L,l):
    for i in l:
        if i in L:
            L.remove(i)
    return L 

def pref(L):            
    ml=inter(L,m)
    cl=inter(L,c)
    sl=inter(L,s)

    if ml!=[]:
        return ml+cl+sl
    elif cl!=[]:
        return ml+cl+sl
    elif sl!=[]:
        return ml+cl+sl
    else:
        return []

def join(L):
    l=[]
    for i in L:
        l.extend(i)
    return l

b2=tk.Button(root, text=('RESET'), command=reset, padx=20, pady=200)
b2.grid(row=4,column=3,rowspan=9, columnspan=None)

tk.mainloop()
