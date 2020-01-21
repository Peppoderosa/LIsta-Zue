num = 0

while (num>=0):
    num = int(input('valor? '))
    if (num>=0):
        print('resultado: {}'.format(num**2))
    if (num == -1):
        break