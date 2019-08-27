def fattoriale(x):
    if x == 0:
        return 1
    else:
        return x * fattoriale(x-1)