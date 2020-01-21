class Pessoa: # definição da classe
    nome = "" # atrbuto
    idade = 0

    # construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Nome: " + self.nome

    def apresentacao(self):
        return "Olá, " + self.nome + " e tenho " + str(self.idade)

#main

p1 = Pessoa("Jon", 25) # p1 é o identificador e Pessoa() é o tipo
p2 = Pessoa("Mary", 20)

print(p1.apresentacao())
print(p2.apresentacao())