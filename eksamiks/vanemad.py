# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 14:08:34 2016

@author: Risto
Failis lapsed.txt on igal real vanema isikukood, tühik ja lapse isikukood.
 Failis nimed.txt on igal real ühe inimese isikukood, tühik ja tema nimi. 
 Võib eeldada, et korduvaid nimesid failis ei esine. Võib eeldada, et iga
 failis lapsed.txt oleva isikukoodi jaoks on failis nimed.txt välja toodud
 vastav nimi.

Kirjuta programm, mis väljastab ekraanile iga lapsevanema kohta ühe rea: 
tema nimi, koolon, tühik ning seejärel komade ja tühikutega eraldatuna 
tema laste nimed.
Põhitöö tuleks delegeerida funktsioonile seosta_lapsed_ja_vanemad, 
mis võtab argumentideks laste faili nime ja nimede faili nime, ning 
tagastab sõnastiku, kus kirje võtmeks on lapsevanema nimi ja väärtuseks
 tema laste nimede hulk. 
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\eksamiks")



flapsed=input("Sisestage failinimi: ")
f = open(flapsed,  encoding="UTF-8")
andmed = f.readlines()
abimuutuja=[]
tulem=[]
for rida in andmed:
    abimuutuja=rida.strip().split(' ')
    tulem.append(abimuutuja)

def andmed_sisse(failinimi):
    f = open(failinimi,  encoding="UTF-8")
    andmed = f.readlines()
    abimuutuja=[]
    tulem=[]
    for rida in andmed:
        abimuutuja=rida.strip().split(' ')
        tulem.append(abimuutuja)
    return tulem
    
lapsed=andmed_sisse('lapsed.txt')    
nimed=andmed_sisse('nimed.txt')

    
vanem=[]
for i in range(len(nimed)):
    vanem.append(nimed[i][0])

vanemnimi=[]
for i in range(len(vanem)):
    ik=vanem[i]
    for j in range(len(nimed)):
        if ik==nimed[j][0]:
            vanemnimi.append(nimed[j][1]+' '+nimed[j][2])
            
vanemaLapsed=[]
for i in range(len(vanem)):
    lapsik=[]
    for j in range(len(lapsed)):
            if vanem[i]==lapsed[j][0]:
                lapsik.append(lapsed[j][1])
    vanemaLapsed.append(lapsik)
    
tulem=[]
for i in range(len(vanemaLapsed)):
    lapsenimed=[]
    for j in range(len(vanemaLapsed[i])):
        lapseid=vanemaLapsed[i][j]
        for k in range(len(nimed)):
            if nimed[k][0]==lapseid:
                lapsenimed.append(nimed[k][1]+' '+nimed[k][2])
    tulem.append(lapsenimed)

sonastik={}
for i in range(len(vanemnimi)):
    if len(tulem[i])!=0:
        sonastik[vanemnimi[i]]=set(tulem[i])



def seosta_lapsed_ja_vanemad(lapsedtxt,nimedtxt):
    lapsed=andmed_sisse(lapsedtxt)  
    nimed=andmed_sisse(nimedtxt)
    vanem=[]
    for i in range(len(nimed)):
        vanem.append(nimed[i][0])
    vanemnimi=[]
    for i in range(len(vanem)):
        ik=vanem[i]
        for j in range(len(nimed)):
            if ik==nimed[j][0]:
                vanemnimi.append(nimed[j][1]+' '+nimed[j][2])
    vanemaLapsed=[]
    for i in range(len(vanem)):
        lapsik=[]
        for j in range(len(lapsed)):
            if vanem[i]==lapsed[j][0]:
                lapsik.append(lapsed[j][1])
        vanemaLapsed.append(lapsik)
    
    tulem=[]
    for i in range(len(vanemaLapsed)):
        lapsenimed=[]
        for j in range(len(vanemaLapsed[i])):
            lapseid=vanemaLapsed[i][j]
            for k in range(len(nimed)):
                if nimed[k][0]==lapseid:
                    lapsenimed.append(nimed[k][1]+' '+nimed[k][2])
        tulem.append(lapsenimed)
        
    sonastik={}
    for i in range(len(vanemnimi)):
        if len(tulem[i])!=0:
            sonastik[vanemnimi[i]]=set(tulem[i])
    return sonastik

sonast=seosta_lapsed_ja_vanemad('lapsed.txt', 'nimed.txt')

for i in sonast.keys():
    print(i, sonast[i])
    