def mult1(lista, n):
    list_result = []
    for i in lista:
        if i%n == 0:
            list_result.append(-1)
        else:
            list_result.append(i)

    print(list_result)

#################################################

lista = [2,6,3,9,10,11,15,18]
mult1(lista, 5)
