#se

def troca (i, j, lista):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def select_sort(lista):
    for j in range(1, len(lista)):
        menor = j
        for i in range(len(lista)-1):
            if lista[i] < lista[menor]:
                menor = i
        troca(j, menor, lista)
    return lista



print(select_sort([5,8,4,9,1,6,3,7]))