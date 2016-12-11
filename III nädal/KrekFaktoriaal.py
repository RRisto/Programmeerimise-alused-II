def faktoriaalRek(n):
    if n == 0:
        return 1
    else:
        return n * faktoriaalRek(n-1)

print(faktoriaalRek(4))