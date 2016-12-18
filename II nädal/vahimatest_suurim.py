# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:23:29 2016

@author: Risto
Koostada funktsioon vahimatest_suurim, mis võtab argumendiks täisarvude maatriksi (listide listi) ja tagastab antud maatriksist kõikide ridade vähimatest elementidest suurima.

Teisisõnu peab tagastatav element olema

    vähim element oma reas,
    suurim element kõikide selliste elementide seas, mis on oma reas vähimad.

Kontrollitakse vaid funktsiooni definitsiooni, programmis seda rakendama ei pea.
"""

#mat=[[1,2],[1,0]]
def vahimatest_suurim(mat):
    vahim=[]
    for i in range(len(mat)):
        vahim.append(min(mat[i])) 
    return max(vahim)
    
#vahimatest_suurim(mat)
