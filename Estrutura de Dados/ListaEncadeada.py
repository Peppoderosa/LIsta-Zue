#lista encadeada
#Autor desconhecido
class Node: 
    item = None
    proximo = None

    def __init__(self,item):
        self.item = item
        


class Lista_Encadeada:
    inicio = None
    tam = 0

    def __init__(self):
        self.inicio = Node(None)

    def listavazia(self):
        return (self.tam == 0)

        #inserir em uma posição
    def inserir(self, item, pos=0):
        if (pos <= self.tam):
            p = self.inicio
            for i in range(pos):
                p = p.proximo
            aux = Node(item)
            aux.proximo = p.proximo
            p.proximo = aux
            self.tam += 1
        else:
            print('opc inv')

    #imprimir
    def imprimir(self):
        p = self.inicio
        for i in range(self.tam):
            p = p.proximo
            print(p.item)
        print('------')

    #remover
    def remover(self, pos):
        if not self.listavazia() and pos < self.tam:
            p = self.inicio
            for i in range(pos):
                p = p.proximo
            aux = p.proximo
            p.proximo = aux.proximo
            item = aux.item 
            del aux
            self.tam -= 1
            return item
        else:
            print('opc inv')
    
    #pesquisa
    def pesquisar (self, item):
        p = self.inicio
        if not self.listavazia():
            for i in range(self.tam):
                p = p.proximo
                if item == p.item:
                    return item
            return None
        else:
            print("Operação Inválida!")

#main
lista = Lista_Encadeada()
lista.inserir('A', 0)
lista.inserir('B', 1)
lista.inserir('C', 2)
e = lista.pesquisar("B")
if e == None:
    print("Não foi encontrado.")

lista.imprimir()

print('rem ' + lista.remover(1))