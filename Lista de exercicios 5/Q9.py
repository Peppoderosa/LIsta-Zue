def maisVelho(dicio):
    maior = 0
    for i in dicio.keys():
        if i > maior:
            maior = i
    return 'Mais velho: {}'.format(maior)

#################################################

def flv1835(dicio):
    c = 0
    t = 0
    for i in dicio.keys():
        t += 1
        if i >= 18 and i <= 35:
            if dicio[i][0] == 'f':
                if dicio[i][1] == 'l':
                    if dicio[i][2] == 'v':
                        c +=1
    return 'Mulheres com olhos verdes, loiras com 18 a 35 anos: {:.2f}%'.format((c*100)/t)



#################################################

dicio = {}

v = int(input('Idade? '))
while v != -1:
    dicio[v] = str(input('Sexo(m/f), Cabelos (l/c/p), Cor dos olhos (a/v/c), respectivamente? '))
    v = int(input('Idade? '))

print(maisVelho(dicio))
print(flv1835(dicio))