n1 = int(input('What is the base? '))
n2 = int(input('What is the exponent? '))
s = 1

for i in range(0,n2):
    s = s*n1

print('{} ^ {} = {}'.format(n1, n2, s))