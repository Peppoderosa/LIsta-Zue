import random
import array

c = '\033[m'


n1 = input('primeiro nome? ')
n2 = input('segundo nome? ')
n3 = input('terceiro nome? ')
n4 = input('quarto nome? ')

lista = [n1, n2, n3, n4]

n = random.randint(0,3)
print('\033[7m',lista[n],c)
lista.pop(n)

n = random.randint(0,2)
print('\033[7;31m',lista[n],c)
lista.pop(n)

n = random.randint(0,1)
print('\033[7;33m',lista[n],c)
lista.pop(n)

print('\033[7;36m',lista[0],c)