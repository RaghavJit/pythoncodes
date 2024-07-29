import tkinter as tk

window=tk.Tk()
window.eval("tk::PlaceWindow %s center" % window.winfo_toplevel())
window.title("Trial")
#window.minsize(800,600)

e1=tk.Entry(window, justify='left', borderwidth=10, font=('Constantia', '15', 'bold'), bg='grey', fg='white', width='10')
e1.grid(row=0,column=0,rowspan=None,columnspan=None)

l1=tk.Label(window, text=('label'), width='10', bg='white', fg='black', font=('Constantia', '15', 'bold'))
l1.grid(row=1,column=0,rowspan=None,columnspan=None)

b1=tk.Button(window, text=('button'),  font=('Constantia', '15', 'bold'), padx=20, pady=20)
b1.grid(row=0, column=1,rowspan=2,columnspan=None)

radio=tk.StringVar()
def selection():
    e1.delete(0,tk.END)
    e1.insert(tk.END, radio.get())

r1=tk.Radiobutton(window, text=("opt1"), variable=radio, value='O',command=selection)
r1.grid(row=2,column=0,rowspan=None,columnspan=None)

r2=tk.Radiobutton(window, text=("opt2"), variable=radio, value='X',command=selection)
r2.grid(row=2,column=1,rowspan=None,columnspan=None)

ck1=tk.IntVar()
ck2=tk.IntVar()

c1=tk.Checkbutton(window, text=("   first  "), variable=ck1, onvalue=1, selectcolor='red', offvalue=0)
c2=tk.Checkbutton(window, text=("second"), variable=ck2, onvalue=1, offvalue=0)

c1.grid(row=3,column=0,rowspan=None,columnspan=None)
c2.grid(row=4,column=0,rowspan=None,columnspan=None)

lb1=tk.Listbox(window, bg="yellow", bd=4, height=5, width=10)
lb1.grid(row=5,column=0,rowspan=None,columnspan=None)
lb1.insert(1,'option1')
lb1.insert(2,'option2')
lb1.insert(3,'option3')
lb1.insert(4,'option4')
lb1.insert(5,'option5')

C=tk.Canvas(window, bg='blue', height=300, width=400)
coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=90, fill="red")


C.grid(row=3,column=1,rowspan=None,columnspan=None)
window.mainloop()
