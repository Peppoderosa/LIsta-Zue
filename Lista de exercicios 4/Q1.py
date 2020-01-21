def nTimes (n):
    linha = ''
    for x in range(1, n+1):
        for i in range(0, x):
            linha += str(x) + ' '
        print(linha)
        linha = ''

#################################################

nTimes(10)