# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 19:51:56 2016

@author: Risto
"""
#Analüüsi teemaks on meeste ja naiste ajakasutuse erinevus Eestis. Andmed on
#statistikaameti kodulehelt (http://pub.stat.ee/px-web.2001/Database/Sotsiaalelu/01Ajakasutus/01Ajakasutus.asp,
#tabel KESKMINE AJAKASUTUS PÄEVAS PÕHITEGEVUSE JA SOO JÄRGI). Kas vastab
#tõele, et naised tegelevad rohkem koduhoidmisega seotud tegevustega? ning
#mehed rohkem lõbutsemise ja tööga?
#Ülesandeks on teha funktsioon, mis leiab tabelist püles iga tegevuse ajavahe
#sugude lõikes ning kahel erineval perioodil, mis on tabelis toodud.
#Tulemina tuleks tagastada sorteeritud tabel. Lisaks peab tabelis olema veer, 
#kus on "kordisti", mitu korda on võrreldava soo ajakulu suurem võrdlusaluseks oleva
#soo ajakulust.
#from os import chdir
#chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\II nädal")
import pandas as pd

ajak = pd.read_csv('ajakasutus.csv', delimiter=';', encoding='utf-8')
ajak.head()
#asendame ".." nulliga
ajak.loc[ajak['Mehed']== '..']=0
#funktsioon, mis loob tabeli ajakulu võrdlusega
def ajavõrdlus(keda='Naised', periood="'2009-2010'", jarjestus='Kordistaja'):
    if keda=='Naised':
        kellega='Mehed'
    else:
        kellega='Naised'
    tegevused=[]
    naeg=[]
    maeg=[]
    osakaal=[]
    for i in range(len(ajak)):
        if (ajak['periood'][i] == periood and int(ajak[keda][i])>int(ajak[kellega][i])):
            tegevused.append(ajak['tegevus'][i])
            naeg.append(int(ajak[keda][i]))
            maeg.append(int(ajak[kellega][i]))
            if (int(ajak[keda][i])==0):
                kedaaeg=0.01#kui aeg on 0, siis pnen 0.01, et saaks jagada
            else:
                kedaaeg=int(ajak[keda][i])
            if (int(ajak[kellega][i])==0):
                kellegaaeg=0.01
            else:
                kellegaaeg=int(ajak[kellega][i])
            osakaal.append(kedaaeg/kellegaaeg)
        else:
            next  
    #paneme kokkudf-ks
    df = pd.DataFrame(tegevused)
    df['naeg']=naeg
    df['maeg']=maeg
    df['osakaal']=osakaal
    #anname df nimed
    df.columns = ['Tegevus', keda, kellega, 'Kordistaja']
    #järjekorda
    return df.sort([jarjestus], ascending=False)

#kasutamine   
ajavõrdlus()    
ajavõrdlus(keda='Mehed')    
ajavõrdlus(periood="'1999-2000'")    
ajavõrdlus(keda='Mehed',periood="'1999-2000'")    
#vastus:
#mehed tunduvad tõesti rohkem tööga tegelevat, mis läheb kokku ka hüpoteesiga
#lisaks tgelevad mehed ka rohkem arvutimängudega (kuid ajakulu absoluutmahus 
#pole suur). Naised tunduvad aga rohkem tegelevat tõesti kodu hoidmisega,
#hooldamise
