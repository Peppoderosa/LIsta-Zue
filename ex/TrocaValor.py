a = input('um valor? ')
b = input('outro valor? ')

p = a
a = b
b = p

print('\033[33m{}\n{}\033[m'.format(a,b))
