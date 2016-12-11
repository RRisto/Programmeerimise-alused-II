# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 19:37:21 2016

@author: Risto
"""


from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\III nädal")

järjend=[[], [3,[4,5],[2,3,4,5,3,3], [7], 5, [1,2,3], [3,4]], [1,2,3,4,5]]
järjend=[[[1,2,3]]]
järjend=[1,2,3]
def max_pikkus(järjend):
    maxpikkus = len(järjend)
    for i in järjend:
        try:
            if type(i) == list:
                if maxpikkus < len(i):
                    maxpikkus = len(i)
                else:
                    maxpikkus = max_pikkus(i)
        except:
            #print('Error')
            continue
    return maxpikkus

max_pikkus(järjend)

def max_length(obj):
    if isinstance(obj,int):
        return len(obj)
    elif all(isinstance(i,int) for i in obj):
        return 1
    else:
        return max(max_length(i) for i in obj)
        
max_length(järjend)

def nested_list(l):
    if type(l) is not list:
        return 0

    lens = [len(l)]

    for x in l:
        lens.append(nested_list(x))
    return max(lens)
    
nested_list(järjend)

def max_pikkus(järjend):
    maxpikkus=[len(järjend)]
    for i in järjend:
        if isinstance(i, list):
            maxpikkus.append(max_pikkus(i))
    return max(maxpikkus)
    
max_pikkus(järjend)