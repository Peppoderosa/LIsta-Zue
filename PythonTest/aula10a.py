'''
n = str(input('Nome? '))

if n == 'jon':
    print('massa')
else:
    print('OK')
print('olá, {}'.format(n))
'''

n1 = float(input('Primeira nota? '))
n2 = float(input('Segunda nota? '))

m  = (n1+n2)/2

print('A média foi {}'.format(m))
print('Massa' if m>=6 else 'Não massa')

