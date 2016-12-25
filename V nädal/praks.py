# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:20:54 2016

@author: Risto
"""

from os import chdir
chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\V nädal")


#vahe
a={1,3,6}
b={1,3,7}
c=a-b
print(c)#jätab need, mida pole teises
b-a
#sümmetriline vahe
a^b#jätab alles, mis ei ole nende ühisosas
b^a

ennik=(1,2,3)
ennik2=ennik[:]
ennik2

ennik2=ennik
ennik=list(ennik)
ennik2

hulk={1,2,3,4}
hulk.pop()
hulk[1]#error

#matrix transpose
mat=[[1,2], [3,4]]

def transp(mat):
    


uusmat=[]
for i in range(len(mat)):
    for j in range(len(mat[0])):
        uusmat[j][i]=mat[i][j]
        
X = [[12,7],
    [4 ,5],
    [3 ,8]]

result = [[0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

for r in result:
   print(r)
#veel üks variant   
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]

for r in result:
   print(r)

"""Kirjutada funktsioon, mis võtab argumendiks 2 maatriksit ning
 kontrollib, kas üks on saadud 
teisest transponeerimise teel. (Maatriksid ei pruugi olla 
ruutmaatriksid.)
https://et.wikipedia.org/wiki/Transponeeritud_maatriks """
#trued
maatriks_1 = [[1, 2], [3, 4], [5, 6]]
maatriks_2 = [[1, 3, 5], [2, 4, 6]]
#falsed
maatriks_3 = [[1, 2], [1, 1]]
maatriks_4 = [[1, 2, 3], [2, 2, 3]]

def transp_kontroll(mat, transp):
    uusmat=[]
    abikas=[]
    for j in range(len(mat[0])):
        abikas=[]
        for i in range(len(mat)):
            abikas.append(mat[i][j])
        uusmat.append(abikas)
    return uusmat==transp

transp_kontroll(maatriks_1, maatriks_2) 
transp_kontroll(maatriks_3, maatriks_4) 


 """Kirjutada funktsioon tulba_pikimad, mis võtab argumendiks 
 kahemõõtmelise järjendi, mille elementideks on sõnad. Funktsioon 
 leiab igas tulbas pikima sõna ning tagastab listi nendest 
sõnadest. Sama pikkusega sõnade puhul võetakse eespool olev sõna.
Kirjutada funktsioon enim_taishaalikuid, mis võtab argumendiks sõnade 
listi ning tagastab sõna, milles on kõige rohkem täishäälikuid. 
Täishäälikute leidmiseks võib kasutada listi: 
taishaalikud = ["a","e","i","o","u","õ","ä","ö","ü"]
Kasutades neid funktsioone, leida kahemõõtmelise järjendi 
tulba pikimatest sõnadest sõna, 
milles on kõige rohkem täishäälikuid"""

sonade_tabel = [["piim", "kommikarp", "lillkapsas"], ["leib", 
"hakkliha", "sink"], ["makaronid", "mandariinid", "tee"]]  

#minu kökerdis
def pikimad(sonade_tabel):
    pikimad=[]
    for j in range(len(sonade_tabel[0])):
        pikim=sonade_tabel[0][j]
        for i in range(len(sonade_tabel)):
            if len(sonade_tabel[i][j])>len(pikim):
                pikim=sonade_tabel[i][j]
        pikimad.append(pikim)
    return pikimad
                

pikimad(sonade_tabel)

def taishaalikuid(sone):
    taishaalikud = ["a","e","i","o","u","õ","ä","ö","ü"]
    summa=0
    for taht in sone:
        if taht in taishaalikud:
            summa+=1
    return summa
    
taishaalikuid("mina")            


def rohkeim_taishaalikuid(sonade_tabel):
    taishaalikud = ["a","e","i","o","u","õ","ä","ö","ü"]
    sone=""
    for i in range(len(sonade_tabel)):
        for j in range(len(sonade_tabel[i])):
            if taishaalikuid(sonade_tabel[i][j])>taishaalikuid(sone):
                sone=sonade_tabel[i][j]
    return sone

rohkeim_taishaalikuid(sonade_tabel)   
            

def tulba_pikimad(sonade_tabel):
    pikimad=[]  
    for j in range(len(sonade_tabel[0])):
        pikimsona=sonade_tabel[0][j]
        for i in range(len(sonade_tabel)):
            if len(pikimsona)<len(sonade_tabel[i][j]):
                pikimsona=sonade_tabel[i][j]
        pikimad.append(pikimsona)
    return pikimad
    
tulba_pikimad(sonade_tabel)
    

taishaalikud = ["a","e","i","o","u","õ","ä","ö","ü"]

def mitu_taishaalikut(sona):
    taishaalikud=["a","e","i","o","u","õ","ä","ö","ü"]
    arv=0
    for taht in sona:
        if taht in taishaalikud:
            arv+=1
    return arv
    
    
#ei pea olema kahemõõtmeline järjend    
def enim_taishaalikuid(sonade_tabel):
    sona=""
    max_taishaalikuid=0
    for i in range(len(sonade_tabel)):
        for j in range(len(sonade_tabel[i])):
            if max_taishaalikuid<mitu_taishaalikut(sonade_tabel[i][j]):
                sona=sonade_tabel[i][j]
                max_taishaalikuid=mitu_taishaalikut(sonade_tabel[i][j])
    return sona
#õige
def enim_taishaalikuid(slist):
    th_rohkem_sona=slist[0]
    for sona in slist:
        if mitu_taishaalikut(th_rohkem_sona)<mitu_taishaalikut(sona):
            th_rohkem_sona=sona
    return th_rohkem_sona

print(enim_taishaalikuid(tulba_pikimad(sonade_tabel)))  

"""Pekingi olümpiamängude tarbeks rakendati 2008. aastal ajutiselt 
liikluses regulatsioonid, et 
vähendada õhusaastet. Paarisarvulisel kuupäeval võisid liikuda
 vaid autod, mille 
numbrimärgil oli paarisarv ning paaritul kuupäeval võisid liikuda 
autod, mille numbrimärgil 
oli paaritu arv. 
Failis on igal real ühe pere autode numbrimärgid tühikuga eraldatud. 
Küsida kasutajalt kuupäev, kujul DD-MM-YYYY. 
Funktsioon võtab argumentideks failist loetud kahemõõtmelise järjendi 
ja kasutaja 
sisestatud kuupäeva ning tagastab perede arvu, kes ei saa sel päeval 
autoga liikuda"""

failinimi=input("Sisestage failinimi: ")

f = open("numbrimärgid.txt",  encoding="UTF-8")
andmed = f.readlines()

tulem=[]
for i in range(len(andmed)):
        tulem.append(andmed[i].split())
        
print(tulem) 
            
def kes_saab(tulem, kpv):
    paev=int(kpv[0:2])
    pos=neg=0
    if paev%2==0:
        for i in range(len(tulem)):
            arv=0
            for j in range(len(tulem[i])):
                if int(tulem[i][j][-1])%2==0:
                    arv+=1
            if arv>0:
                pos+=1
        return (len(tulem)-pos)
    
    if paev%2!=0:
        for i in range(len(tulem)):
            arv=0
            for j in range(len(tulem[i])):
                if int(tulem[i][j][-1])%2!=0:
                    arv+=1
            if arv>0:
                neg+=1
        return (len(tulem)-neg)
           
kes_saab(tulem, '15-detsember-2016')
kes_saab(tulem, '14-detsember-2016')

"""Kirjutada funktsioon, mis võtab argumendiks sõnade järjendi ning 
tagastab sõnastiku, kus 
võtmeks on sõna ning väärtuseks sõnas esinevate täishäälikute arv."""

sonade_jarjend = ["logistik", "bussijuht", "autolukksepp", 
"kirjakandja", "programmeerija", "klienditeenindaja"]

def taishaalikuid(sone):
    arv=0
    taishaalikud=["a","e","i","o","u","õ","ä","ö","ü"]
    for i in sone:
        if i in taishaalikud:
            arv+=1
    return arv

def sonastik(jarjend):
    sonastik={}
    for i in sonade_jarjend:
        sonastik[i]=taishaalikuid(i)
    return sonastik

sonastik(sonade_jarjend)

"""Python lubab listidesse panna liste, mille elementideks on omakorda
 listid, mille 
elementideks on listid jne.
Kirjuta funktsioon max_pikkus, mis võtab argumendiks listi, mille 
elementideks võivad olla 
täisarvud või listid, mille elementideks võivad olla täisarvud või 
listid, mille jne. Funktsioon 
peab tagastama pikima selles puntras leiduva listi pikkuse."""

jarjend=[[], [3,[4,5],[2,3,4,5,3,3], [7], 5, [1,2,3], 
[3,4]], [1,2,3,4,5]]
jarjend=[1,2,3]
jarjend=[[[1,2,3]]]



def max_pikkus(lst):
    maxpikkus=len(lst)
    pikkus=len(lst)
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            pikkus=max_pikkus(lst[i])
            if pikkus>maxpikkus:
                maxpikkus=pikkus
    return maxpikkus

max_pikkus(jarjend)            


def max_pikkus(jarjend):
    pikkus=[len(jarjend)]
    for i in range(len(jarjend)):
        if isinstance(jarjend[i], list):
             pikkus.extend([max_pikkus(jarjend[i])])
    return max(pikkus)
    
max_pikkus(jarjend)  

#teine variant
def max_pikkus(jarjend):
    pikkus=len(jarjend)
    for i in range(len(jarjend)):
        if isinstance(jarjend[i], list):
             pikkusuus=max_pikkus(jarjend[i])
             if pikkusuus>pikkus:
                 pikkus=pikkusuus
    return pikkus
max_pikkus(jarjend)  
#max element
def max_el(jarjend):
    element=0
    for i in range(len(jarjend)):
        if isinstance(jarjend[i], list):
             elementuus=max_el(jarjend[i])
             if elementuus>element:
                 element=elementuus
        if isinstance(jarjend[i], int):
            elementuus=jarjend[i]
            if elementuus>element:
                 element=elementuus
    return element
    
max_el(jarjend)    
#teha list flatiks
def flattened(jarjend):
    new_lis = []
    for item in jarjend:
        if type(item) == type([]):
            new_lis.extend(flattened(item))
        else:
            new_lis.append(item)
    return new_lis

flattened(jarjend)

"""Koostada rekursiivne funktsioon, mis saab argumendina ühe positiivse 
täisarvu. Funktsioon 
peab (igal väljakutsel) ekraanile väljastama argumendi. Rekursiivselt 
peab korraldama, et igal 
järgmisel väljakutsel on argument eelmisest 3 võrra väiksem ja argument 
oleks positiivne.
Lõpuks peab funktsioon peab tagastama esimese sellise arvu, mis pole 
positiivne"""

def fun(arv):
    tulem=arv
    if arv>0:
        print(arv)
        tulem=fun(arv-3)
    return tulem

fun(11)
fun(-3)

##muu pula    
def on_palindroom(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and on_palindroom(s[1:-1])

s = 'kuulilennuteetunneliluuk'      
on_palindroom(s)

def rpikkus(loend):
    if loend == []:
        return 0
    else:
        return 1 + rpikkus(loend[1:])


rpikkus(jarjend)

def rekFun(x, y):
    print(y)
    if x < 0:
        return y
    else:
        return rekFun(x - 1, y + 2) + rekFun(x - 2, y + 3)
 
print(rekFun(2, 0))


def rekFun(x, y):
    print(y)
    if x < 0:
        return y
    else:
        return rekFun(x - 1, y + 2)
 
print(rekFun(2, 0))

def rekFun(x, y):
    print(y)
    if x < 0:
        return y
    else:
        return rekFun(x - 2, y + 3)
        
    
print(rekFun(2, 0))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
        
        
        
fibonacci(4)

#andmestruktuurid
h1 = {1, 2 ,3 ,4}
h2 = {3, 5, 6, 7}
h2.add(7)
h1.update(h2)
h3 = {4, 6, 7}
h4 = h1 | h2 & h3
print(h4 ^ {1, 2, 5})

{1,2,3}<={1,2,3}

h1

h5=h1

h5
h5.add(8)
h1
h5


hääli = {'Andrus': 12900, 'Indrek':14000, 'Marju':19000}
hääli2=hääli


hääli2['mina']=500
hääli

muusikud = ("John", "Paul", "George", "Ringo") 
a = [1941, 1842, 1943] 
a[1] = 1942 
s = {muusikud[0]:a[0], muusikud[2]:a[2], muusikud[3]:a[0]} 
s["Paul"] = a[1] 
print(s["John"]) 
print(s["Paul"]) 
s2 = s.copy() 
del s2["John"] 
s.update({"John":1940}) 
for i,j in s2.items(): print(j,i)


##kaustade läbimise ülesanne
struktuur=[["Fail11"], ["Fail21"],
           [["Fail311"], "Fail31", "Fail32", "Fail33"],
  "Fail1", "Fail2"]
  
def fun(järjend, taane):
    i=1
    for element in järjend:
        if isinstance(element, list):
            print(taane+"Kaust "+str(i))
            fun(element, taane+"     ")
            i+=1
        else:
            print(taane+"Fail: "+element)
            
fun(struktuur, "     ")

#leida mitmemõõtmelise järjendi max element

tabel = [[1, -43, 5, 3, 7], [-4, 6, 7, 2, 3], [5, 6, -7, -1, 4]]
lst = []

for i in range(len(tabel)):
 loendaja = 0
 for j in range(len(tabel[i])):
  if tabel[i][j] % 2 == 0:
   loendaja += 1
 if loendaja >= 2:
   lst += [i]#nii saab ka listi appendida

print(lst) 


def on_suuremaid(järjend, piir):
    for i in range(len(järjend)):
        if järjend[i] > piir:
            return True
    return False
    
tabel = [[1, -43, 5, 3, 7], [-4, 6, 7, 9, 8], [5, 6, -7, -1, 4]]

loendaja = 0
for el in tabel:
    if on_suuremaid(el, 6):
        loendaja += 1

print(loendaja)

tabel[0]<6
    
def väljasta_tabel(tabel):
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            print(tabel[i][j], end=" ")
        print()
 
arvude_tabel = [[1, 3, 5], [4, 6, 6], [3, 6, -3]]
väljasta_tabel(arvude_tabel)
arvude_tabel2 = [[-1, 3, 5], [4, -8, 6]]
väljasta_tabel(arvude_tabel2)


def loo_diagonaalmaatriks(järk, sisu):
    maatriks = []
    for i in range(järk): #ridade koostamine
        rida = []
        for j in range(järk):
            if i == j: # peadiagonaalil
                rida.append(sisu)
            else:
                rida.append(0)
        maatriks.append(rida)
    return maatriks
    
loo_diagonaalmaatriks(3, 1)

lst=[1,2,3]


def rekFun(n):
    if n > 0:
        print("E")
    else:
        print(n)
        rekFun(n + 2)
        print(n)
 
rekFun(-7)

#puureksursioon
from turtle import *
from random import *
def puu(pikkus):
    if pikkus < 5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(45)
        puu(randint(6, 7) / 10 * pikkus)
        right(90)
        puu(randint(6, 7) / 10 * pikkus)
        left(45)
        back(pikkus)

puu(4)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
fibonacci(4)


def paaris(n):
    if n == 0:
        return True
    else:
        return paaritu(n - 1)
 
def paaritu(n):
    if n == 0:
        return False
    else:
        return paaris(n - 1)
        
        
paaris(2) 
paaritu(2)       


def faktoriaal_saba(n, f=1):
    if n == 0:
        return f
    else:
        return faktoriaal_saba(n - 1, f * n)
 
print(faktoriaal_saba(3))


#proovin listi sisse stuffi
lst=[[1, 2, "mina"], [3,4], (5,6),{"töö":"mkm", "kodu":"lasna"}, {7,8,9}]

lst=[(1,2,3),{"töö":"mkm", "kodu":"lasna"}]
def prindi_tuple(andmed):
    for i in range(len(andmed)):
        print(andmed[i])
        
def prindi_dict(andmed):
    for i in andmed.keys():
        print(andmed[i])

def prindi_set(andmed):
    for i in andmed:
        print(i)
def prindi_list(andmed):
    for i in range(len(andmed)):
        print(andmed[i][j])
        
for i in range(len(lst)):
    if isinstance(lst[i], tuple):
        prindi_tuple(lst[i])
    if isinstance(lst[i], dict):
        prindi_dict(lst[i])
    if isinstance(lst[i], list):
        prindi_list(lst[i])
    if isinstance(lst[i], set):
        prindi_set(lst[i])
        
        
ennik={1,2,(3,4)}        
for i in ennik:
    print(i)        
 


sonastik={"lst":[1,2,3], "ennik":(1,2,3)}       
sonastik['lst']
sonastik['ennik']
        
       
       
dict1={"töö":"mkm", "kodu":"lasna"}
type(dict1.keys())     
list(dict1.keys())
       
     
ennik=(1,2,3)

ennik2=ennik[:]
proov=zip([1,2,3], [4,5,6])
proov
for i in proov:
    print(i)

ennik
ennik.add(4)


lst1=[1,2,3]
lst2=[4,5,6]

lst1.append(lst2)

lst1.extend(lst2)

lst1=[1,2,3]
lst2=[4,5,6]
lst1+lst2

#pole saama
a = [1, 2, 3]
b=a
b=b+[4]
a
b
#mis
a = [1, 2, 3]
b=a
a+=[1]
a
b

#koopia tegemin
from copy import deepcopy
a = [1,2,[3,3]]
b = deepcopy(a)
a[2].append(4)
a
b
c=a.copy()
c[2].append("proov")
c
c[0].append("proov2")

#töötab, listide ja ennikute puhul mitte
{(1,2), (3,4,5)}

