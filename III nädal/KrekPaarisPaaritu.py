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


