listaNum = [2,3,4,5,6,7]
s = 0
for n in range(0,len(listaNum)):
    if listaNum[n]%2==0:
        s = s + listaNum[n]
print(s)