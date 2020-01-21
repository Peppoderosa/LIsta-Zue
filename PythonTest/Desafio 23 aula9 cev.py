n = input('Digite um número de 0 a 9999? ')

c = n.replace('', ' ').split()

print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(c[3],c[2], c[1], c[0]))