class Celula:
    item = None
    proximo = None

    def __init__(self,item):
        self.item = item

class PilhaEncadeada:
    topo = None
    tamanho = 0

	#verificar se esta vazia
    def estaVazia(self):
        return True if self.tamanho==0 else False

	# #empilhar
    def empilhar(self,item):
        aux = self.topo #guarda referencia para o topo anterior
        self.topo = Celula(item) #cria novo topo
        self.topo.proximo = aux  #informa quem eh o proximo do topo (celula anterior)
        self.tamanho +=1

	#desempilhar
    def desempilhar(self):
        if not self.estaVazia():
            item = self.topo.item
            self.topo = self.topo.proximo
            self.tamanho -=1
            return item
        else:
            return ''

	#verificar tamanho
    def verTamanho(self):
        return self.tamanho

	#imprimir	
    def imprimir(self):
        aux = self.topo
        while aux!=None:
            print(aux.item)
            aux = aux.proximo
        print('---')
