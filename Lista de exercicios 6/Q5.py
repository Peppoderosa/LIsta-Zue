def copiaArquivos(nome1, nome2):
    arq1 = open('{}.txt'.format(nome1), 'r')
    arq2 = open('{}.txt'.format(nome2), 'w')
    arq2.write(arq1.read())
    arq1.close()
    arq2.close()

#################################################

nomeP = 'primeiroArquivo'
nomeS = 'segundoArquivo'

copiaArquivos(nomeP, nomeS)

