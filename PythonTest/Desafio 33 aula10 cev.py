n1 = int(input('Primeiro numero? '))
n2 = int(input('Segundo numero? '))
n3 = int(input('Terceiro numero? '))

if n1>n2 and n1>n3 and n2>n3:
    print('{} é maior e {} é o menor'.format(n1, n3))
elif n2>n1 and n2>n3 and n1>n3:
    print('{} é maior e {} é o menor'.format(n2, n3))
elif n3>n1 and n3>n2 and n1>n2:
    print('{} é maior e {} é o menor'.format(n3, n2))
elif n3>n1 and n3>n2 and n2>n1:
    print('{} é maior e {} é o menor'.format(n3, n1))
elif n2>n1 and n2>n3 and n3>n1:
    print('{} é maior e {} é o menor'.format(n2, n1))
elif n1>n2 and n1>n3 and n3>n2:
    print('{} é maior e {} é o menor'.format(n1, n2))
else:
    print('Tem numero igual aí. Tenta novamente.')
