def aste(n, m):
    if m == 0:
        return 1
    else:
        return n * aste(n, m-1)
