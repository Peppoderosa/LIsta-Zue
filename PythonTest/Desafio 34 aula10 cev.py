s = float(input('Salario atual? '))

if s>1250:
    print('Seu novo salario é {}{:.2f}{}'.format('\033[7;43m',s*1.1,'\033[m'))
else:
    print('Seu novo salário é {}{:.2f}{}'.format('\033[7;43m',s*1.15,'\033[m'))