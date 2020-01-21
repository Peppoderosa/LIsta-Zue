def sed(stringPad, stringSub, nome1, nome2):
    arq1 = open('{}.txt'.format(nome1), 'r')
    arq2 = open('{}.txt'.format(nome2), 'w')
    aux1 = arq1.readlines()
    listaAux = []
    for i in aux1:
        linha = i.split('\n')
        for x in linha:
            linha2 = x.split()
            for z in linha2:
                if z == stringPad:
                    listaAux.append(stringSub)
                else:
                    listaAux.append(z)
            arq2.write(' '.join(listaAux))
            listaAux = []
        arq2.write('\n')

    arq1.close()
    arq2.close()

#################################################
stringPad = 'Nutella'
stringSub = 'Pacoca'
nomeP = 'primeiroArquivo'
nomeS = 'segundoArquivo'

sed(stringPad, stringSub, nomeP, nomeS)

