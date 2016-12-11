# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 18:35:39 2016

@author: Risto
"""
failinimi=input("Sisestage failinimi: ")

def andmed_sisse(failinimi):
    f = open(failinimi,  encoding="UTF-8")
    andmed = f.readlines()
    #teeme andmetest korraliku järjendi (ilma tühikute ja numbriteks)
    numbrid=[]
    sudoku=[]
    for i in range(len(andmed)):
        for j in range(len(andmed[i])):
            numbrid.append(andmed[i][j].strip())
            numbrid=list(filter(None, numbrid))#eemaldame tühiku
            numbrid=list(map(int, numbrid))#teeme int-ks
        sudoku.append(numbrid)
        numbrid=[]
    return sudoku

def kastid_korras(sudoku):
    nums = set(range(1, 10))
    for i in range(3):
        for j in range(3):
            result=set()
            for row in sudoku[(i*3):(i*3+3)]:
                for n in row[(j*3):(j*3+3)]:
                    result.add(n)
            if result!=nums:
                        return False
            else:
                        return True
            
#kastid_korras(sudoku)  

def read_korras(sudoku):
    nums = set(range(1, 10))
    for i in range(len(sudoku)):
        result=set() #sisuliselt järjestatud list
        for j in range(len(sudoku[i])):
            result.add(sudoku[i][j])
        if result!=nums:
                return False
        else:
                return True
            
#sudokuT=list(map(list, zip(*sudoku)))#transpose, ridadest saavad veerud
def rea_summa(sudoku):
    tulem=True
    i=0
    while(tulem and i <(len(sudoku))):
        if sum(sudoku[i])!=45:
            tulem=False
        else:
            i+=1
    return tulem
            
#read_korras(sudoku)   
#read_korras(sudokuT) 

#õige arv element
#def oige_suurus(sudoku):
#    tulem=True
#    i=0
#    for i in range(len(sudoku)):
#        if (len(sudoku[i])==9):
#            return True
#        else:
 #           return False
def oige_suurus(sudoku):
    tulem=True
    i=0
    while(tulem and i <(len(sudoku))):
        if (len(sudoku[i])==9):
            i+=1
        else:
            tulem=False
    return tulem
            
#lõplik otsus
def sudoku_kontroll(failinimi):
    sudoku=andmed_sisse(failinimi)
    sudokuT=list(map(list, zip(*sudoku)))
    if (read_korras(sudoku) and read_korras(sudokuT) and  kastid_korras(sudoku) and rea_summa(sudoku) and rea_summa(sudokuT) and len(sudoku)==9 and oige_suurus(sudoku)):
        print("OK")
    else:
        print("Viga")

sudoku_kontroll(failinimi)


 