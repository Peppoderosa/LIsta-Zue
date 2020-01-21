grade = (input('Enter a grade (0 to 10)? '))
if grade.isnumeric():
    n = float(grade)
    if n >= 0 and n <= 10:
        print('OK')
    else:
        print('Error!')
else:
    print('Error!')
