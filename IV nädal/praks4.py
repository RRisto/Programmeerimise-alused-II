# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 13:40:07 2016

@author: Risto
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\IV nädal")
#annab errori, peab objekti dictionaryks
a={}
a.add(2)
print(a)
#ühte ja sama võtit saab olla ainult üks

hääli={'Andrus':12900,'Indrek':14000, 'Marju':19000}
print(hääli)#prindib järjestuses
hääli['Tunne']=20000
for nimi in hääli:
    print(nimi+" "+str(hääli[nimi]))
    
for n, h in hääli.items():
    print(n,h)
    
print('Andrus' in hääli)
print(19000 in hääli)
print(hääli.keys())
#kustutab Andruse kirje
del hääli['Andrus']
print(hääli)

hääli={'Andrus':12900,'Indrek':14000, 'Marju':19000}
print(hääli.pop('Andrus'))
print(hääli)

hääli1={'Andrus':12900,'Indrek':14000, 'Marju':19000}
hääli2={'Andrus':13900,'Indrek':14000, 'Marju':19000}

hääli1==hääli2
hääli1+hääli2#error

d={2:1,3:1}
d[1]=1#siin [1] viitab key väärtusele 1!!!
print(d)

d[2]=7
print(d)

j=[1,6,7,4,2,9]
j[20]=3

d.append(5)
#annab errori kuna loobis d pikkus hakkab muutuma
for võti in d:
    print(d.pop[võti])
#####, alias, töötab listi puhul
a=[1,3,5]
b=a
b[1]=7
print(a[1])
#teine struktuur, siin ei muutu
a=5
b=a
b=7
print(a)

a=7
id(a)#annab midagi mis on mäluaadress (mitte päris, kuid enam vähem)
b=7
id(b)#sama mis a puhul
c=[1,4,7]
id(c)
d=c
id(d)

e=[6,9,0]
id(e)
#koopia
a=[2,4,6]
b=a[:]#koopia!!! o isesiesev
b.append(7)
print(b)
print(a)











