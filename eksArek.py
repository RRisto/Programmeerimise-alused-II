def fun(n):
    if n > 0:
        print(n)
        return fun(n-3)
    else:
        return n

print("Tagastatakse: " + str(fun(6)))