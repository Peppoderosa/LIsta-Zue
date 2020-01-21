def highSum (lista):
    lista = sorted(lista)
    return lista[-1] + lista[-2]

print(highSum([3,2,5]))