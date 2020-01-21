class Pilha:
    elementos = None
    tam_max = None
    topo = None

    #criar pilha vazia
    def __init__(self, tam_max):
        self.tam_max = tam_max
        self.topo = 0
        self.elementos = [None] * tam_max

    #verificar se a pilha está vazia
    def estaVazia(self):
        if (self.topo == 0):
            return True
        else:
            return False
    
    #verificar se a pilha está cheia
    def estaCheia(self):
        if (self.topo == self.tam_max):
            return True
        else:
            return False

    #inserir/empilhar/push
    def push(self, item):
        if (not self.estaCheia()):
            self.elementos[self.topo] = item
            self.topo += 1
        else:
            print("A pilha está cheia.")

    #remover/desempilhar/pop
    def pop(self):
        if (not self.estaVazia()):
            self.topo -= 1
            item = self.elementos[self.topo]
            self.elementos[self.topo] = None
            return self.elementos[self.topo]
        else:
            print("Apilha está vazia.")

    # retornar o topo
    def top(self):
        if (not sel.estaVazia()):
            self.topo -= 1
            item = self.elementos[self.topo]
            self.topo += 1
            return item
        else:
            print("A pilha está vazia.")
    # imprimir a pilha
    def imprimir(self):
        for i in range(len(self.elementos)-1, -1, -1):
            print(self.elementos[i])
        print("=====")

#main
pilha = Pilha(5)
pilha.push(17)
pilha.push(15)
pilha.push(23)

pilha.imprimir()
pilha.pop()
pilha.imprimir()
pilha.pop()
pilha.imprimir()


