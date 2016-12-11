# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:13:37 2016

@author: Risto
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\III nädal")

#eksam 6 või 20 jaanuaril, andmebaasid on 19 jaanuaril eksam

def faktoriaalRek(n):
    if n==0:
        return 1
    else:
        return n*faktoriaalRek(n-1)

faktoriaalRek(3)

def rfun(n):
    if n==0:
        return 0
    return 1+rfun(n-1)

print(rfun(3))

def rfun(n):
    if n==0:
        return 0
    return 2+rfun(n-1)
    
print(rfun(3))

def rfun(n):
    if n==0:
        return 0
    return rfun(n-1)
    
print(rfun(3))


def printAlla(n):
    if n<=0:
        print("Stop")
    else:
        print(n)
        printAlla(n-1)

printAlla(7)
#tagurpidi prindib
def printAlla(n):
    if n<=0:
        print("Stop")
    else:
        printAlla(n-1)        
        print(n)
printAlla(7)       
#alla ja üles        
def printAlla(n):
    if n<=0:
        print("Stop")
    else:
        print(n)
        printAlla(n-1)
        print(n)
printAlla(7) 
#puurekursioon
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibonacci(8)

def rekFun(x,y):
    if x==0:
        return y
    elif x<0:
        return rekFun(x+1,y-2)
    else:
        return rekFun(x-1, y+2)

rekFun(-6,0)

#sabarekursioon

#andmesutruktuurid
#järjend (list) [2,3,4,-1], saab elemente panna juurde ja eemaldada ja 
#anda uusi väärtusi.
c=[1,2,3]
a=["Tere",1,c]
e=[] #tühi list

#ennik, ei saa elemente lisad/eemaldada ja anda uusi väärtusi 
#sama mis korteez, tuple. kasutatakse kuna pythonis on osa
#funktsioone selle jaoks optimeeritd
b=(1,2,3,45)
b[1]
b[9]
b[1]=2#annab errori
list(b)
tuple(a)

#hulkon mittekorduvate järjestamate elementidega andmestruktuur. võib olla
#muteeritav (set) ja mittemuteeritav (frozenset). ei saa ükskut
#elementi indeksiga välja võtta kuna pole järjekorda
h1={8,1,3,6,7}
h1={8,1,3,6,7,7}#7 saab olla ühe korra, üks "kaob2 ära
h2=set([6,4,5])

for element in h2:#nii saab üksiku elemendi kätte
    print(element)

6 in h2
10 in h2
10 not in h2

h3={6,5,4,4}
h3==h2

#on range alamhulk
h3<h2
h4={6,4}
h4<h2
#mitterange alamhulk
h3<=h2
#sama ka ülemhulkadega
#ühisosa
h4&h2
#ühend
h4|h2
{4,5,6}|{1,2,3}&{4,5,6}
#ühisosa võtmine on korrutamine (tähtsam) ja ühendi võtmine on liitmine
{1,2,3}|{4,5,6}&{7,8,9}
#vahe
{8,-6,6}-{8,-6}
#sümmetirline vahe
{8,-6,6}^{8,-6}

h4.add(12)
h4

print(h4.pop())
h4
#sõne, fikseeritud, mittemuteeritav

#sõnastik










         