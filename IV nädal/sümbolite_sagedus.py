# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:08:06 2016

@author: risto.hinno
Kirjutada funktsioon sümbolite_sagedus, mis võtab argumendiks sõne ja 
tagastab sõnastiku, mis sisaldab selles sõnes esinevate tähtede 
esinemiste sagedusi.
Sõnastiku võtmeteks on tähed või muud sümbolid (ehk sõned pikkusega 1) 
ja väärtusteks täisarvud, mis näitavad, mitu korda vastavad sümbolid 
sõnes esinesid. Esitada tuleb vaid funktsiooni definitsioon. Programmi 
põhiosas seda rakendama ei pea.
"""

#sõne='abca11'
def sümbolite_sagedus(sõne):
    unik=list(set(sõne))
    sagedus=[]
    arv=0
    for i in range(len(unik)):
        for j in range(len(sõne)):
            if unik[i]==sõne[j]:
                arv+=1
        sagedus.append(arv)
        arv=0
    return dict(zip(unik, sagedus))
    
    
#sümbolite_sagedus(sõne)
