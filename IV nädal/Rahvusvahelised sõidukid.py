# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:23:32 2016

@author: risto.hinno
Kirjutada funktsioon failist_sõnastik, mis võtab argumendiks failinime 
ning tagastab vastava faili sisu põhjal sõnastiku, kus võtmeteks on 
riigitähised ja väärtusteks riikide nimed.
Kirjutada funktsioon tähised_nimedeks, mis võtab argumendiks järjendi 
riikide tähistest ja eelmise funktsiooni poolt koostatud sõnastiku ning 
tagastab järjendi vastavate riikide nimedest. Kui mõni tähis on tundmatu, 
siis selle riigi nimi asendada tagastatavas järjendis väärtusega None.
Rakendada funktsioone sobivalt programmis, mis küsib kasutajalt esiteks 
andmebaasi failinime ja teiseks sõne, mis koosneb tühikutega eraldatud 
piiri ületanud sõidukite riikide tähistest, ning väljastab sõidukite 
päritolumaade nimed üksteise alla. Kui mõni riigitähis on tundmatu, 
siis väljastada selle riigi nime asemel Tundmatu maa.

"""
#failinimi='riigid.txt'
def failist_sõnastik(failinimi):
    fo = open(failinimi, "r",encoding='utf8')
    andmed = fo.readlines()
    võti=[]
    väärtus=[]
    abimuutuja=[]
    for i in range(len(andmed)):
        abimuutuja=andmed[i].strip().split(' ', 1)
        võti.append(abimuutuja[0])
        väärtus.append(abimuutuja[1])
    #sõnastik
    return dict(zip(võti, väärtus))

#failist_sõnastik(failinimi)
#sõnastik=failist_sõnastik(failinimi)
def tähised_nimedeks(riigid, sõnastik):
    tulem=[]
    for i in riigid:
        if i in sõnastik:
            tulem.append(sõnastik[i])
        else:
            tulem.append(None)
    return tulem
    
#riigid=['EST','eeded', 'LT', 'Mää']   
#tähised_nimedeks(riigid, sõnastik)
    
failinimi=input('Riigitähiste faili nimi: ')
riigid=input('Piiri ületanud sõidukite tähised: ')
riigid=riigid.split()
nimed=tähised_nimedeks(riigid, failist_sõnastik(failinimi))
for i in nimed:
    if i==None:
        print('Tundmatu maa')
    else:
        print(i)



   