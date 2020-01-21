'''
lista1 = range(1,6)
lista2 = range(6,11)
#lista1[len(lista1):] = lista2
lista1 = lista1 + lista2

tupla = ('jose','rua 15',152)
nome, rua, numero = tupla
#print(nome, rua, numero)

numeros = [12,3,5,4,3,8,9,1,3]
conjunto = set(numeros)
print(conjunto)
print(3 in conjunto)
print(2 in conjunto)
'''

telefones = {'jose':2545,'pedro':5214,'ana':5522}
print(telefones)
print(telefones['ana'])
print(sorted(telefones))
print(telefones.keys())
print(2545 in telefones.values())
