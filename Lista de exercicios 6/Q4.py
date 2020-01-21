def armazena(nome, telefone):
    arq = open('contatos.txt', 'a')
    arq.write(nome+' - '+telefone+'\n')
    arq.close()

#################################################

def mostraNomes():
    arq = open('contatos.txt', 'r')
    nomes = arq.readlines()
    for i in nomes:
        aux = i.split('-')
        print(aux[0])
    arq.close()

#################################################

nome = str(input('Nome? '))

while nome != 'sair':
    telefone = str(input('Telefone? '))
    armazena(nome, telefone)
    nome = str(input('Nome? '))

mostraNomes()