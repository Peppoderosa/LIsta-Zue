def traduzir (lista):
    cifra = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    traducao = ''
    for i in lista:
        for x in cifra:
            if i == cifra.index(x):
                traducao += x

    print(traducao)

#################################################

frase = [2,15,13,0,4,9,1]
traduzir(frase)