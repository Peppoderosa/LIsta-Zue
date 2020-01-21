def size (lista):
    c = 0
    for i in lista:
        c += 1
    return c

#################################################

def maxValue (lista):
    for i in range(0, len(lista) - 1):
        for i in range(0, len(lista) - 1):
            if lista[i] > lista[i + 1]:
                x = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = x

    return lista[-1]

#################################################

def minValue (lista):
    for i in range(0, len(lista) - 1):
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                x = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = x

    return lista[0]

#################################################

def binValue (number):
    binList = []
    while number != 0:
        binList.insert(0, number%2)
        number = number//2

    return binList

#################################################

ex = [5,2,13,1,8,15]

print(size(ex))
print(maxValue(ex))
print(minValue(ex))
print(binValue(ex[2]))
