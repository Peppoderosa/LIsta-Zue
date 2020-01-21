b = float(input('Valor do boleto: '))
d = float(input('Dias de atraso: '))

print('Total a pagar: {}'.format(b+2+(b*0.05*d)))