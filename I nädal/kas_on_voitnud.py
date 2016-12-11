# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 16:53:53 2016

@author: Risto
"""
#from os import chdir
#chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\I nädal")

def võitis_nurkademängu(tabel):
    nurgad=0
    
    for i in range(0,len(tabel), 4):
        for j in range(0,len(tabel[i]),4):
            if (tabel[i][j]=="X"):
                nurgad+=1
    
    if (nurgad==4):
        return True
    else:
        return False

#tabel=[[1,30,34,55,"X"],[10,"X",40,"X",67],[5,20,"X",48,61],[4,"X",43,"X",70],["X",17,33,51,"X"]]
#tabel=[[1,30,34,55,"X"],[10,16,"X",50,67],["X",20,38,48,61],[4,26,43,49,70],["X",17,33,51,66]]
#tabel=[["X",30,34,55,"X"],[10,16,"X",50,67],["X",20,38,48,61],[4,26,43,49,70],["X",17,33,51,66]]

#võitis_nurkademängu(tabel)

def x_peadiagonaalil(tabel):
    xdiag=0
    for i in range(0,len(tabel)):
        if (tabel[i][i]=="X"):
                xdiag+=1
    return xdiag

def x_kõrvaldiagonaalil(tabel):
    ydiag=0
    for i in range(len(tabel)):
        if (tabel[i][4-i]=="X"):
                ydiag+=1
    return ydiag

def võitis_diagonaalidemängu(tabel):
    if (x_peadiagonaalil(tabel)==5 and x_kõrvaldiagonaalil(tabel)==5):
        return True
    else:
        return False
    
#võitis_diagonaalidemängu(tabel)    
    
def võitis_täismängu(tabel):
    element=0
    for i in range(len(tabel)):
        for j in range(len(tabel)):
            if (tabel[i][j]=="X"):
                element+=1
    if (element==25):
        return True
    else:
        return False

#tabel=[["X","X","X","X","X"],["X","X","X","X","X"],["X","X","X","X","X"],["X","X","X","X","X"],["X","X","X","X","X"]]
            
#võitis_täismängu(tabel)          
            
        
            
    