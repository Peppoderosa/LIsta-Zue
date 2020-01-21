#Josué Luiz Leite Silva, Trabalho prático CSD, CC 2019.1
entrada = str(input())

ruaA = int(entrada[0])
ruaB = int(entrada[2])
ruaC = int(entrada[4])
sinal = "A"
if (ruaA == 0 and ruaB == 0 and ruaC == 0):
    sinal = "Rua A"
elif (ruaA > 0 and ruaB > 0 and ruaC > 0):
    sinal = "Rua A"
elif (ruaA > 0 and ruaC == 0):
    sinal = "Rua A"
elif (ruaB > 0 and ruaA == 0):
    sinal = "Rua B"
elif (ruaC > 0 and ruaB == 0):
    sinal = "Rua C"


print(sinal)