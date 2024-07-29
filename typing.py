import time
import pandas as pd
def check(x,y):
    v=''
    s=''
    for i in range(len(x)):
        if x[i]==y[i]:
            v=x[i]
        else:
            v=' '+x[i].upper()+' '
        s=s+v
    if str(x)==str(y):
        return ("NULL")
    else:
        return s
def acc(x,y):
    n=0
    for i in range(len(x)):
        if x[i]==y[i]:
            continue
        else:
            n=n+1
    return ((len(x)-n)/len(x))*100
def proc(x):
    x1=x.lower()
    x2=''
    for i in range(len(x1)):
        if x1[i] in ['.',
                     ',',
                     '?',
                     ' " ',
                     '-',
                     '_',
                     " ' ",
                     ' ’ ',
                     ' “ ',
                     '<',
                     ">",
                     ' ” ']:
            pass
        else:
            x2=x2+x1[i]
    return x2
while True:
    try:
        while True:
            t1=input("Enter text to be typed: ")
            t=proc(t1)
            print("")
            print(t)
            print("")
            a=input("Hit the 'ENTER' key to START")
            print("")
            print("-------------START--------------")

            t1=time.time()
            b=input("")
            t2=time.time()

            D={"Total characters typed: ":len(b) ,'Keystrokes/Min: ':str(len(b)*60/(t2-t1))+' KpM', 'Words/minut: ':str((len(b)/5)*60/(t2-t1))+' WpM', 'Your mistakes: ':str(check(t,b)),
               'Accurate keystrokes/sec: ':str((len(t)*acc(t,b)/100)/(t2-t1)), 'time taken: ':str(t2-t1)+' s'}
            DF=pd.Series(D)
            print("________REPORT________")
            print(DF)
            print('')
            print("________REPORT________")
            print("Total characters typed: "+str(len(b)))
            print('Keystrokes/Min: '+str(len(b)*60/(t2-t1))+' KpM')
            print('Words/minut: '+str((len(b)/5)*60/(t2-t1))+' WpM')
            print('Your mistakes: '+str(check(t,b)))
            print('Your accuracy: '+str(acc(t,b))+"%")
            print('Accurate keystrokes/sec: '+str((len(t)*acc(t,b)/100)/(t2-t1)))
            print('time taken: '+str(t2-t1)+' s')
            print("")
    except:
        print("-------------------AN ERROR OCCURED-------------------")
