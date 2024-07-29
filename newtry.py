import random
r=random.randint(1,3)
s=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
s1=("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21")
s2={1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 11:11, 12:12, 13:13, 14:14, 15:15, 16:16, 17:17, 18:18, 19:19, 20:20, 21:21}
while True:
    x=str(input(""))
    if str(x) in str(s1):
        if x[-2]+x[-1]=="20":
            print("21...YOU WON!")
        elif x[-2]+x[-1] != "20":
            nmbr=str(x[-2]+x[-1])
            l=int(s2.get(nmbr.lstrip()))
            print(s[l:l+r])
    else:
        comment=random.choice["Invalid input", "Your entry is wrong", "ERROR"]
        print("",comment)


