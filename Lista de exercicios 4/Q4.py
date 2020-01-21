def mmc(n, m):
    listPrimo  = []
    listResult = []
    if n >= m:
        for i in range(0, n+1):
            if primo(i):
                listPrimo.append(i)
        for x in listPrimo:
            for a in range(0, n):
                if n%x == 0 and m%x == 0:
                    n = int(n / x)
                    m = int(m / x)
                    listResult.append(x)
                elif n%x == 0:
                    n = int(n / x)
                    listResult.append(x)
                elif m%x == 0:
                    m = int(m / x)
                    listResult.append(x)
    elif n < m:
        for i in range(0, m+1):
            if primo(i):
                listPrimo.append(i)
        for x in listPrimo:
            for a in range(0, m):
                if n%x == 0 and m%x == 0:
                    n = int(n / x)
                    m = int(m / x)
                    listResult.append(x)
                elif n%x == 0:
                    n = int(n / x)
                    listResult.append(x)
                elif m%x == 0:
                    m = int(m / x)
                    listResult.append(x)
    f = 1
    for b in listResult:
        f = f*b

    return f

#################################################

def primo(n):
    c = 0
    for i in range(1, n+1):
        if n%i == 0:
            c += 1
    if c == 2:
        return True
    else:
        return False

#################################################

print(mmc(8,6))