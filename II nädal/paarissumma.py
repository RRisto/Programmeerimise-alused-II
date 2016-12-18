# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 20:22:19 2016

@author: Risto
Kirjutada rekursiivne funktsioon paarissumma, mis võtab argumendiks ühe arvu a ja tagastab kõikide positiivsete paarisarvude summa, mis on väiksemad või võrdsed a-ga.

Oma funktsiooni saate lihtsalt testida, kirjutades sama funktsionaalsusega mitterekursiivse funktsiooni ning kontrollides, kas need funktsioonid annavad sama tulemuse näiteks väärtuste a=1…1000 korral.

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
    
