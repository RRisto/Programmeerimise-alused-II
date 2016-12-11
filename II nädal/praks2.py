# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 13:43:39 2016

@author: Risto
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\II nädal")

t=True
print(not t)

#return - tagastab väärtuse
#print - väljastab väärtuse (nt ekraanile)
def tagastasumma(x,y):
    return x+y
tagastasumma(2,3)

def väljastasumma(x,y):
    print(x+y)
väljastasumma(2,3)

2+tagastasumma(2,3)
2+väljastasumma(2,3)#väljastab 5 ja veateate
print(väljastasumma(2,3))#väljastab 5 ja None
type(väljastasumma(2,3))#NoneType

tagastasumma(2, tagastasumma(3,4))
väljastasumma(2, väljastasumma(3,4))
tagastasumma(2,väljastasumma(3,4))

#csv failist allalaadimine
import csv as comsep

#rekursioon, alamprogramm=funktsioon, seotud fraktalitega
def rekFun(n):
    if n>0:
        print("E")
    else:
        print(n)
        rekFun(n+2)
        
rekFun(-7)
rekFun(7)

def rekFun(n):
    if n>0:
        print("E")
    else:
        print(n)
        rekFun(n-2)

rekFun(-7)#teooarias inf loop, praktikas rekursiooni sügavus määratud

def fun(n):
    print(n)
    fun(n-1)
fun(5)

#faktoriaal loopiga
def faktoriaalIter(n):
    fakt=1
    for i in range(1, n+1):
        fakt*=i
    return fakt

faktoriaalIter(4)
#faktoriaal rekursiooniga
def faktoriaalRek(n):
    if n==0:
        return 1
    else:
        return n*faktoriaalRek(n-1)
        
faktoriaalRek(4)
#vanasti tegelesid inimesed rekursiooniga rohkem

fail = open("RV0282sm.csv", encoding="UTF-8")
andmed = [[], []]
for rida in fail: # ridade kaupa
    osad = rida.split(";") # rea andmed järjendisse
    andmed[0].append(int(osad[2].strip('"')))
    andmed[1].append(int(osad[3]))
fail.close()

for i in range(len(andmed[0]) - 1):
    if andmed[1][i + 1] > andmed[1][i]:
        print(andmed[0][i])


####
def loenda(järjend, element):

    # tühjas järjendis ei saa seda elementi esineda
    # see on rekursiooni baas
    if len(järjend) == 0:
        return 0
    else:
        # rekursiooni samm
        # järjendi päiseks nimetame tema esimest elementi
        päis = järjend[0]
        # sabaks nimetame kõike seda, mis tuleb peale esimest elementi
        saba = järjend[1:]

        # kasutame sama funktsiooni rekursiivselt järjendi sabal ...
        elementide_arv_sabas = loenda(saba, element)

        # ... ja kombineerime saadud tulemuse päisest saadud infoga
        if päis == element:
            return elementide_arv_sabas + 1
        else:
            return elementide_arv_sabas

print(loenda("kukesupp", "u"))
print(loenda("kukesupp", "p"))
print(loenda("kukesupp", "r"))