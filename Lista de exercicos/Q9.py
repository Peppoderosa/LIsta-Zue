weight = float(input('What the fish weight?(kg) '))

if weight > 50:
    exedent = weight-50
    print('You will pay ${} to fine for overweight'.format(exedent*4))
else: 
    print('You dont need pay an fine for overweight')