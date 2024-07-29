import random
import math


a=random.randint(1,9)
b=random.randint(0,9)
c=random.randint(0,9)
d=random.randint(0,9)

l=(a*1000)+(b*100)+(c*10)+(d)

print("",l)

k=int(input("Guess the four digit code(Tries left:4):\n"))

p=math.floor(k/1000)
q=math.floor(k/100)-(10*p)
r=math.floor(k/10)-(100*p)-(10*q)
s=k-(1000*p)-(100*q)-(10*r)

if k == l:
    print("You cracked the code!")
else:
 if math.floor(k/1000) == math.floor(l/1000):
     print(str(p)+" is correctly placed")
 elif p == a:
     print(str(p)+" is correct")
 elif p == b:
     print(str(p)+" is correct")
 elif p == c:
     print(str(p)+" is correct")
 elif p == d:
     print(str(p)+" is correct")
    
 if math.floor(k/100)-(10*p) == math.floor(l/100)-(10*a):
     print(str(q)+" is correctly placed")
 elif q == a:
     print(str(q)+" is correct")
 elif q == b:
     print(str(q)+" is correct")
 elif q == c:
     print(str(q)+" is correct")
 elif q == d:
     print(str(q)+" is correct")

 if math.floor(k/10)-(100*p)-(10*q) == math.floor(l/10)-(100*a)-(10*b):
     print(str(r)+" is correctly placed")
 elif r == a:
     print(str(r)+" is correct")
 elif r == b:
     print(str(r)+" is correct")
 elif r == c:
     print(str(r)+" is correct")
 elif r == d:
     print(str(r)+" is correct")

 if k-(1000*p)-(100*q)-(10*r) == l-(1000*a)-(100*b)-(10*c):
     print (str(s)+" is correctly placed")
 elif s == a:
     print(str(s)+" is correct")
 elif s == b:
     print(str(s)+" is correct")
 elif s == c:
     print(str(s)+" is correct")
 elif s == d:
     print(str(s)+" is correct")#try 1 end



 k1=int(input("Tries left:3\n"))

 p1=math.floor(k1/1000)
 q1=math.floor(k1/100)-(10*p1)
 r1=math.floor(k1/10)-(100*p1)-(10*q1)
 s1=k1-(1000*p1)-(100*q1)-(10*r1)

 if k1 == l:
     print("you cracked the code")
 else:
     if math.floor(k1/1000) == math.floor(l/1000):
         print(str(p1)+" is correctly placed")
     elif p1 == a:
         print(str(p1)+" is correctly placed")
     elif p1 == b:
         print(str(p1)+" is correctly placed")
     elif p1 == c:
         print(str(p1)+" is correctly placed")
     elif p1 == c:
         print(str(p1)+" is correctly placed")

     if math.floor(k1/100)-(10*p1) == math.floor(l/100)-(10*a):
         print(str(q1)+"  is correctly placed")
     elif q1 == a:
         print(str(q1)+" is correct")
     elif q1 == b:
         print(str(q1)+" is correct")
     elif q1 == c:
         print(str(q1)+" is correct")
     elif q1 == d:
         print(str(q1)+" is correct")

     if math.floor(k1/100)-(10*p1) == math.floor(l/100)-(10*a):
         print(str(q1)+"  is correctly placed")
     elif r1 == a:
         print(str(q1)+" is correct")
     elif r1 == b:
         print(str(q1)+" is correct")
     elif r1 == c:
         print(str(q1)+" is correct")
     elif r1 == d:
         print(str(q1)+" is correct")

     if math.floor(k1/100)-(10*p1) == math.floor(l/100)-(10*a):
         print(str(q1)+"  is correctly placed")
     elif s1 == a:
         print(str(q1)+" is correct")
     elif s1 == b:
         print(str(q1)+" is correct")
     elif s1 == c:
         print(str(q1)+" is correct")
     elif s1 == d:
         print(str(q1)+" is correct")



     k3=int(input("Tries left:2\n"))

     p3=math.floor(k3/1000)
     q3=math.floor(k3/100)-(10*p3)
     r3=math.floor(k3/10)-(100*p3)-(10*q3)
     s3=k3-(1000*p3)-(100*q3)-(10*r3)        

     if k3 == l:
         print("You cracked the code")
     else:
         if math.floor(k3/1000) == math.floor(l/1000):
             print(str(p3)+" is correctly placed")
         elif p3 == a:
             print(str(p3)+" is correctly placed")
         elif p3 == a:
             print(str(p3)+" is correctly placed")
         elif p3 == a:
             print(str(p3)+" is correctly placed")
         elif p3 == a:
             print(str(p3)+" is correctly placed")

         if math.floor(k3/100)-(10*p3) == math.floor(l/100)-(10*a):
             print(str(q3)+" is correctly placed")
         elif q3 == a:
             print(str(q3)+" is correct")
         elif q3 == b:
             print(str(q3)+" is correct")
         elif q3 == c:
             print(str(q3)+" is correct")
         elif q3 == d:
             print(str(q3)+" is correct")

         if math.floor(k3/10)-(100*p3)-(10*q3) == math.floor(l/100)-(100*a)-(10*b):
             print(str(r3)+" is correctly placed")
         elif r3 == a:
             print(str(r3)+" is correct")
         elif r3 == b:
             print(str(r3)+" is correct")
         elif r3 == c:
             print(str(r3)+" is correct")
         elif r3 == d:
             print(str(r3)+" is correct")

         if k3-(1000*p3)-(100*q3)-(10*r3) == l-(1000*a)-(100*b)-(10*c):
             print (str(s3)+" is correctly placed")
         elif s3 == a:
             print(str(s3)+" is correct")
         elif s3 == b:
             print(str(s3)+" is correct")
         elif s3 == c:
             print(str(s3)+" is correct")
         elif s3 == d:
             print(str(s3)+" is correct")    

                 
                     
         





     
