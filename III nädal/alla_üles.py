# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:19:35 2016

@author: Risto
"""

def alla_üles(n):
    if n<=0:
        print("Baas!")
    else:
        print(n)
        alla_üles(n-2)
        print(n-1)
