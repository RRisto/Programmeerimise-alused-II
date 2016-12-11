# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 19:28:43 2016

@author: Risto
"""
#lubadused=[{"lastetoetusi tõsta", "pensione tõsta", "tulumaksu langetada", "kaitsekulutusi tõsta"},{"muuta kõike varasemat"},{"sisserännet piirata", "pensione tõsta", "kaitsekulutusi tõsta"},{},{"väljarännet piirata", "pensione tõsta", "õpetajate palku tõsta", "kaitsekulutusi tõsta", "alkoholiaktsiisi tõsta"}]

def kooslubajad(lubadused):
    uhine=[]
    indeksid=[]
    for i in range(len(lubadused)):
        for j in range(len(lubadused)):
            if i!=j:
                uhine.append(len(set(lubadused[i])&set(lubadused[j])))
                indeksid.append((i,j))
    return indeksid[uhine.index(max(uhine))]
            
#kooslubajad(lubadused)    
    
