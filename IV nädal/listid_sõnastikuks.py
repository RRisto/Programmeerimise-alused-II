# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 20:24:09 2016

@author: risto.hinno
"""
"""Kirjuta funktsioon listid_sõnastikuks, mis võtab argumendiks kaks 
ühepikkust listi ning tagastab nende põhjal moodustatud sõnastiku, kus
 võtmeteks on esimese listi elemendid ja väärtusteks teise listi 
 vastavatel positsioonidel olevad elemendid. Kui võtmete listis 
 on korduvaid elemente, siis sõnastikku panna neist viimane koos 
 vastava elemendiga väärtuste listist."""
 
a=[1,34, 7, 34]
b=['abc', 'xyz','qqq','rrr']

def listid_sõnastikuks(a,b):
    a=list(reversed(a))
    b=list(reversed(b))
    abilist=[]
    eemalda=[]#indeksid elementidest, mis tuleb eemaldada
    for i in range(len(a)):
        if a[i] not in abilist:
            abilist.append(a[i])
        else:
            eemalda.append(i)
    a=list(abilist)
    b = [ item for i,item in enumerate(b) if i not in eemalda ]
    sonastik={}
    for i in range(len(a)):
        sonastik[a[i]] = b[i]
        
    return sonastik
    

#listid_sõnastikuks(a,b)   

