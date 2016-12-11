# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:33:14 2016

@author: Risto
"""

failinimi=input("Sisestage failinimi: ")
f = open(failinimi,  encoding="UTF-8")
massid = f.readlines()

kaal=[]
for mass in massid:
    kaal.append(int(mass.rstrip()))

print("Liftiootajate kogumass on", sum(kaal), "kilogrammi")

maxinimest=int(input("Milline on lifti kandevõime inimeste arvuna? "))
maxkaal=int(input("Milline on lifti kandevõime kilogrammides? "))

def mitu_esimest(massid, maxin,maxkg):
    loop=0
    kaalud=0
    kontrollkaal=massid[0]
    inimest=0
    while (kontrollkaal<maxkg and inimest<maxin and loop<=(len(massid)-1)):
        kaalud+=massid[loop]
        if(loop+1>(len(massid)-1)):
            kontrollkaal=kontrollkaal
        else:
            kontrollkaal+=massid[loop+1]
        inimest+=1
        loop+=1
    return inimest
    
print("Lifti pääseb nimekirja",mitu_esimest(massid=kaal, maxin=maxinimest, maxkg=maxkaal),"esimest")

    