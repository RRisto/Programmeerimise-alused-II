# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:33:14 2016

@author: Risto
Ülesanne

Liftide puhul on oluline nende kandevõime, mis sõiduliftide puhul on 320–1600 kilogrammi. Sageli märgitakse kandevõime nii inimeste arvu kui ka kogumassiga (nt kandevõime on 5 inimest, 400 kg). Mõeldud on siis nii, et näiteks neli 105-kilogrammist inimest lifti minna ei tohi. Või ka kuus 60-kilogrammist.

Olgu liftiootajate massid kirjas failis, igaüks eri real (see fail teha ise mingi tekstiredaktoriga).  Lifti sisenemisel analüüsitakse failis olevaid masse ning lifti lubatakse vastavalt kandevõimele inimesi nimekirja algusest.  

Koostada funktsioon mitu_esimest, mis võtab argumentideks masside järjendi, kandevõime inimeste arvuna ja kandevõime kilogrammides ning leiab ja tagastab (return), mitu esimest inimest lifti pääseb. Näiteks, kui järjendis on massid 110, 115, 120, 105, 80 ja kandevõime on 5 inimest, 400 kilogrammi, siis funktsioon tagastab arvu 3, sest neljanda inimesega  kandevõime ületataks.  Kui aga järjendis on massid 50, 65, 60, 58, 40, 56 ja kandevõime on 5 inimest, 400 kilogrammi, siis funktsioon tagastab arvu 5, sest kuues inimene oleks juba üle  kandevõime.

Koostada programm, mis

    küsib kasutajalt failinime;
    loeb failist lifti ootajate massid ja koostab nendest järjendi;
    leiab ja väljastab ekraanile, kui suur on liftiootajate kogumass;
    küsib kasutajalt lifti kandevõime inimeste arvuna;
    küsib kasutajalt lifti kandevõime kilogrammides;
    leiab ja väljastab ekraanile, mitu esimest inimest lifti pääseb. Selleks tuleb kasutada koostatud funktsiooni mitu_esimest.

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

    