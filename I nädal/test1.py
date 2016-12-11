# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 17:58:23 2016

@author: Risto
"""
#1
tabel=[[1,5,2],[3,7,9],[2,4,6]]
for rida in tabel:
    print(end=" | ")
    for el in rida:
       print(el, end=" | ") 
    print("")
    
#2
tabel[len(tabel)-1][len(tabel[len(tabel)-1])-1] 
#3
a=[[1,5,2,4],[3,7,9],[2,4,6]]
for i in range(len(a[0])):
    for el in a[i]:
        print(el)
#4
a=[[1,6,7],[30,21,24],[44,34,45,4],[46,60,52]]
s=a[0][0]
for rida in a:
    for el in rida:
        if el>s:
            s=el
print(s)

s=a[0][0]
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j]>s:
            s=a[i][j]
print(s)

s=a[0][0]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i][j]>s:
            s= a[i][j]
        j+=1
    i+=1
print(s)

s=a[0][0]
for i in range(len(a[0])):
    for j in range(len(a[i])):
        if(a[i][j]>s):
            s=a[i][j]
print(s)

s=a[0][0]
while i<len(a):
    while j <len(a[i]):
        if a[i][j]>s:
            s=a[i][j]
print(s)
#5
a=[[1,2.0,2],[3,7,3.7],["X",4,6]]
summa=0
for el in a:
    for i in el:
        if type(i)==int:
            summa+=i
print(summa)

a=[[1,2.0,2],[3,7,3.7],["X",4,6]]
summa=0
for el in a:
    for i in el:
        if i==int:
            summa+=i
print(summa)
 
a=[[1,2.0,2],[3,7,3.7],["X",4,6]]
summa=0
for el in a:
    for i in el:
        if type(i)==True:
            summa+=i
print(summa)

a=[[1,2.0,2],[3,7,3.7],["X",4,6]]
summa=0
for el in a:
    for i in el:
        if int(i)==True:
            summa+=i
print(summa)   

a=[[1,2.0,2],[3,7,3.7],["X",4,6]]
summa=0
for el in a:
    for i in el:
        if isinstance(i, int)==True:
            summa+=i
print(summa)          




