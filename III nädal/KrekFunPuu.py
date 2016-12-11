def rekFun(x, y):
    if x == 0:
        return y
    elif x < 0:
        return rekFun(x + 1, y - 2)
    else:
        return rekFun(x - 1, y + 2)

print(rekFun(-6, 0))
