n = int(input('Enter a number? '))
fibo = [1,1]

for i in range(2, n):
    fibo.append(fibo[i-1]+fibo[i-2])

for x in range(0,n):
    print(fibo[x])