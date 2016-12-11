# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 07:45:28 2016

@author: Risto
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimine")

a=[1,5,8]
b=[1,34,4.6]
print(a[0])
print(b[2])
b[2]=1632
print(b[2])


a=[1,3,5,6]
b=a
print(b[1])
#muutub ka b!!! listis muudab
a=[1,3,5,6]
b=a
a[1]=7
print(b[1])
#nüüd b muutus ja ka a muutus!!!
b[1]=6
print(b[1])
print(a[1])

a=5
b=a
print(b)
#nüüd ei muuda (teine andmetüüp)
a=5
b=a
b=7
print(a)

###kahemõõtmeline järjend
a=[[1,3,4],[2,4,5]]
print(a[1])
print(a[1][2])
print(len(a))
print(len(a[0]))

for i in range(len(a)):
    print(a[i])

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j])
    print("\n")

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="hafa")
    print("\n")
    
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print("\n")
    

b = [1, 9, 1, 8]
korrutis = 1
for i in range(len(b)):
    korrutis *= i
    print(i)
print(korrutis)


























