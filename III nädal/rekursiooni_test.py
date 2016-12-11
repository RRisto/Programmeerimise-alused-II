# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 20:38:27 2016

@author: Risto
"""

#esimene küs
from turtle import *
def puu(pikkus):
    if pikkus<5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(45)
        puu(0.6*pikkus)
        right(90)
        puu(0.6*pikkus)
        left(45)
        back(pikkus)
delay(0)
speed(10)
left(90)
puu(100)

#2
def puu(pikkus):
    if pikkus<5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(55)
        puu(0.6*pikkus)
        right(90)
        puu(0.5*pikkus)
        left(50)
        back(pikkus)
delay(0)
speed(10)
left(90)
puu(100)

exitonclick()

def puu(pikkus):
    if pikkus<5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(50)
        puu(0.6*pikkus)
        right(90)
        puu(0.5*pikkus)
        left(40)
        back(pikkus)
delay(0)
speed(10)
left(90)
puu(100)

exitonclick()

def puu(pikkus):
    if pikkus<5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(50)
        puu(0.5*pikkus)
        right(90)
        puu(0.5*pikkus)
        left(40)
        back(pikkus)
delay(0)
speed(10)
left(90)
puu(100)

exitonclick()

def puu(pikkus):
    if pikkus<5:
        forward(pikkus)
        back(pikkus)
    else:
        forward(pikkus)
        left(50)
        puu(0.99*pikkus)
        right(90)
        puu(0.9*pikkus)
        left(40)
        back(pikkus)
delay(0)
speed(10)
left(90)
puu(100)

exitonclick()

#3
def printKuhu(n):
    if n>=30:
        print("Stop!")
    else:
        print(n)
        printKuhu(n+5)

print(printKuhu(5))

#4
def printKuhu(n):
    if n<=0:
        print("Stop!")
    else:
        print(n-1)
        printKuhu(n-1)
        print(n)
print(printKuhu(2))