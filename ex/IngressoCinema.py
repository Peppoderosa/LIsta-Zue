age = float(input('Tell your age? '))
ocupation = str(input('And your ocupation? '))

if age>18 and age<60:
    if ocupation == 'student':
        print('You pay $12')
    elif ocupation == 'teacher':
        print('You pay $15')
    else:
        print('You pay $20')
else:
    print('You pay $10')
