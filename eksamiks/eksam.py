# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:22:48 2016

@author: Risto
Õppejõud koostas eksami, milles oli 7 ülesannet. Iga ülesande eest 
võis saada kuni 10 punkti. Eksami tulemused on kirjas failis eksam.txt.

Leiame iga tudengi eksamipunktide kogusumma.
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\eksamiks")


def andmed_sisse(failinimi):
    f = open(failinimi,  encoding="UTF-8")
    andmed = f.readlines()
    abimuutuja=[]
    tulem=[]
    for rida in andmed:
        abimuutuja=rida.strip().split(' ')
        tulem.append(abimuutuja)
    return tulem

def andmed_sisse2(failinimi):
    f = open(failinimi,  encoding="UTF-8")
    andmed = f.readlines()
    abimuutuja=[]
    tulem=[]
    for rida in andmed:
        abimuutuja=rida.split('|')
        abimuutuja=abimuutuja[1].strip().split(',')
        tulem.append(abimuutuja)
    return tulem
    
f = open('eksam.txt',  encoding="UTF-8")
andmed = f.readlines()
abimuutuja=[]
tulem=[]
for rida in andmed:
    abimuutuja=rida.split('  |')
    tulem.append(abimuutuja)

    
tulem=andmed_sisse('eksam.txt')
arvud=andmed_sisse2('eksam.txt')

nimed=[]
for i in range(len(tulem)):
    nimed.append(tulem[i][0]+' '+tulem[i][1])
hinded=[]
for i in range(len(arvud)):
    hinne=0
    for j in range(len(arvud[i])):
        hinne+=int(arvud[i][j])
    hinded.append(hinne)

        
    
    
    
    