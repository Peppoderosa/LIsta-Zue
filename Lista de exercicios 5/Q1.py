import random
def lancar():
    return random.randint(1,6)

#################################################

def conta(lista):
    quanti = [0,0,0,0,0,0]
    for i in lista:
        if i == 1:
            quanti[0] = quanti[0]+1
        elif i == 2:
            quanti[1] = quanti[1]+1
        elif i == 3:
            quanti[2] = quanti[2]+1
        elif i == 4:
            quanti[3] = quanti[3]+1
        elif i == 5:
            quanti[4] = quanti[4]+1
        elif i == 6:
            quanti[5] = quanti[5]+1
            
    return quanti

#################################################

saida = []
quant = []

for i in range(0,10):
    saida.append(lancar())

quant = conta(saida)

print(saida)
print(quant)
