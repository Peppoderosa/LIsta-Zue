year = int(input('Say a year? '))

if year%4 == 0:
    if year%100 !=0 or year%400 == 0:
        print('This year is "bissexto"*.')
    else:
        print("This year ISN'T 'Bissexto'*.")
else:
    print("This year ISN'T 'Bissexto'*.")

# *não sei como dizer bissexto em inglês