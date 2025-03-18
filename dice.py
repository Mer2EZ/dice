# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 10:46:47 2025

@author: Mert
"""

import numpy.random as rand

def d20(i):
    return rand.randint(1,21,i)

def d12(i):
    return rand.randint(1,13,i)

def d10(i):
    return rand.randint(0,10,i)

def d100(i):
    return 10*d10(i)

def d8(i):
    return rand.randint(1,9,i)

def d6(i):
    return rand.randint(1,7,i)

def d4(i):
    return rand.randint(1,5,i)

menu="""
[20] - d20
[12] - d12
[10] - d10
[100] - d100
[8] - d8
[6] - d6
[4] - d4
[q] - quit
"""

inp=str(input("Enter '0' for start."))

while inp!='q':
    print(menu)
    inp=str(input("Choice: "))
    
    if inp=='q':
        print("Closing...")
        break
    
    num=int(input("Number of dice: "))
    
    if inp=='20':
        print(d20(num))
    elif inp=='12':
        print(d12(num))
    elif inp=='10':
        print(d10(num))
    elif inp=='100':
        print(d100(num))
    elif inp=='8':
        print(d8(num))
    elif inp=='6':
        print(d6(num))
    elif inp=='4':
        print(d4(num))
    else:
        print("error")