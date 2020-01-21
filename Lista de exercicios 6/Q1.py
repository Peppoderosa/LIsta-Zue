arq = open('crescente.txt', 'w')
for i in range(1, 101):
    arq.write(str(i)+'; ')
arq.close()