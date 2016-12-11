# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:09:54 2016

@author: Risto
"""

#from os import chdir
#chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\I nädal")

#table=[[1,30,34,55,75],[10,16,40,50,67],[5,20,38,48,61],[4,26,43,49,70],[15,17,33,51,66]]
#table=[[1,30,34,55,76],[10,16,40,50,67],[5,20,38,48,61],[4,26,43,49,70],[15,17,33,51,66]]

def on_legaalne_bingo_tabel(table):
    i=0
    j=0 
    tulem=True
    for i in range(len(table)):
        for j in range(len(table[0])):
            if((j*15)<table[i][j] <=((j+1)*15)):
                j+=1
            else:
                tulem=False
                break
        i+=1
    return tulem

      
##on_legaalne_bingo_tabel(table)
