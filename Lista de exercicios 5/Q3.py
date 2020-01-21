def contaVogal(texto):
    dicio = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    dicio['a'] = contaLetra('a', texto)
    dicio['e'] = contaLetra('e', texto)
    dicio['i'] = contaLetra('i', texto)
    dicio['o'] = contaLetra('o', texto)
    dicio['u'] = contaLetra('u', texto)

    return dicio

#################################################

def contaLetra(l, t):
    c = 0
    for i in t:
        if i == l:
            c += 1
    return c

#################################################

frase = 'by the last breath of the fourth winds blow'
print(contaVogal(frase))
