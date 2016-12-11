# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:23:29 2016

@author: Risto
"""

#mat=[[1,2],[1,0]]
def vahimatest_suurim(mat):
    vahim=[]
    for i in range(len(mat)):
        vahim.append(min(mat[i])) 
    return max(vahim)
    
#vahimatest_suurim(mat)
