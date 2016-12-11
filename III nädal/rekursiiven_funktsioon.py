# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 19:23:17 2016

@author: Risto
"""

def rek_fun(n):
    if n<=0:
        print("Baas!")
    else:
        print(n)
        rek_fun(n-2)
        print(n-1)
rek_fun(7)
rek_fun(8) 
    