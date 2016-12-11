def printAlla(n):
    if n <= 0: 
        print("Stop!") 
    else:
        print(n) 
        printAlla(n-1)
