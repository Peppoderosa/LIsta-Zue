def contaVogal(texto):
    dicio = {}
    dicio['a'] = texto.count('a')
    dicio['i'] = texto.count('i')
    dicio['e'] = texto.count('e')
    dicio['u'] = texto.count('u')
    dicio['o'] = texto.count('o')
    
    return dicio

frase = 'by the last breath of the fourth winds blow'
print(contaVogal(frase))
