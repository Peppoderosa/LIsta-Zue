d = float(input('Qual a distância? '))

if d <= 200:
    print('Preço a pagar: {}'.format(d*0.5))
else:
    print('Preço a pagar: {}'.format(d*0.45))