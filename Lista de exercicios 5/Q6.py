def lerMatriz ():
    lista1 = []
    matriz = []
    for i in range(6):
        for x in range(3):
            n = int(input('numero? '))
            lista1.append(n)
        matriz.append(lista1)
        lista1 = []
    return matriz

#################################################

def maiorElemento(matriz):
    maior = 0
    posicao = [0,0]
    for i in matriz:
        for x in i:
            if x > maior:
                maior = x
                posicao[0] = i.index(x)
                posicao[1] = matriz.index(i)
    posicaoReal = '{} é o maior número, que fica na {}° linha e na {}° Coluna.'.format(maior, posicao[1]+1, posicao[0]+1)
    return posicaoReal

#################################################

def menorElemento(matriz):
    menor = 999999999
    posicao = [0,0]
    for i in matriz:
        for x in i:
            if x < menor:
                menor = x
                posicao[0] = i.index(x)
                posicao[1] = matriz.index(i)
    posicaoReal = '{} é o menor número, que fica na {}° linha e  na {}° Coluna.'.format(menor, posicao[1]+1, posicao[0]+1)
    return posicaoReal

#################################################

matriz = lerMatriz()

print(maiorElemento(matriz))
print(menorElemento(matriz))

for i in matriz:
    print(i)
