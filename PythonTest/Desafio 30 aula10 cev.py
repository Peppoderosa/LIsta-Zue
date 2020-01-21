n = int(input('Numero? '))
c = '\033[m'
if n%2==0:
    print('\033[7;44mPar',c)
else:
    print('\033[7;41mImpar',c)