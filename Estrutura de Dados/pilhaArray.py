class Node:
    item = None
    proximo = None

    def __init__(self, item):
        self.item = item

class Pilha:
    inicio = None
    tamanho = 0

    def __init__(self):
        self.inicio = Node(None)
    
    def estaVazia(self):
        if self.tamanho == 0:
            return True
        else:
            return False

    def push(self, item):
        p = self.inicio
        aux = Node(item)
        aux.proximo = p.proximo
        p.proximo = aux
        self.tamanho = self.tamanho + 1

    def pop(self):
        if (not self.estaVazia()):
            p = self.inicio
            aux = p.proximo
            item = aux.item
            self.inicio = self.inicio.proximo
            del aux
            self.tamanho = self.tamanho - 1
            return item
        else:
            print("Lista vazia.")
    
    def top(self):
        if (not self.estaVazia()):
            p = self.inicio
            aux = p.proximo
            item = aux.item
            return item
        else:
            print("Lista vazia.")

    
    def imprimir(self):
        p = self.inicio
        for i in range(self.tamanho):
            if p.proximo != None:
                p = p.proximo
                print(p.item)
        print("======")

#main
pilha = Pilha()
pilha.push(15)
pilha.push(5)
pilha.push(20)
pilha.push(37)

print("Removido", pilha.pop())
print("Topo")
pilha.imprimir()
