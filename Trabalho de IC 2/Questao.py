
def binRecursivo (numero):
    if numero > 0:
        print(numero % 2)
        binRecursivo(numero // 2)


#################################################

binRecursivo(523)