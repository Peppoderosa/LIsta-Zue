def armazena(nome, email, curso):
    arq = open('cadastroAlunos.txt', 'a')
    arq.write(nome+' | '+email+' | '+curso+'\n')
    arq.close()

#################################################

def mostraNomes():
    arq = open('cadastroAlunos.txt', 'r')
    nomes = arq.readlines()
    for i in nomes:
        aux = i.split('|')
        print(aux[0])
    arq.close()

#################################################

opc = 0

while opc != 3:
    print('1 - Para cadastrar aluno novo')
    print('2 - Para listar alunos cadastrados')
    print('3 - Para sair')
    opc = int(input('-> '))
    if opc == 1:
        nome = str(input('Nome? '))
        email = str(input('E-mail? '))
        curso = str(input('Curso? '))
        armazena(nome, email, curso)
    elif opc == 2:
        mostraNomes()
    elif opc != 3 and opc != 2 and opc != 1:
        print('Opção inválida.')

