# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 15:22:48 2016

@author: Risto
Õppejõud koostas eksami, milles oli 7 ülesannet. Iga ülesande eest 
võis saada kuni 10 punkti. Eksami tulemused on kirjas failis eksam.txt.

Leiame iga tudengi eksamipunktide kogusumma.
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\eksamiks")


def andmed_sisse(failinimi):
    f = open(failinimi,  encoding="UTF-8")
    andmed = f.readlines()
    abimuutuja=[]
    tulem=[]
    for rida in andmed:
        abimuutuja=rida.strip().split(' ')
        tulem.append(abimuutuja)
    return tulem

def andmed_sisse2(failinimi):
    f = open(failinimi,  encoding="UTF-8")
    andmed = f.readlines()
    abimuutuja=[]
    tulem=[]
    for rida in andmed:
        abimuutuja=rida.split('|')
        abimuutuja=abimuutuja[1].strip().split(',')
        tulem.append(abimuutuja)
    return tulem
    
f = open('eksam.txt',  encoding="UTF-8")
andmed = f.readlines()
abimuutuja=[]
tulem=[]
for rida in andmed:
    abimuutuja=rida.split('  |')
    tulem.append(abimuutuja)

    
tulem=andmed_sisse('eksam.txt')
arvud=andmed_sisse2('eksam.txt')

nimed=[]
for i in range(len(tulem)):
    nimed.append(tulem[i][0]+' '+tulem[i][1])
hinded=[]
for i in range(len(arvud)):
    hinne=0
    for j in range(len(arvud[i])):
        hinne+=int(arvud[i][j])
    hinded.append(hinne)

punktid=[]
for i in range(len(arvud)):
    abikas=[]
    for j in range(len(arvud[i])):
        abikas.append(int(arvud[i][j].strip()))
    punktid.append(abikas)

"""Maksimaalsed tulemused: leia iga ülesande kohta selle lahendamisel 
 saadud maksimaalne skoor.    """
maks=[]
for j in range(len(punktid[0])):
    abi=0
    for i in range(len(punktid)):
        if int(punktid[i][j])>abi:
            abi=int(punktid[i][j])
    maks.extend([abi])

"""Seinast seina: väljasta nende tudengite nimed, kes said vähemalt 
ühe ülesande eest 10 punkti ja mõne teise ülesande eest 0 punkti."""
seinast_seina=[]
for i in range(len(punktid)):
    if max(punktid[i])==10 and min(punktid[i])==0:
        seinast_seina.extend([nimed[i]])
        
"""Priimused: leia nende tudengite nimed, kes kogusid summaarselt kõige 
rohkem punkte. Kui mitu inimest sai sama palju punkte, väljasta kõigi 
nende nimed (vihje – kogu need nimed järjendisse)."""
maksp=max(hinded)
maksid=[]
for i in range(len(hinded)):
    if hinded[i]==maksp:
        maksid.append(nimed[i])
        
"""Spikerdamine: fail on koostatud nii, et kõrvuti istunud tudengite
 andmed on failis järjest. Kontrolli, kas tulemused viitavad sellele, 
 et mõni spikerdas oma naabri pealt. Loeme, et spikerdamises võib 
 tudengit kahtlustada, kui tema kõik tulemused on kas võrdsed või 
 ülimalt 2 punkti võrra väiksemad kui ühel tema kahest naabrist. 
 Väljasta kõigi spikerdamises kahtlustatavate tudengite nimed."""

spikerdaja=[]
for i in range(1,len(punktid)-1):
    vahe=[]
    vahe_parast=[]
    for j in range(len(punktid[j])):
        vahe.extend([punktid[i][j]-punktid[i-1][j]])
        vahe_parast.extend([punktid[i][j]-punktid[i+1][j]])
    if (max(vahe)<=0 and min(vahe)>=-2) or (max(vahe_parast)<=0 and min(vahe_parast)>=-2):
        spikerdaja.append(nimed[i])
    
"""Skaleeritud hindamine: oletame, et hindamisskeem on selline, et kui 
mõne ülesande eest ei saanud keegi maksimumpunkte, siis korrutatakse 
kõigi tudengite punktid läbi sellise koefitsiendiga, et parima tulemuse
 saanud tudengi uus tulemus oleks 10. Teisenda ja väljasta kõigi
 tudengite kõigi ülesannete punktid sellest hindamisskeemist lähtuvalt 
 (ühe komakoha täpsusega). Vihje: koosta järjend, kus on iga ülesande
 kohta leitud sellele vastav kordaja, ning kasuta seda tudengite hinnete
 tuvastamisel"""
koefit=[]
for i in range(len(maks)):
        koefit.extend([10/maks[i]])

punktid_skal=[]
for i in range(len(punktid)):
    abikas=[]
    for j in range(len(punktid[i])):
        abikas.append(round(punktid[i][j]*koefit[j],1))
    punktid_skal.append(abikas)
    
"""Hobide mõju: failis hobid.txt on eksami teinute hobid. Täienda 
programmi nii, et see väljastaks iga hobi kohta vastavate tudengite 
keskmise eksamitulemuse. """

f = open('hobid.txt',  encoding="UTF-8")
andmed = f.readlines()
abimuutuja=[]
tulem=[]
for rida in andmed:
        abimuutuja=rida.strip().split('|')
        tulem.append(abimuutuja)

hobinimed=[]
for i in range(len(tulem)):
    hobinimed.append(tulem[i][0].strip())

hobialad=[]

hobialad=andmed_sisse2('hobid.txt')
#eemaldan tühikud
hobialad2=[]
for i in range(len(hobialad)):
    abikas=[]
    for j in range(len(hobialad[i])):
        abikas.append(hobialad[i][j].strip())
    hobialad2.append(abikas)

ala=[]
for i in range(len(hobialad2)):
    for j in range(len(hobialad2[i])):
        if hobialad2[i][j] not in ala:
            ala.append(hobialad2[i][j])


def ala_esindajad(ala1):
    tulem=[]    
    for i in range(len(hobialad2)):
        abikas=[]
        for j in range(len(hobialad2[i])):
            if ala1==hobialad2[i][j]:
                abikas.append(hobinimed[i])
        tulem.extend(abikas)
    return tulem 


ala_esindajad('tantsimine')                   
ala_esindajad('kino')                   
           
#harrastajad
harrastajad=[]
for i in range(len(ala)):
    hobiala=ala[i]
    harrastajad.append(ala_esindajad(hobiala))
        
#keskmine
keskmised=[]
for i in range(len(punktid)):
    keskmised.append(sum(punktid[i])/len(punktid[i]))

#alade keskmised
def isiku_keskmine(nimi):
    hinne=0
    for i in range(len(nimed)):
        if nimed[i]==nimi:
            return keskmised[i]
            
rida=0
alahinded=[]
for i in range(len(harrastajad)):
    alhinded=[]
    for j in range(len(harrastajad[i])):
        alhinded.append(isiku_keskmine(harrastajad[i][j]))
    alahinded.append(alhinded)        
        
#ala keskmised
alakeskmine=[]
for i in range(len(alahinded)):
    alakeskmine.append(sum(alahinded[i])/len(alahinded))
#alade nimed 
ala    
 

   