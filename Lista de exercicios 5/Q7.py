def lerMatriz ():
    lista1 = []
    matriz = []
    l = int(input('Quantas linhas terá a matriz? '))
    c = int(input('Quantas colunas terá a matriz? '))
    for i in range(l):
        for x in range(c):
            n = int(input('número? '))
            lista1.append(n)
        matriz.append(lista1)
        lista1 = []
    return matriz

#################################################

def imprimaMatriz(matriz):
    for i in matriz:
        print(i)

#################################################

def multiplicaMatrizes(matrizA, matrizB):
    matrizR = gerarMatriz(len(matrizA[0]), len(matrizB[0]))
    for l in range(len(matrizA[0])):
        for c in range(len(matrizB)):
            for z in range(len(matrizA)):
                matrizR[l][c] += matrizA[l][z] * matrizB[z][c]
    return matrizR

#################################################

def gerarMatriz (l, c):
    lista1 = []
    matriz = []
    for i in range(l):
        for x in range(c):
            lista1.append(0)
        matriz.append(lista1)
        lista1 = []
    return matriz

#################################################

def identidade(matriz):
    n = matriz[0][0]
    b = False
    for i in range(len(matriz)):
        if matriz[i][i] == n:
            b += 1

    if b == len(matriz[0]):
        print('É identidade.')
    else:
        print('Não é identidade.')

#################################################

matrizA = lerMatriz()
matrizB = lerMatriz()
#matrizI = [[2,9,1],[7,2,2],[6,5,2]]
matrizM = multiplicaMatrizes(matrizA, matrizB)
identidade(matrizM)
imprimaMatriz(matrizM)