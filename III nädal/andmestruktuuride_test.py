# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 15:44:08 2016

@author: Risto
"""


#1
{1,4,2}|{1,2,7}&{3,1}
#2
{9,1,7}^{1,7,9}
#3
len(list(set((1,3,6,3,1))))
#4
linnad={"Tartu","Pärnu","Viljandi","Põlva","Tartu"}
linnad.add("Pärnu")
linnad.add("Narva")
if "Narva" not in linnad:
    print(linnad[1])
    
#5
paaride_hulk={(-2,8),(3,7),(2,9)}
tulemus=0
for paar in paaride_hulk.add((1,4)):
    tulemus+=paar[0]
print(tulemus)
