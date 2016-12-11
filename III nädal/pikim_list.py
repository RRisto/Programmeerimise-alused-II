# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 18:29:29 2016

@author: Risto
"""

#from os import chdir
#chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\III nädal")

#järjend=[[], [3,[4,5],[2,3,4,5,3,3], [7], 5, [1,2,3], [3,4]], [1,2,3,4,5]]
#järjend=[[[1,2,3]]]
järjend=[1,2,3]


def max_pikkus(järjend):
    maxpikkus=[len(järjend)]
    for i in järjend:
        if isinstance(i, list):
            maxpikkus.append(max_pikkus(i))
    return max(maxpikkus)
    
max_pikkus(järjend)
max_pikkus(järjend)