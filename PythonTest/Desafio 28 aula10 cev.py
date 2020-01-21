import random

n = random.randint(0,5)

np = int(input('Adivinhe o numero de 0 a 5? '))

if n == np:
    print('Acertou, Mizeravi!')
else:
    print('Não, mano')
print(n)
