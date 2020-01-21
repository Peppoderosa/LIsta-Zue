import random
n1 = input('primeiro nome? ')
n2 = input('segundo nome? ')
n3 = input('terceiro nome? ')
n4 = input('quarto nome? ')

n = random.randint(1,4)

if (n == 1):
    print(n1)
elif (n == 2):
    print(n2)
elif (n == 3):
    print(n3)
elif (n == 4):
    print(n4)
else:
    print('Tente novamente.')