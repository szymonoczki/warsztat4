def potega(n):
    if n < 0:
        n = n * -1
    if n != 0:
        return n+n-1+potega(n-1)
    return 0
