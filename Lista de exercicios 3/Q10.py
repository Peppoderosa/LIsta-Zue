def intencao (candidato, concorrente, n):
    resultadoAnt = 0.00
    for i in range(0, n):
        if candidato[i] > concorrente[i]:
            resultado = float(candidato[i]) - float(concorrente[i])
            if resultado > resultadoAnt:
                resultadoAnt = resultado

    print('{:.2f}'.format(resultadoAnt))

#################################################

'''
quant = 7
candidato = [10.3,15.3,17.5,19.4,22.5,22.6,22.3]
concorrente = [20.4,18.2,16.3,15.8,14.5,14.9,15.6]
'''

n = int(input('Enter the number of researches? '))
candidato = str(input("Enter the researches of 'Candidato'? "))
concorrente = str(input("Enter the researches of 'Concorrente'? "))
for i in candidato:
    if i == '[' or i == ']':
        candidato = candidato.replace(i, '')
for i in concorrente:
    if i == '[' or i == ']':
        concorrente = concorrente.replace(i, '')

candidato = candidato.split(',')
concorrente = concorrente.split(',')
newCandidato = []
newConcorrente = []
for i in candidato:
    newCandidato.append(float(i))
for i in concorrente:
    newConcorrente.append(float(i))

intencao(candidato, concorrente, n)
