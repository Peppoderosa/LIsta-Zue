def maisDeSeisMedias(dicioNotas):
    for i in dicioNotas:
        if len(dicio[i]) >= 6:
            print(i)

#################################################
def media(dicioNotas):
    arq2 =open('media.txt', 'a')
    soma = 0
    for i in dicioNotas:
        for x in dicio[i]:
            soma += int(x)
        arq2.write(i+': '+str(soma/len(dicio[i]))+'\n')
        soma = 0
    arq2.close()

#################################################

arq1 = open('notas.txt', 'r')
aux1 = arq1.readlines()
dicio = {}
nome = ''
listaNotas = []
for i in aux1:
    aluno = i.split('\n')
    for x in aluno:
        notas = x.split()
        for z in notas:
            if z.isnumeric():
                listaNotas.append(z)
            else:
                nome = z
        dicio[nome]= listaNotas
    listaNotas = []

arq1.close()

#a)
print('Alunos com mais de 6 notas:')
maisDeSeisMedias(dicio)

#b)
media(dicio)