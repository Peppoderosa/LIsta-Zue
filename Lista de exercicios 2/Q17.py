n = int(input('Enter a number (0-9)? '))
if (n < 9) and (n > 0):
    for i in range(0,10):
        print(n)
        n += 10
else:
    print('Invalid number.')