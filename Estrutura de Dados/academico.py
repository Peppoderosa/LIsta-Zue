class Aluno: # definição da classe
    nome = " " # atrbuto
    matricula = " "
    nota = [0, 0]

    # construtor
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def media(self):
        notas = self.nota
        return (notas[0]+notas[1])/2

#main

a1 = Aluno("Mick", "524135", [5,9])

print(a1.media())