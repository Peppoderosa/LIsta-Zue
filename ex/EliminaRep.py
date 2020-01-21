def possui (l, v):
    for i in l:
        if i == v:
            return True
    return False

def copia_Lista(l):
    lAux = []
    for i in l:
        if (possui(l, i) != False):
            lAux.append(i)
    return lAux

lista = [2,2,3,3,3,8,6]
print(copia_Lista(lista))