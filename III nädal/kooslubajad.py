# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 11:26:26 2016

@author: Risto
"""

def kooslubajad(lubadused):
    uhine=[]
    indeksid=[]
    for i in range(len(lubadused)):
        for j in range(len(lubadused)):
            if i!=j:
                uhine.append(len(set(lubadused[i])&set(lubadused[j])))
                indeksid.append((i,j))
    return indeksid[uhine.index(max(uhine))]