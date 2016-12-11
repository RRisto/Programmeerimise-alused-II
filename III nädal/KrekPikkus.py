def pikkus(loend):
    i = 0
    for c in loend:
        i += 1
    return i

def rpikkus(loend):
    if loend == []:
        return 0
    else:
        return 1 + rpikkus(loend[1:])
