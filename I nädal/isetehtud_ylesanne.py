# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:51:50 2016

@author: Risto
"""
import random
#funktsioon, mis loob bingo tabeli
def bingotabel():
    alglist=[]
    algus=1
    lopp=16
    rida=[]
    for i in range(5):
        alglist=alglist+random.sample(range(algus,lopp,1),5)
        algus+=15
        lopp+=15
        
    bingo=[]
    for i in range(5):
        rida=[]
        for j in range(5):
            rida.append(alglist[j*5+i])
        bingo.append(rida)
    
    return bingo
#kasutamise näide   
bingotabel()