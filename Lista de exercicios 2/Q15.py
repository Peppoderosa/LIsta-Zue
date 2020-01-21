while (True):
    i = int(input('Enter an odd number? '))
    if i % 2 != 0:
        a = (i//2)+i%2
        b = i//2
        print('{}-{}={}'.format(a*a,b*b,i))
        break
    else:
        print("Is not an odd number.")