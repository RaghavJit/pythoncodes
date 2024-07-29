import tkinter
 

root=tkinter.Tk()
root.title("password")

e=tkinter.Entry(root,borderwidth=10,width=50,bg="cyan")
e.grid(row=1,column=0)

l1= tkinter.Label(root,text="Enter Password")
l1.grid(row=0,column=0)

def check():
    if e.get()==("1024"):
        label=tkinter.Label(root,text="WELCOME")
        label.grid(row=3,column=0)
    else:
        label=tkinter.Label(root,text="Wrong Password!")
        label.grid(row=2,column=0)


bt=tkinter.Button(root,text="Enter",command=check)
bt.grid(row=2,column=0)

root.mainloop()
