n1 = int(input('Enter the first number? '))
n2 = int(input('Enter the second number? '))

for n in range(n1, n2):
    if n != n1 and n != n2:
        print(n)