#pega valor por valor e compara com a lista ja pre ordenada, ate achar o lugar correto e então adiciona-lo nessa lista

def troca (i, j, lista):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def insert_sort(lista):
    for i in range(1, len(lista)):
        j = i
        while j>0 and lista[j] < lista[j-1]:
            troca(j, j-1, lista)
            j-=1
    return lista


print(insert_sort([5,8,4,9,1,6,3,7]))