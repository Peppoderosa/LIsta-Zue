def binario (number):
    binList = ''
    while number != 0:
        binList += str(number%2)
        number = number//2

    resultado = ''
    v = len(binList)-1
    for i in binList:
        resultado += binList[v]
        v -= 1

    return resultado

#################################################
def octal (number):
    octList = ''
    while number != 0:
        octList += str(number%8)
        number = number//8

    resultado = ''
    v = len(octList)-1
    for i in octList:
        resultado += octList[v]
        v -= 1

    return resultado

#################################################
def hexadecimal(number):
    hexList = []
    while number != 0:
        hexList.append(number%16)
        number = number//16

    nova_lista = []
    l = 'ABCDEF'
    v = [10,11,12,13,14,15]
    for x in hexList:
        for y in v:
            if x == y:
                x = (l[y-10])
        nova_lista.append(x)

    resultado = ''
    v = len(nova_lista) - 1
    for i in nova_lista:
        resultado += str(nova_lista[v])
        v -= 1

    return resultado

#################################################

n = int(input('Número? '))
base = int(input('Qual a base(2/8/16)? '))
if base == 2:
    print(binario(n))
elif base == 8:
    print(octal(n))
elif base == 16:
    print(hexadecimal(n))