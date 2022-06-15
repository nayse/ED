from pilha import Pilha
from pilha_encadeada import PilhaEncadeada

def main():
    pilha = PilhaEncadeada()
    pilha.empilhar('ana')
    pilha.empilhar('jorge')
    pilha.empilhar('pedro')
    pilha.empilhar('carla')
    pilha.imprimir()
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.desempilhar()
    pilha.imprimir()
    pilha.empilhar('gustavo')
    pilha.empilhar('joana')
    pilha.imprimir()

main()