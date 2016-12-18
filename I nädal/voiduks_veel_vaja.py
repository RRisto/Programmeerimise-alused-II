# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:06:41 2016

@author: Risto
Järgnevatele funktsioonidele antakse argumendiks 5 x 5 tabel, milles iga element on kas täisarv lõigust 1 - 75 või täht X. Täht X sümboliseerib seda, et vastav arv on juba loositud.

1. Koostada funktsioon nurkademänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud mänguväli võidaks nurkademängu.

2. Koostada funktsioon diagonaalidemänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud mänguväli võidaks diagonaalidemängu.

3. Koostada funktsioon täismänguks_vaja, mis tagastab järjendi arvudest, mida on veel vaja loosida selleks, et antud mänguväli võidaks täismängu.
"""

#from os import chdir
#chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\I nädal")

def nurkademänguks_vaja(tabel):
    nurgad=[]
    for i in range(0,len(tabel), 4):
        for j in range(0,len(tabel[i]),4):
            if (tabel[i][j]!="X"):
                nurgad.append(tabel[i][j])
    return nurgad

tabel=[[1,30,34,55,75],[10,16,40,50,67],[5,20,38,48,61],[4,26,43,49,70],[15,17,33,51,66]]
#tabel=[[1,30,34,55,76],[10,16,40,50,67],[5,20,38,48,61],[4,26,43,49,70],[15,17,33,51,66]]
#tabel=[["X","X","X","X","X"],["X","X","X","X","X"],["X","X","X","X","X"],["X","X","X","X","X"],["X","X","X","X","X"]]
tabel=[[6, 28, 41, 55, 64], [13, 23, 'X', 56, 'X'], ['X', 'X', 31, 'X', 'X'], [3, 'X', 'X', 51, 66], [4, 18, 'X', 'X', 62]]
#nurkademänguks_vaja(tabel)

def diagonaalidemänguks_vaja(tabel):
    tulem=[]
    vasak=4
    for i in range(0,len(tabel)):
        if (tabel[i][i]!="X"):
                tulem.append(tabel[i][i])
        if (tabel[i][i+(vasak-i)]!="X" and (i+(vasak-i))!=i):
        #if (tabel[i][i+(vasak-i)]!="X"):
                    tulem.append(tabel[i][i+(vasak-i)])
        vasak-=1
    return tulem
    #xdiag=[]
    #ydiag=[]
    #for i in range(0,len(tabel)):
    #    if (tabel[i][i]!="X"):
    #            xdiag.append(tabel[i][i])
    #for i in range(len(tabel)):
    #    if (tabel[i][4-i]!="X"):
    #            ydiag.append(tabel[i][4-i])
    #return list(set(xdiag+ydiag))
diagonaalidemänguks_vaja(tabel)
   

        
def täismänguks_vaja(tabel):
    puuduvad=[]
    for i in range(len(tabel)):
        for j in range(len(tabel)):
            if (tabel[i][j]!="X"):
                puuduvad.append(tabel[i][j])
    return puuduvad
        
#täismänguks_vaja(tabel)



