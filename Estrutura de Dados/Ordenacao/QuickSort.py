#dividir para conquistar

def troca (i, j, lista):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def quick_sort(lista):
    if len(lista) == 1:
        return lista
    else :
        for i in range(len(lista)):
            quick_sort()



print(quick_sort([5,8,4,9,1,6,3,7]))