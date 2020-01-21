agenda = [['Ana', '99999-1234'], ['Bia', '99999-5678']]

p = 'd'
while p != 'c':
    print('(a) Adicionar telefones na agenda')
    print('(b) Procurar um telefone')
    print('(c) Sair')
    p = str(input('-> '))
    if p == 'a':
        nome = str(input('Digite o nome? '))
        numero = str(input('Digite o numero? '))
        aux = ['','']
        aux[0] = nome
        aux[1] = numero
        agenda.append(aux)
        agenda = sorted(agenda)
        print('Adicionado.\n')
    elif p == 'b':
        nome = str(input('Digite o nome? '))
        b = False
        for i in agenda:
            if i[0] == nome:
                print(i[1])
                b = True
        if b == False:
            print('Não está na agenda.')

print(agenda)
