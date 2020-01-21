#antececor e sucessor
'''
while True:
    n = int(input('digite um numero inteiro: '))
    if n == -1:
        break
    print("%d %d" % (n-1, n+1))
'''
from datetime import datetime 
from random import randint


start = datetime.now()
print("%d hr %d min %d seg %d mic" % (start.hour, start.minute, start.second, start.microsecond))

n_item = 100000000
lista = []
for i in range(n_item):
    n = randint(0, 10)
    lista.append(n)

end = datetime.now()
print("%d hr %d min %d seg %d mic" % (end.hour, end.minute, end.second, end.microsecond))

print(end.microsecond - start.microsecond)