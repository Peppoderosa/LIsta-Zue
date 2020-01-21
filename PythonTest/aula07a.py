n1 = int(input('numero? '))
n2 = int(input('outro numero? '))

s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

print('soma: {}, \n o produto: {} \n e a divisão: {:.3f}'.format(s,m,d), end=' -> ')
print('divisão inteira: {} e a potencia: {}'.format(di,e))
