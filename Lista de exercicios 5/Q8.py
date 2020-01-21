def subonjunto(listaA, listaB):
    c = 0
    for i in listaA:
        if i in listaB:
            c += 1

    if c == len(listaB):
        print(True)
    else:
        print(False)

#################################################

def convertParaLista(lista):
    newLista = []
    for i in lista[0]:
        if i.isnumeric():
            newLista.append(int(i))
    return newLista

#################################################

listaA = []
listaB = []

n = int(input('Qual o tamanho da primeira lista? '))
listaA.append(list(input('Primeira lista? '))) # Entrada do tipo: '[n, n, n]'

m = int(input('Qual o tamanho da segunda lista? '))
listaB.append(list(input('Segunda lista? '))) # Entrada do tipo: '[m, m]'

listaA = convertParaLista(list(listaA))
listaB = convertParaLista(list(listaB))

subonjunto(listaA, listaB)