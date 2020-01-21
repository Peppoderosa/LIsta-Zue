ips = open('ips.txt', 'r')
enderecos = ips.readlines()
ips.close()
validar = True
ipsValidos = []
ipsInvalidos = []

for i in enderecos:
    unico = i.split('.')
    for x in unico:
        if int(x) >= 256 or int(x) < 0:
            validar = False
    if validar == False:
        ipsInvalidos.append(i)
    else:
        ipsValidos.append(i)
    validar = True

ips.close()

resultadoIps = open('resultadoIps.txt', 'w')
resultadoIps.write('[Enderecos validos:]\n')
for i in ipsValidos:
    resultadoIps.write(i)
resultadoIps.write('\n[Enderecos invalidos:]\n')
for i in ipsInvalidos:
    resultadoIps.write(i)

resultadoIps.close()
