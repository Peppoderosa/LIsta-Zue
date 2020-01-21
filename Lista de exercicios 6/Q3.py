arq = open('nomes.txt', 'a')
nome = str(input('Nome? '))
while nome != 'sair':
    arq.write(nome.upper()+'\n')
    nome = str(input('Nome? '))
arq.close()