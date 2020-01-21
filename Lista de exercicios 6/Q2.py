arq = open('ParesDecrescentes.txt', 'w')
c = 198
for i in range(100):
    arq.write(str(c)+'\n')
    c -= 2
arq.close()