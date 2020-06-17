"""
author: Susan Margevich
file name: farmerEddie.py
plays Farmer Eddie Game
"""

from myList import *
from random import *

def readFile(file):
    """
    reads input file
    returns two separate linked lists
    """
    list1=createList()
    list2=createList()
    currentlist=list1
    for line in open(file):
        line=line.strip()
        if line == '':
            currentlist=list2
        else:
            append(currentlist, line)
    return list1,list2

def spin(lst, spinNumb):
    """
    generates print statement and spinning wheel
    """
    spin = createSpin(lst)
    printState ='Spin '+ str(spinNumb)+ ':' + lst.cursor.data
    while spin >0:
        printState=printState+ ' -> '+ next(lst)
        spin -=1
    return printState

def Game(lst1,lst2):
    """
    uses spinWheel function to play game
    """
    spinNumb = 1
    Current = lst1
    while True:
        print(spin(Current, spinNumb))
        if Current.cursor.data == 'Switch':
            print('-----Switching Wheels-----')
            if Current == lst1:
                Current = lst2
            else:
                Current = lst1
        elif Current.cursor.data != 'Switch':
            Current.cursor.landed += 1
            if Current.cursor.landed == 3:
                print(Current.cursor.data, ' won!')
                break
        spinNumb +=1

def main():
    (list1, list2) = readFile(input('Enter a file for names of animals on the wheels: '))
    intSeed = int(input('Enter a seed for the random number generator: '))
    seed(intSeed)
    Game(list1, list2)

main()