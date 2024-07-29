import tkinter as tk

root=tk.Tk()
root.eval("tk::PlaceWindow %s center" % root.winfo_toplevel())
root.title("CHEEMGLISH TRASNLATOR")

l0=tk.Label(root, text='Hemlo my name is cheems, I am your tramslamtor')
l0.grid(row=0, column=0, columnspan=3)

l1=tk.Label(root, text='Enter text here :')
l1.grid(row=1, column=0, columnspan=1)

e1=tk.Entry(root, justify='left', width=30)
e1.grid(row=1, column=1, columnspan=2)

e2=tk.Entry(root, justify='left', width=45)
e2.grid(row=2, column=0, columnspan=3)

def cheem():
    s=e1.get()
    if any([("mn" in s), ("am" in s), ('em' in s), ('im' in s), ('om' in s), ('um' in s)]):
        e2.delete(0, tk.END)
        e2.insert(tk.END, s+" hue hue hue")

    elif ("n" in s):
        s=s.replace("n", "m")
        e2.delete(0, tk.END)
        e2.insert(tk.END, s)
        
    elif any([('a' in s), ('e' in s), ('i' in s), ('o' in s), ('u' in s)]):
        if ('a' in s):
            s.find('a')
            s=s[:s.find('a')+1]+"m"+s[s.find('a')+1:]
            e2.delete(0, tk.END)
            e2.insert(tk.END, s)
        elif ('e' in s):
            s.find('e')
            s=s[:s.find('e')+1]+"m"+s[s.find('e')+1:]
            e2.delete(0, tk.END)
            e2.insert(tk.END, s)
        elif ('i' in s):
            s.find('i')
            s=s[:s.find('i')+1]+"m"+s[s.find('i')+1:]
            e2.delete(0, tk.END)
            e2.insert(tk.END, s)
        elif ('o' in s):
            s.find('o')
            s=s[:s.find('o')+1]+"m"+s[s.find('o')+1:]
            e2.delete(0, tk.END)
            e2.insert(tk.END, s)
        elif ('u' in s):
            s.find('u')
            s=s[:s.find('u')+1]+"m"+s[s.find('u')+1:]
            e2.delete(0, tk.END)
            e2.insert(tk.END, s)

    if ("?" in s):
        s="Kya matlab "+s
        e2.delete(0, tk.END)
        e2.insert(tk.END, s)
    
b=tk.Button(root, text='EMTER', command=cheem, padx=110)
b.grid(row=3, column=0, columnspan=3)
