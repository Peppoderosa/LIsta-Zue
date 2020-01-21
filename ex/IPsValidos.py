ips = open('ips.txt', 'r')
enderecos = ips.readlines()
ips.close()
validar = True
for i in enderecos:
    unico = i.split('.')
    for x in unico:
        if int(x) > 224:
            validar = False
    if validar == False:
        print('Invalido', unico)
    else:
        print('Valido', unico)
    validar = True