import random

concent = input("Shell we start?")
if concent == ("Yes"):#ok
    concent2 = input("Would you start or me?\n")
    if concent2 == ("you"):#computer start
        start = str(input("1 2 3\n"))
        if start == ("4"):#choice 1(I)
            a121 = str(input("5 6\n"))#comp restriction c1(I)***
            if a121 == ("7") :#choice 1.2(I)
                a1211=str(input("8 9 10\n"))#comp rest.*****
                if a1211 == ("11"):#choice 1.2.1(I)
                    a12111=str(input("12\n"))
                    if a12111 == 13:#GAME END
                        print("YOU LOST!")
                    else:
                        print("You entered an invalid number")
                elif a1211 == ("11 12"):#choice 1.2.1(II)GAME END
                    print("13...YOU WON!")
                else:#choice 1.2.1(III)
                    print("You entered an invallid number")

            elif a121 ==("7 8"):#choice 1.2(II)
                a1212=str(input("9 10\n"))#comp rest.*****
                if a1212 == ("11"):
                    a12121=str(input("12"))
                    if a12121 == ("13"):
                        print("YOU LOST!")
                    else:
                        print("You entered an invalid number")

                elif a1212 == ("11 12"):
                    print("13...YOU WON!")

                elif a1212 == ("11 12 13"):
                    print("YOU LOST!")
                

            elif a121 ==("7 8 9"):#choice 1.2(III)
                a12131 = str(input("10 11 12\n"))#comp rest.*****
                if a12131 == ("13"):#choice 1.2.1 (I)GAME END
                    print("YOU LOST!")
                else:#choice 1.2.1(II)
                    print("You entered an invallid number")

            else:#choice 1.2(IV)
                print("You entered an invalid number")


        elif start == ("4 5"):#choice1(II)  
            a122 = str(input("6 7 8\n"))#comp rest. c1(II)***
            if a122 == ("9") :#choice 2.2(I)
                a1221=(input("10 11\n"))#comp rest.*****
                if a1221 == ("12"):#choice 2.2.1(I)
                    print("13...YOU WON!")
                elif a1221 == ("12 13"):#choice 2.2.1(II)
                    print("YOU LOST!")
                else:#choice 2.2.1(III)
                    print("You entered an invalid number")
                
            elif a122 == ("9 10"):#choice 2.2(II)
                a1222=str(input("11 12\n"))#compt rest.*****
                if a1222 == ("13"):#choice 2.2.1(I)
                    print("YOU LOST!")
                else:#choice 2.2.1(II)GAME END
                    print("You entered an invalid number")

            elif a122 == ("9 10 11"):#choice 2.2(III)
                a1221=input("12\n")
                if a1221 == ("13"):#choice 2.2.1(I)
                    print("YOU LOST!")
                else:
                    print("You entered an invalid number")

            else:
                print("You entered an invalid numner")


        elif start == ("4 5 6"):#choice1(III)
            a123 = str(input("7 8 9\n"))#comp rest. c1(III)***
            if a123 == ("10") :#choice 3.2(I)
                a1231=str(input("11 12\n"))#comp rest.*****
                if a1231 == ("13"):#choice 3.2.1(I)
                    print("YOU LOST")
                else:#choice 3.2.1(II)
                    ("You entered an invalid number")    

            elif a123 == ("10 11"):#choice 3.2(II)
                a1232=str(input("12\n"))#comp rest.*****
                if a1232 == ("13"):#choice 3.2.2(I)
                    print("YOU LOST")# GAME END
                else:
                    print("You entered an invalid number") 
                
            elif a123 == ("10 11 12"):#choice 3.2(III)
                print("13...YOU WON!")#comp rest.*****GAME END(you)

            else:
                print("You entered an invalid number")



        else:
            print("You entered an invalid number")




    elif concent2 == ("me"):#player start
        b1=input("Begin then\n")

        if b1 == ("1"):#choice 1(I)
            b11=int(input("2 3 4\n")#comp rest.*****
            if b11 = ("5"):#choice 1.1(I)
                b11=int(input("6 7 8\n"))#comp rest.*****
                if b111==("9"):#choice 1.1.1(I)
                    b1111=int(input("10 11 12"))
                    if b1111 == ("13"):
                        print("YOU LOST")#comp win*****
                    else:
                        print("You entered an invalid number")
                elif b111==("9 10"):#choice 1.1.1(II)
                    b1112=int(input("11"))
                    if b1112==("12"):
                        print("13...YOU WON!")
                    elif b1112==("12 13"):
                        print("YOU LOST")
                    else:
                        print("You entered an invalid number")
                    print("13...YOU WON!")
                elif b111==("9 10 11"):#choice 1.1.1(III)
                    b1113=int(input("12"))
                    if b1113==("13"):
                        print("YOU LOST!")
                    else:
                        print("You entered an invalid number")
                else:
                    print("You entered an invalid number")
            elif b11 ==("5 6"):#choice 1.1(II)
                b112=int(input("7 8\n"))#comp rest.*****
                    if b112==("9"):#choice 1.1.2(I)
                        b1121=int(input("10 11 12"))
                        if b1121==("13"):
                            print("YOUU LOST")
                        else:
                            print("You entered an invalid number")
                    elif b112==("9 10"):#choice 1.1.2(II)
                        b1122=int(input("11"))
                        if b1122==("12"):
                            print("13...YOU WON!")
                        elif b1122==("12 13"):
                            print("YOU LOST")
                        else:
                            print("You entered an invalid number")
                    elif b112==("9 10 11"):#choice 1.1.2(III)
                        b1123==int(input("12"))
                        if b1123==("13"):
                            print("YOU LOST")
                        else:
                            print("You entered an invalid number")
                    else:
                        print("You entered an invalid number")
            elif b11==("5 6 7"):#choice 1.1(III)
                b113=int(input("8 9\n")#comp rest.*****
                    if b113==("10"):
                        b1131=int(input("11 12"))
                        if b1131 ==("13"):
                            print("YOU LOST")
                         else:
                             print("You entered an invalid number")
                    elif b113==("10 11"):
                        b1132=int(input("12"))
                        if b1132==("13"):
                            print("YOU LOST")
                        else:
                            print("You entered an invalid number")

                    elif b113=("10 11 12"):
                        b1133=
                    else:
                        print("You entered an invalid number")
            else:
                print("You entered an invalid number")

        elif b1== ("1 2"):#choice 1(II)
            b12=int(input("3 4\n"))#comp rest.*****
            if b12==("5"):#choice 1.2(I)
                b121=int(input("6 7 8\n"))
                if b121==("9"):#choice 1.1.3(I)
                    b1211=int(input("10\n"))
                    if b1211==("11"):
                        b1211x=int(input("12\n"))
                        if b1211x==("13"):
                            print("YOU LOST")
                        else:
                            print("You entered an invalid number")
                    elif b1211==("11 12"):
                        print("13...YOU WON!")
                    elif b1211==("11 12 13"):
                        print("YOU LOST")
                    else:
                        print("You entered an invalid number")
                        
                elif b121==("9 10"):#choice 1.1.3(II)
                    b1212=int(input("11 12"))#comp rest.*****
                    if b1212==("13"):
                        print("YOU LOST!")
                    else:
                        print("You entered an invalid number")
                elif b121==("9 10 11"):#choice 1.1.3(III)
                    b1213=int(input("12"))
                    if b1213==("13"):
                        print("YOU LOST")
                    else:
                        print("You entered an invalid number")
                else:
                    print("You entered an invalid number")
            elif b12 ==("5 6"):#choice 1.2(II)
                b122=int(input("7\n"))#comp rest.*****
                if b122==("8"):#choice 1.2.1(I)
                    b1221=int(input("9 10 11"))
                    if b1221==("12"):
                        print("13...YOU WON!")
                    else:
                        print("You entered an invalid number")
                elif b122==("8 9"):
                    b1222=int(input("10"))
                    if b1222==("11"):
                        b122cx==int(input("12"))
                        print("13...YOU LOST!")
                elif b122==("8 9 10"):
                else:
                    print("You entered an invalid number")
                
            elif b12 ==("5 6 7"):#choice 1.2(III)
                b123=int(input("8 9\n")
            else:
                print("You entered an invalid number")

        elif b1== ("1 2 3"):#choice 1(III)
            b13=int(input("4 5 6"))#comp rest.*****
            if b13 == ("7")#choice 1.3(I)
            elif b13==("7 8")#choice 1.3(II)
            elif b13==("7 8 9")#choice 1.3(III)
            else:
                print("You entered an invalid number")
        else:#choice 1(X)
            print("You entered an invalid number")
        

    else:#concent else
        print("I didn't get that.")



else:#player mode else.
    print("No other options avalable.")

    
