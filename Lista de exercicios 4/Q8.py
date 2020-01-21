def lista_rel (lista1, lista2):
    lista_uni = lista1 + lista2
    print(lista_uni)

    lista_int = []
    for i in lista1:
        for x in lista2:
            if i == x:
                lista_int.append(x)
    if len(lista_int) > 0:
        print(lista_int)
    else:
        print('No intersection.')

    lista_intercalada = []
    if len(lista1) > len(lista2):
        for c in range(0, len(lista2)):
            lista_intercalada.append(lista1[c])
            lista_intercalada.append(lista2[c])
    elif len(lista1) < len(lista2):
        for c in range(0, len(lista1)):
            lista_intercalada.append(lista1[c])
            lista_intercalada.append(lista2[c])
    print(lista_intercalada)


#################################################

a = [7,0,9]
b = [2,0,1,5,8,6,3,4]

lista_rel(a, b)
