escale = str(input('Which scale of you value? \nc - Celcius\nf - Fahrenheit\nk - Kelvin\n--> '))
temp = float(input('And what the value? '))

if escale == 'c':
    print('This value in Fahrenheit is: ', (9*temp+160)/5)
    print('This value in Kelvin is: ', temp+273.15)
if escale == 'f':
    print('This value in Celcius is: ', (5*temp-160)/9)
    print('This value in Kelvin is: ', ((5*temp-160)/9) + 273.15)
if escale == 'k':
    print('This value in Celcius is: ', temp - 273.15)
    print('This value in Fahrenheit is: ', (9*(temp-273.15)+160)/5)