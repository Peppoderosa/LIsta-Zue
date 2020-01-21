def ordena (lista):
    for i in range(0, len(lista) - 1):
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                x = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = x

    return lista

#################################################

lista = [5,3,11,15,2,4,1,0]
print(ordena(lista))