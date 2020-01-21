dicio = {}

chave = 1
nome = str(input('nome? (digite ~nao~ para parar) '))
while nome != 'nao':
    idade = str(input('idade? ')) 
    telefone = str(input('telefone? '))
    dicio[chave] = '{}-{}-{}'.format(nome, idade, telefone)
    chave += 1
    nome = str(input('nome? (digite ~nao~ para parar) '))

agenda = open('agenda.txt', 'w')
for i in dicio:
    agenda.write('{}: {}\n'.format(i, dicio[i]))

agenda.close()