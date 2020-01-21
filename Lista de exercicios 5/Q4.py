def media(nome):
    listaNotas = dicio[nome]
    return (listaNotas[0]+listaNotas[1])/2

#################################################

def lerNotas():
    notas = [0,0]
    notas[0] = float(input('Digite a primeira nota? '))
    notas[1] = float(input('Digite a segunda nota? '))
    return notas

#################################################

dicio = {}

nome = str(input('Digite o nome? '))
while nome != '':
    notas = lerNotas()
    dicio[nome] = notas 
    nome = str(input('Digite o nome? '))

nome = str(input('Digite o nome para saber a média? '))
while nome != '':
    print(media(nome))
    nome = str(input('Digite o nome para saber a média? '))
    