days = int(input('How many days will you stay with the car? '))
kilometer = float(input('And how many kilometer will you drive? '))

print('You will pay: ${}'.format((days*30)+(kilometer*0.01)))