n1 = int(input('Primeira reta? '))
n2 = int(input('Segunda reta? '))
n3 = int(input('Terceira reta? '))

c = '\033[m'

'''
ma = 0
me = 0
i = 0

if n1>n2 and n1>n3 and n2>n3:
    #print('{} é maior e {} é o menor'.format(n1, n3))
    ma = n1
    me = n3
    i = n2
elif n2>n1 and n2>n3 and n1>n3:
    #print('{} é maior e {} é o menor'.format(n2, n3))
    ma = n2
    me = n3
    i = n1
elif n3>n1 and n3>n2 and n1>n2:
    #print('{} é maior e {} é o menor'.format(n3, n2))
    ma = n3
    me = n2
    i = n1
elif n3>n1 and n3>n2 and n2>n1:
    #print('{} é maior e {} é o menor'.format(n3, n1))
    ma = n3
    me = n1
    i = n2
elif n2>n1 and n2>n3 and n3>n1:
    #print('{} é maior e {} é o menor'.format(n2, n1))
    ma = n2
    me = n1
    i = n3
elif n1>n2 and n1>n3 and n3>n2:
    #print('{} é maior e {} é o menor'.format(n1, n2))
    ma = n1
    me = n2
    i = n3
else:
    print('Tem erro aí. Tenta novamente.')



if me+i<ma:
    print('É possível formar triângulo')
else:
    print('Não é Possível formar triângulo')

'''

if abs(n2-n3 < n1) and n1 < n2+n3:
    if abs(n1-n3 < n2) and n2 < n1+n3:
        if abs(n1-n2 < n3) and n3 < n1+n2:
            print('\033[4;35mÉ\033[m possível formar um triângulo')
else:
    print('\033[4;33mNão é\033[m possível formar um triângulo')

