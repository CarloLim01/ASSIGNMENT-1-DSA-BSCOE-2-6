# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*).

import time 

def asterisk():
    str1 = "CARLO"
    printC = [[" " for i in range (5)] for j in range (5)]
    printA = [[" " for i in range (5)] for j in range (5)]
    printR = [[" " for i in range (5)] for j in range (5)]
    printL = [[" " for i in range (5)] for j in range (5)]
    printO = [[" " for i in range (5)] for j in range (5)]

    #LETTER C
    time.sleep(2)
    for i in range (5):
        for j in range (5):
            if (j==0) or ((i==0 or i==4) and (j>0)):
                printC[i][j] = "\033[1;35;1m*\033[0m"

    #LETTER A
    for i in range (5):
        for j in range (5):
            if ((j==0 or j==4) and i!=0) or (i==0 or i==2) and (j>0 and j<4):
                printA[i][j] = "\033[1;35;1m*\033[0m"

    #LETTER R
    for i in range (5):
        for j in range (5):
            if j==0 or (j==4 and (i!=0 and i!=2)) or ((i==0 or i==2) and (j>0 and j<4)):
                printR[i][j] = "\033[1;35;1m*\033[0m"

    #LETTER L
    for i in range (5):
        for j in range (5):
            if j==0 or (i==4 and j>0):
                printL[i][j] = "\033[1;35;1m*\033[0m"

    #LETTER O
    for i in range (5):
        for j in range (5):
            if ((j==0 or j==4) and (i!=0 and i!=4)) or ((i==0 or i==4) and (j>0 and j<4)):
                printO[i][j] = "\033[1;35;1m*\033[0m"

    for i in range(5):
        for j in range(5):
            print(printC[i] [j],end=" ")
        print(end="  ")
        for j in range(5):
            print(printA[i] [j],end=" ")
        print(end="   ")
        for j in range(5):
            print(printR[i] [j],end=" ")
        print(end="  ")
        for j in range(5):
            print(printL[i] [j],end=" ")
        print(end="  ")
        for j in range(5):
            print(printO[i] [j],end=" ")
        print()

def start():
    time.sleep(1)
    print("\t\t\033[1;37;1m   >>> MY NICKNAME IS <<<\033[0m\n\n")

def end():
    time.sleep(1)
    print("\n\n\t\t\033[1;37;1m     >>> THANKYOU <<<\033[0m")

def menu():
    start()
    asterisk()
    end()
    print("\n\n")

menu()