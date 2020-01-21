lista = [1,3,8,4,6,10,8]
n = 25
i = 0
soma = 0

while(i<len(lista) and soma <= n):
    soma = soma + list[i]
    i = i+1

if (i == len(lista)):
    print('não')
else:
    print('sim')
        