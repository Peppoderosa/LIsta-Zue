mercearia = {1:5.30, 2:6.00, 3:3.20, 4:2.50}

codigo = int(input('Código do produto? '))
quantidade = int(input('Quantidade? '))

total = mercearia[codigo]*quantidade

if total >= 40 or quantidade >= 15:
    total = total*0.85

print('{:.2f}'.format(total))