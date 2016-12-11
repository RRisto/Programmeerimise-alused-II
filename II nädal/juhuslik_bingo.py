# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:54:50 2016

@author: Risto
"""

import random as random
#funktsioon, mis loob bingo tabeli
#def juhuslik_bingo():
#    alglist=[]
#    algus=1
#    lopp=16
#    rida=[]
#    for i in range(5):
#        alglist=alglist+random.sample(range(algus,lopp,1),5)
#        algus+=15
#        lopp+=15     
#    bingo=[]
#    for i in range(5):
#        rida=[]
#        for j in range(5):
#            rida.append(alglist[j*5+i])
#        bingo.append(rida)
#    
#    return bingo
#kasutamise näide   
#juhuslik_bingo()
def juhuslik_bingo():
    alglist=[]
    algus=1
    lopp=16
    for i in range(5):
        alglist.append(list(random.sample(range(algus,lopp,1),5)))
        algus+=15
        lopp+=15
    return list(map(list, zip(*alglist)))
    
    