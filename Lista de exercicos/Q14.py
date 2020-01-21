ph = float(input('Report the level of acidity: '))

if ph>=0 and ph<7:
    print('Is acidic.')
elif ph>7 and ph<14:
    print('Is alkaline.')
elif ph == 7:
    print('Is neutral.')
else:
    print('Invalid value. Try again.')