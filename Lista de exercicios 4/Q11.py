def list_str(lista):
    high = ''
    for i in range(0, len(lista)):
        if len(lista[i]) > len(high):
            high = lista[i]

    vogais = 'aeiou'
    countV = 0
    for x in lista:
        aux = x.strip()
        for y in vogais:
            for z in aux:
                if y == z:
                    countV += 1

    countE = 0
    for x in lista:
        aux = x.strip()
        for z in aux:
            countE += 1

    count1 = 0
    for w in lista:
        if w == lista[0]:
            count1 += 1

    return "'{}' | {:.3f} | {}".format(high, (countV/countE), count1)


#################################################

frase = ['by','the','last','breath','of','the','fourth','winds','blow']
print(list_str(frase))