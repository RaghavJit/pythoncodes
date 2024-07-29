import random
L1=["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","9","4","7"]
L2=["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
L3=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","5","6","8","0","/","^","#","%","?"]
L4=["1","2","3","4","5","6","7","8","9","0"]
L5=["$","-","#",")","3","/","?","R"]
print("Seciurty levels")
print("Max, Med, Min")
while True:
    enter=input("Choose level of secuirty:\n")
    if enter==("Max"):
       a1=random.choice(L1)

       a2=random.choice(L5)

       a3=random.choice(L3)

       a4=random.choice(L4)

       a5=random.choice(L5)

       a6=random.choice(L3)

       a7=random.choice(L4)

       a8=random.choice(L1)
       print("Here's a password for you:",a1+a2+a3+a4+a5+a6+a7+a8)
    elif enter==("Med"):
        a1=random.choice(L1)

        a2=random.choice(L5)

        a3=random.choice(L3)

        a4=random.choice(L4)

        a5=random.choice(L5)

        a6=random.choice(L3)
        print("Here's a password for you:",a1+a2+a3+a4+a5+a6)
    elif enter==("Min"):
        a1=random.choice(L1)

        a2=random.choice(L5)

        a3=random.choice(L3)

        a4=random.choice(L4)
        print("Here's a password for you:",a1+a2+a3+a4)
    else:
        print("No other options avaible")
