class TabelaHash:
    tam_max = None
    tabela = None
    tamanho = None
    
    
    #criar tabela hash vazia
    def __init__ (self, tam_max):
        self.tam_max = tam_max
        self.tabela = [None] * tam_max
        self.tamanho = 0

    #verificar se esta vazia
    def estaVazia(self):
        return (self.tamanho == 0)

    #verificar se esta cheia
    def estaCheia(self):
        return (self.tamanho == self.tam_max)
    
    #funcao hash
    def funcao_hash(self, item):
        return item % self.tam_max
    
    #funcao rehash 
    def funcao_rehash(self, item):
        return (item + 1) % self.tam_max

    #inserir
    def inserir(self, item):
        if (not self.estaCheia()):
            self.tamanho += 1
            indice = self.funcao_hash(item)
            if (self.tabela[indice] == None):
                self.tabela[indice] = item
            else:
                while (self.tabela[indice] != None):
                    indice = self.funcao_rehash(indice)
                self.tabela[indice] = item
        else:
            print("A tabela está cheia.")

    #imprimir
    def imprimir(self):
        for i in range(self.tam_max):
            #print("[%d]" % i)
            if (self.tabela[i] != None):
                print("[{}] {}".format(i, self.tabela[i]))
        print("=====")

    #busca por item
    def busca (self, item):
        if (not self.estaVazia):
            indice = self.funcao_hash(item)
            if (self.tabela[indice] != item):
                indice_original = indice
                while (self.tabela[indice] != item):
                    indice = self.funcao_rehash(indice)
                    if (indice == indice_original):
                        print("Elemento não encontrado.")
                        return None
            
            return indice
        else:
            print("A tabela está vazia.")

    #remover
    def remove(self, item):
        if (not self.estaVazia()):
            indice = self.busca(item)
            if (indice != None):
                temp = self.tabela[indice]
                self.tamanho -= 1
                self.tabela[indice] = None
                return temp
        else:
            print("A tabela está vazia.")

tabela = TabelaHash(10)
tabela.inserir(16)
tabela.inserir(2)
tabela.inserir(3)
tabela.inserir(4)
tabela.inserir(5)
tabela.inserir(6)
tabela.inserir(7)
tabela.inserir(8)
tabela.inserir(9)
tabela.imprimir()
print(" %d " % tabela.busca(1))