# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 12:32:46 2016

@author: Risto
"""

#from os import chdir
#chdir(r"C:\Users\Risto\Documents\Infotehnoloogia mitteinformaatikutele\Programmeerimise alused II\II nädal")

failinimi=input("Sisestage failinimi: ")
f = open(failinimi,  encoding="UTF-8")
sudoku = f.readlines()

numbrid=[]
tulem=[]
for i in range(len(sudoku)):
    for j in range(len(sudoku[i])):
        numbrid.append(sudoku[i][j].strip())
        numbrid=list(filter(None, numbrid))
        numbrid=list(map(int, numbrid))
    tulem.append(numbrid)
    numbrid=[]

#kontrollime kas asja pole reas rohkem kui ühe korra
veaRida=[]
veaVeerg=[]
korduvR=False
for i in range(len(tulem)):
    for j in range(len(tulem[i])):
        if(tulem[i].count(tulem[i][j])>1):
            korduvR=True
            #tulem[i].index(tulem[i][j])
            veaVeerg.append(j+1)
            veaRida.append(i+1)
        else:
            next
#kontrollime ka rea summa on 45
rida45=True
veaRida45=[]
for i in range(len(tulem)):
    if sum(tulem[i])!=45:
        rida45=False
        veaRida45.append(i+1)
    else:
        next
#kontrollime sama asja ka veerus
veerg45=True
veaVeerg45=[]
tulemT=list(map(list, zip(*tulem)))#transpose
for i in range(len(tulemT)):
    if sum(tulemT[i])!=45:
        veerg45=False
        veaVeerg45.append(i+1)
    else:
        next
#tulemite printimine
if korduvR==True:
    print("Viga real nr", str(veaRida[0])+ ", veerus nr",str(veaVeerg[0]))
elif rida45==False:
    print("Viga real nr",str(veaRida45[0]))
elif veerg45==False:
    print("Viga veerus nr", str(veaVeerg45[0]))
else:
    print("OK")


#veel netist
# 3x3
r1 = [9,3,2,5,4,8,1,7,6]
r2 = [1,8,7,9,2,6,5,4,3]
r3 = [5,4,6,3,7,1,2,8,9]
sec1 = [r1, r2, r3]
nums = set(range(1, 10))

nums == set(n for row in sec1 for n in row[:3])
#This iterates over the first three rows and returns the first 
#three elements in each of those rows. To get a better visual, 
#here is the equivalent for-loop code to make it a bit easier 
#to decipher:
result = set()
for row in sec1[:3]:
    for n in row[:3]:
      result.add(n)


for i in range(3):
    for j in range(3):
        result=set()
        for row in tulem[(i*3):(i*3+3)]:
            for n in row[(j*3):(j*3+3)]:
                result.add(n)
        if result!=nums:
            print("kolmik rida", i, "veerg",j, "ei vasta")
        else:
            print("arvud on:" ,result)
            

#ridade kontroll, et on 1-9




#netist
            
            
# checks no duplicates from 1 to 9 (duplicate 0's are ok)
def check_no_dups(nineGrouping):  
    uniqueDigits = set()
    for num in nineGrouping:
      if num != 0:
        if num  in uniqueDigits:
            return False
      uniqueDigits.add(num)
    return True
    

def check_row(grid, row):
    nineGrouping = []
    for cell in grid[row]:
        nineGrouping.append(cell)
    return check_no_dups(nineGrouping)

def check_column(grid, column):
    nineGrouping = []
    for row in grid:
        nineGrouping.append(row[column])
    return check_no_dups(nineGrouping) 

def check_subgrid(grid, row, column):
    nineGrouping = []
    for i in range(row, row + 3):
        for j in range(column, column + 3):
            nineGrouping.append(grid[i][j])
    return check_no_dups(nineGrouping)

def check_sudoku(grid):
    if not nine_by_nine(grid) or not all_digits(grid):
      return None
    for i in range(0, 9):
      if not check_row(grid, i):
          return False
      if not check_column(grid, i):
	      return False
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            if not check_subgrid(grid, i, j):
                return False

    return True
pass

#test
check_sudoku(tulem)
