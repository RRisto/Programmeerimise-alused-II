# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:54:03 2016

@author: Risto
"""

def fua(x):
    return x-1

def fub(x):
    return x*x
    
fua(fub(2))>fub(fua(2))
fua(fub(2))<fub(fua(2))

#mis väljastatkase ekraanile? midagi muud VIGA!!!
linn="Tartu"
for i in range(1,4):
    print(linn[i]+linn[-i])
    
värv="sinine"
värvid=["must","valge",värv]
print(max(värvid))

järjend=[1,-1,1,4]
print(järjend[järjend[1]])


def keskmine(arv1,arv2):
    k=arv1 + arv2/2
    return k

print(keskmine(1,3))