# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 18:46:43 2016

@author: Risto
"""
#kahemõõtmeline järjend,
#1
a=["javascript", "java", "PHP","Python"]
for i in range(len(a)):
    keel=""
    for j in range(len(a[i])-1,-1,-1):
        keel+=a[i][j]
    a[i]=keel
    
print(a)

#2
tabel=[[1,2,3], [4,5,6], [7,8,9]]
uus=[]

for i in range(len(tabel)):
    rida=[]
    for j in range(len(tabel)):
        rida.append(tabel[j][i])
    uus.append(rida)
print(uus)

#3
tabel=[[1,2,3,10],[4,5,6,7],[8,9,11,34]]

for i in range(0, len(tabel), 2):
    for j in range(0,3):
        print(tabel[i][j], end=" ")
    print("")

#4
a=[[-2,3,1],[1,6,2],[4,2,1]]
ridade_suurimad=[]
for i in range(len(a)):
    suurim=a[i][0]
    for j in range(len(a[i])):
        if a[i][j]>suurim:
            suurim=a[i][j]
    ridade_suurimad.append(suurim)
print(sum(ridade_suurimad))

ridade_suurimad=[]
for i in range(len(a)):
    ridade_suurimad.append(suurim_reas(a[i]))
print(sum(ridade_suurimad))

def suurim_reas(b):
    suurim=b[0]
    for i in range(len(b)):
        if b[i]>suurim:
            suurim=b[i]
    return suurim

def suurim_reas(b):
    suurim=b[0]
    i=0
    while i<len(b):
        if b[i]>suurim:
            suurim=b[i]
        i+=1
    return suurim
    
def suurim_reas(b):
    suurim=b[0]
    for i in range(len(b)):
        if b[i]>suurim:
            return suurim

def suurim_reas(b):
    suurim=b[0]
    while i<len(b):
        if b[i]>suurim:
            suurim=b[i]
    return suurim
    
#5
for i in range(5):
    for j in range(5):
        if j>i:
            print(" ",end="")
        else:
            print("*",end="")
    print("")
    

############rekursiooni test
#1
def fun(x,y):
    if y==0:
        return x
    else:
        return fun(y, x%y)

print(fun(12,20))
#2
def üksKood(x):
    return üksKood(x)
print(üksKood(3))

#3
def üksKood(x):
    if x==3:
        return x
    else:
        return üksKood(x-1)

print(üksKood(5))

#4
def mitu_baasi(n):
    if n==3:
        return n+3
    if n==2:
        return n+2
    if n==1:
        return n+1
    else: 
        return mitu_baasi(n-1)

print(mitu_baasi(4))

#5
def mitu_baasi(n):
    if n==3:
        return n+3
    if n==2:
        return n+2
    if n==1:
        return n+1

print(mitu_baasi(4))
