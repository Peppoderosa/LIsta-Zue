#compara cada um dos valores com o seu seguinte

def troca (i, j, lista):
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux

def bubble_sort(lista):
    cont = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                troca(i, i+1, lista)
                cont+=1
                swapped = True
    return lista, cont


print(bubble_sort([5,8,4,9,1,6,3,7]))