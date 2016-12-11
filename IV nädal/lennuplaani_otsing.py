# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 21:16:03 2016

@author: risto.hinno
Koostada rekursioonil põhinev funktsioon leidub_lennuplaan, mis võtab 
argumentideks lähtelinna nime, sihtlinna nime ja lendude andmebaasi, 
ning tagastab tõeväärtuse vastavalt sellele, kas selle andmebaasi järgi 
on võimalik lennata lähtelinnast otse või ümberistumistega sihtlinna.

Lendude andmebaas on esitatud sõnastikuna, kus iga kirje võtmeks on 
linna nimi ja vastavaks väärtuseks hulk, mis sisaldab kõiki sellest 
linnast lähtuvate otselendude sihtkohti.
"""

#lennud={"Pariis":{"London", "Berliin","Nice"},"London":{"Berliin":"Pariis"},
#        "Berliin":{"London", "Pariis","Tallinn"},"Tallinn":{"Berliin"}}


        
def leidub_lennuplaan(alg, siht, lennud,saab=[]):
        saab = saab + [alg]#igal ringil paneme leitud sihtkohad juurde
        if alg == siht:
            return True
        if alg not in lennud: 
            return False
        for linn in lennud[alg]:#iga sihtkoha kohta loobime 
            if linn not in saab:#kui linna pole juba saab listis
                uussaab = leidub_lennuplaan(linn, siht,lennud, saab)
                if uussaab: #kui tuli true, siis tagastab True
                    return uussaab
        return False

#leidub_lennuplaan(lennud, 'Tallinn', 'Nice')
#leidub_lennuplaan(lennud, 'Tallinn', 'nice')
#leidub_lennuplaan(lennud, 'Tallinn', 'Berliin')
#leidub_lennuplaan(lennud, 'Pariis', 'Berliin')
#leidub_lennuplaan(lennud, 'Pariis', 'Tallinn')

