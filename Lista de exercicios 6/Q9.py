def binToDecimal (number):
    binList = []
    num = str(number)
    for i in range(len(num)):
        binList.append(int(num[i]))

    valor = 0
    r = len(binList)-1
    for x in range(len(binList)):
        valor += binList[r]*(2**x)
        r -= 1

    return valor

#################################################
arq = open('binarios.txt', 'r')
numeros = arq.readlines()
for i in numeros:
    aux = i.split('\n')
    print(aux[0],'->', binToDecimal(int(aux[0])))
arq.close()