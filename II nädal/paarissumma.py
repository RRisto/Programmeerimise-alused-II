# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:22:19 2016

@author: Risto
"""
#a=10
def paarissumma(a):
    if a%2!=0:
        a=a-1
    if a==0:
        return 0
    else:
        return a+paarissumma(a-2)
 
#paarissumma(a)       
#paarissumma(1)    
    
