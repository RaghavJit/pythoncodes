import tkinter

root=tkinter.Tk()
root.title=("TIC TAC TOE")

e1=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)

e2=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e3=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e4=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e5=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e6=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e7=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e8=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)
e9=tkinter.Entry(root,width=3,font=("ariel","20","bold"),bg="cyan",fg="black",justify="center",borderwidth=7)

e1.grid(row=2,column=1)
e2.grid(row=2,column=2)
e3.grid(row=2,column=3)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)
e6.grid(row=1,column=3)
e7.grid(row=0,column=1)
e8.grid(row=0,column=2)
e9.grid(row=0,column=3)


