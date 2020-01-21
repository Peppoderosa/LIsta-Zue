number1 = int(input('One number? '))
number2 = int(input('Other number? '))

if number1>number2:
    print('{} is biggest'.format(number1))
elif number2>number1:
    print('{} is biggest'.format(number2))
else:
    print('They are equals')