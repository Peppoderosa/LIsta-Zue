from operator import itemgetter

def lerTempo():
    listaTempo = [0]*10
    for i in range(0, 10):
        listaTempo[i] = float(input('Digite um tempo? '))
    return listaTempo

#################################################

def lerCorredor(dicio):
    nome = str(input('Digite o nome do corredor? '))
    dicio[nome] = lerTempo()
    return dicio

#################################################

def voltaMaisRapida(dicio):
    menor = 9999999999
    dono = ''
    ind = 0
    for i in dicio:
        for x in dicio[i]:
            if x < menor:
                menor = x
                dono = i
                ind = dicio[i].index(x)

    return 'A volta mais rápida foi a {}° volta de {}, com {}s.'.format(ind+1, dono, menor)

#################################################

def campeao(dicio):
    tabela = {}
    soma = 0
    for i in dicio:
        for x in dicio[i]:
            soma = soma + x
        tabela[i] = soma/len(dicio[i])
        soma = 0

    tabelaFinal = sorted(tabela.items(), key=itemgetter(1))

    posicao = 1
    for y in tabelaFinal:
        print('{}° lugar:  {} (media de tempo :{:.2f}s)'.format(posicao, y[0], y[1]))
        posicao +=1

#################################################

dicioTempo = {}

for i in range(0,6):
    lerCorredor(dicioTempo)

print(voltaMaisRapida(dicioTempo))
campeao(dicioTempo)
