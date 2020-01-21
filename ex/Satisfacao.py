n = int(input('Number? '))

if (n<100 and n>10) and ((n%2==0 or n%3==0) and n%5==0):
     print('Satisfied')
else: 
    print("Don't satisfied")