class Celula:
    item = None
    proximo = None

    def __init__(self,item):
        self.item  = item

class Lista_Encadeada:
    inicio = None
    quantidade = None

    def __init__(self):
        self.quantidade = 0

    #verificar se esta vazia
    def estaVazia(self):
        return self.quantidade == 0

    #inserir
    def inserir(self,pos,item):
        if self.estaVazia():
            self.inicio = Celula(item)
            self.quantidade+=1
        else:
            if pos <= self.quantidade + 1:
                p = self.inicio
                for i in range(pos-1):
                    p = p.proximo
                aux = Celula(item)
                aux.proximo = p.proximo
                p.proximo = aux
                self.quantidade +=1
            else:
                print('operacao invalida')

    #remover
    def remover(self,pos):
        if not self.estaVazia():
            if pos <= self.quantidade:
                if pos == 0:
                    aux = self.inicio
                    self.inicio = aux.proximo
                    item = aux.item
                    del aux
                    self.quantidade -= 1
                    return item
                else:
                    p = self.inicio
                    for i in range(pos-1):
                        p = p.proximo
                    aux = p.proximo
                    item = aux.item
                    p.proximo = aux.proximo
                    self.quantidade -=1
                    del aux
                    return item
            else:
                print('operacao invalida')
        else:
            print('operacao invalida')

    #imprimir
    def imprimir(self):
        p = self.inicio
        while p!= None:
            print(p.item,end=' ')
            p = p.proximo
        print('\n---')












# class Celula:
#     item = None
#     proximo = None

#     def __init__(self, item):
#         self.item = item

# class Lista_Encadeada:
#     inicio = None
#     quantidade = None

#     def __init__(self):
#         self.quantidade = 0

#     def estaVazia(self):
#         return self.quantidade == 0

#     def inserir(self,pos,item):
#         if pos<=self.quantidade:
#             if self.estaVazia():
#                 self.inicio = Celula(item)
#             else:
#                 p = self.inicio
#                 for i in range(pos-1):
#                     p = p.proximo
#                 aux = Celula(item)
#                 aux.proximo = p.proximo
#                 p.proximo = aux
#             self.quantidade+=1
#         else:
#             print('operação inválida')

#     def remover(self,pos):
#         if not self.estaVazia() and pos <=self.quantidade:
#             if self.quantidade == 1:
#                 self.inicio = None
#                 self.quantidade = 0
#             else: 
#                 p = self.inicio
#                 for i in range(pos-1):
#                     p = p.proximo
#                 aux = p.proximo
#                 p.proximo = aux.proximo
#                 item = aux.item
#                 del aux
#                 self.quantidade -= 1
#                 return item 
#         else:
#             print('operação inválida')

#     def imprimir(self):
#         p = self.inicio
#         while p!=None:
#             print(p.item,end=' ')
#             p = p.proximo
#         print('\n---')
                