# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 08:34:35 2016

@author: Risto
Kirjutada rekursioonil põhinev funktsioon koosta_lennuplaan, mis võtab 
argumendiks lähtelinna nime, sihtlinna nime ja lendude andmebaasi ning 
tagastab järjendi linnanimedest, mida tuleb lendude abil läbida, et jõuda
 lähtelinnast sihtlinna. Järjend algab lähtelinnaga ja lõppeb sihtlinnaga.
Kui selliseid marsruute leidub mitu, siis tagastada neist suvaline. 
Kui ühtegi marsruuti ei leidu, siis tagastada None.
"""

lennud={"Pariis":{"London", "Berliin","Nice"},"London":{"Berliin":"Pariis"},
        "Berliin":{"London", "Pariis","Tallinn"},"Tallinn":{"Berliin"}}


        
def koosta_lennuplaan(alg, siht, lennud,saab=[]):
        saab = saab + [alg]#igal ringil paneme leitud sihtkohad juurde
        if alg == siht:
            return saab
        if alg not in lennud: 
            return None
        for linn in lennud[alg]:
            if linn not in saab:
                uussaab = koosta_lennuplaan(linn, siht,lennud, saab)
                if uussaab: #kui kuskil leiab sihtkoha, siis tagastab teekonna
                    return uussaab
        return None #kui eelnevalt vastet ei leidnud tagastab None
        

koosta_lennuplaan('Tallinn', 'Nice', lennud)
#koosta_lennuplaan('Tallinn', 'AU', lennud)
