iden = open('identidades.txt', 'r')
dicio = {}
size = len(iden.readlines())
iden.close()
iden = open('identidades.txt', 'r')
for i in range(size):
    linha = iden.readline()
    dicio[linha[:7]] = linha[8:]

iden.close()
print(dicio)
print(size)